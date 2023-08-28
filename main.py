import typer

from src.logic import ReadText
from src.utils.helpers import load_config

config = load_config()
default_wpm = config.get("default_wpm")


def main(text_file_path: str, words_per_minute: int = default_wpm):
    file_path = text_file_path

    print(f"Reading from file {text_file_path} at speed {words_per_minute} words per minute\n")

    text_reader = ReadText(file_path, words_per_minute)
    text_reader.start()


if __name__ == '__main__':
    typer.run(main)
