from pathlib import Path

import pytest

from src.utils import LineReader


def test_LineReader_lines_ok():
    """
    Tests if correct lines are returned, empty lines are skipped and StopIteration is reached
    :return: None
    """

    line_reader = LineReader(Path("tests/test_fiels_text.txt"))
    line_generator = line_reader.next_line_generator()
    line1 = next(line_generator)
    line2 = next(line_generator)

    assert line1 == "this is a test line1"
    assert line2 == "this is a test line2"

    with pytest.raises(StopIteration) as ex_info:
        next(line_generator)
    assert ex_info.type is StopIteration
