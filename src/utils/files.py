import atexit
from pathlib import Path


class LineReader:
    def __init__(self, file_path: Path, encoding="utf8"):
        """
        Opens file and sets up atexit
        :param file_path: Path to the text file
        :param encoding: Default utf8
        """

        self.file = file_path.open("r", encoding=encoding)

        atexit.register(self._quit)

    def _quit(self):
        """
        Closes file
        :return: None
        """
        self.file and self.file.close()

    def next_line_generator(self):
        """
        sets up a generator, returns next linen from a file
        :return:
        """
        for line in self.file:
            if line.strip() == "":
                continue

            yield line.strip()
