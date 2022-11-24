"""2022-11-20 09:08:57"""


def greet(user_name: str = None) -> str:
    """This functions greets you on the console. Send an argument to user_name parameter to set the
    name of the person to greet, or leave it empty to greet the world."""

    if user_name is None:
        user_name = 'World!'
    else:
        user_name = ''.join([user_name, '.'])

    if not isinstance(user_name, str):
        raise TypeError("Parameter user_name, is not of type str (string)")

    return f"Hello, {user_name}"


if __name__ == '__main__':
    greet()
