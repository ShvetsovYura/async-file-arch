from pathlib import Path


def save_to_file(data: bytes, path: Path) -> None:
    with open(path, mode="wb") as fb:
        fb.write(data)
