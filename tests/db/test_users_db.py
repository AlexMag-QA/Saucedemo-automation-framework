import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "user_id, expected_username",
    [
        (1, "anna"),
        (2, "alex"),
        (3, "maria"),
    ]
)
def test_users_exist_in_database(
        users_repository,
        user_id,
        expected_username
):
    user = users_repository.get_user_by_id(user_id)

    assert user is not None
    assert user["id"] == user_id
    assert user["username"] == expected_username


@pytest.mark.regression
def test_nonexistent_user_is_not_found(users_repository):
    user_id = 999999

    user = users_repository.get_user_by_id(user_id)

    assert user is None


@pytest.mark.regression
def test_update_user_age_with_rollback(users_repository):
    user_id = 3
    new_age = 99

    users_repository.update_user_age(user_id, new_age)

    user = users_repository.get_user_by_id(user_id)

    assert user is not None
    assert user["age"] == new_age


@pytest.mark.regression
def test_create_user_with_rollback(users_repository):
    user_id = 100
    username = "test_user"
    email = "test_user@test.com"
    age = 30
    is_active = True

    users_repository.create_user(user_id, username, email, age, is_active)

    user = users_repository.get_user_by_id(user_id)

    assert user is not None
    assert user["id"] == user_id
    assert user["username"] == username
    assert user["email"] == email
    assert user["age"] == age
    assert user["is_active"] == is_active
