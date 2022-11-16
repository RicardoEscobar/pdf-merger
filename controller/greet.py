import tkinter as tk

def greet(user_name: str = None) -> None:
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name or 'World!'}")