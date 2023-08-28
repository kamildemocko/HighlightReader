from pathlib import Path

import pytest

from src.logic.logic import ReadText

file_path = "tests/test_story.py"


def test_prepare_line_of_text():
    read_text = ReadText(file_path)
    line_generator = read_text.line_generator

    words, times = read_text._prepare_line_of_text(next(line_generator), wpm=60)
    assert words == ['from', 'pathlib', 'import', 'Path']
    assert times == [0.7047619047619048, 1.2333333333333334, 1.0571428571428572, 0.7047619047619048]


def test_get_tick_for_char():
    read_text = ReadText(file_path)
    line_generator = read_text.line_generator

    words = next(line_generator).split()
    tick = read_text._get_tick_for_char(words, 60)

    assert tick == 0.1761904761904762
