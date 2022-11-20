"""2022-11-20 09:08:57"""


def greet(user_name: str = None) -> None:
    """This functions greets you on the console. Send an argument to user_name parameter to set the
    name of the person to greet, or leave it empty to greet the world."""

    if not isinstance(user_name, str) and user_name is not None:
        raise TypeError("Parameter user_name, is not of type str (string)")

    print(f"Hello, {user_name or 'World!'}")


if __name__ == '__main__':
    greet()
