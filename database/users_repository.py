class UsersRepository:

    def __init__(self, cursor):
        self.cursor = cursor

    def get_user_by_id(self, user_id):
        self.cursor.execute(
            """
            SELECT id, username, email, age, is_active
            FROM users
            WHERE id = %s;
            """,
            (user_id,)
        )

        return self.cursor.fetchone()

    def update_user_age(self, user_id, new_age):
        self.cursor.execute(
            """
            UPDATE users
            SET age = %s
            WHERE id = %s;
            """,
            (new_age, user_id)
        )

    def create_user(self, user_id, username, email, age, is_active):
        self.cursor.execute(
            """
            INSERT INTO users (id, username, email, age, is_active)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (user_id, username, email, age, is_active)
        )
