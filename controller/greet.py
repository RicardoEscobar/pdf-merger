import tkinter as tk


def greet(user_name: str = None) -> None:
    """This functions greets you on the console. Send an argument to user_name parameter to set the
    name of the person to greet, or leave it empty to greet the world."""

    print(f"Hello, {user_name or 'World!'}")
