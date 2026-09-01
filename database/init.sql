CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INTEGER,
    is_active BOOLEAN NOT NULL
);

INSERT INTO users (
    id,
    username,
    email,
    age,
    is_active
)
VALUES
    (1, 'anna', 'anna@test.com', 25, TRUE),
    (2, 'alex', 'alex@test.com', 30, TRUE),
    (3, 'maria', 'maria@test.com', 28, FALSE);