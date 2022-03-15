from data.user import User


def user_count() -> int:
    return 10


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, 'abc')