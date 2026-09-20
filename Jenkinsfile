pipeline {
    agent {
        label 'linux'
    }

    environment {
        DB_HOST = 'localhost'
        DB_PORT = '5432'
        DB_NAME = 'qa_training'
        DB_USER = 'postgres'
        DB_PASSWORD = credentials('qa-db-password')

        ALLURE_HOME = '/mnt/v/Tools (QA)/allure-2.46.1'
        PATH = "${ALLURE_HOME}/bin:${env.PATH}"
    }

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }

    triggers {
        cron('H 2 * * *')
    }

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['smoke', 'regression'],
            description: 'Test suite to run'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Prepare reports directory') {
            steps {
                sh '''
                    rm -rf reports allure-results allure-report

                    mkdir -p \
                      reports \
                      allure-results/api \
                      allure-results/ui \
                      allure-results/db
                '''
            }
        }

        stage('Prepare Database') {
            steps {
                sh 'docker rm -f qa-postgres || true'

                sh '''
                    docker run -d \
                      --name qa-postgres \
                      -e POSTGRES_DB=qa_training \
                      -e POSTGRES_USER=postgres \
                      -e POSTGRES_PASSWORD="$DB_PASSWORD" \
                      -p 5432:5432 \
                      postgres:16
                '''

                sh '''
                    until docker exec qa-postgres pg_isready -U postgres; do
                        sleep 2
                    done
                '''

                sh '''
                    docker exec -i qa-postgres \
                      psql \
                      -U postgres \
                      -d qa_training \
                      < database/init.sql
                '''
            }
        }

        stage('Select Test Suite') {
            steps {
                script {
                    def timerBuild = currentBuild.getBuildCauses(
                        'hudson.triggers.TimerTrigger$TimerTriggerCause'
                    )

                    if (timerBuild) {
                        env.TEST_MARKER = 'regression'
                    } else {
                        env.TEST_MARKER = params.TEST_SUITE
                    }

                    echo "Running test suite: ${env.TEST_MARKER}"
                }
            }
        }

        stage('Tests') {
            parallel {
                stage('API Tests') {
                    steps {
                        sh '.venv/bin/pytest tests/api -m "$TEST_MARKER" -v --junitxml=reports/api-results.xml --alluredir=allure-results/api'
                    }
                }

                stage('UI Tests') {
                    steps {
                        sh '.venv/bin/pytest tests -m "$TEST_MARKER" -v --ignore=tests/api --ignore=tests/db --headless --junitxml=reports/ui-results.xml --alluredir=allure-results/ui'
                    }
                }

                stage('DB Tests') {
                    steps {
                        sh '.venv/bin/pytest tests/db -m "$TEST_MARKER" -v --junitxml=reports/db-results.xml --alluredir=allure-results/db'
                    }
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/*.xml'

            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [
                    [path: 'allure-results/api'],
                    [path: 'allure-results/ui'],
                    [path: 'allure-results/db']
                ]
            ])

            archiveArtifacts(
                artifacts: 'reports/*.xml',
                allowEmptyArchive: true
            )
        }

        cleanup {
            sh 'docker rm -f qa-postgres || true'
        }
    }
}