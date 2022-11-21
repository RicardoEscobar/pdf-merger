from pathlib import Path


def str_to_path(path_collection: list | tuple) -> list | tuple:
    """This function recieves a list or tuple, loops through it and converts it's elements from str
    to Path."""

    result = map(lambda path: Path(path)
                 if isinstance(path, str)
                 else path,
                 path_collection)

    if isinstance(path_collection, list):
        return list(result)
    else:
        return tuple(result)
