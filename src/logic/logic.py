from pathlib import Path
from time import sleep

import colorama
from colorama import Fore

from src.utils.helpers import load_config
from src.utils.files import LineReader


class ReadText:
    def __init__(self, file_path: str, wpm: int):
        self.config = load_config()
        colorama.init()
        self.wpm = wpm

        line_reader = LineReader(Path(file_path).resolve())
        self.line_generator = line_reader.next_line_generator()

    def _prepare_line_of_text(self, line: str) -> tuple[list[str], list[float]]:
        """
        Prepares line of text -> splits into words and adds time it should be highlighted
        :param line: line of text
        :param wpm: words per minute - tick
        :return: tuple of tuples - word and time
        """
        words = line.split()
        tick = self._get_tick_for_char(words, self.wpm)

        out_words = list()
        out_time = list()
        for word in words:
            out_words.append(word)
            out_time.append(len(word) * tick)

        return out_words, out_time

    def _get_tick_for_char(self, words: list[str], wpm: int) -> float:
        """
        Returns tick for char in a word in a line, including wait time between words
        :param words: tuple of words
        :param wpm: words per minute
        :return: seconds for a character
        """
        character_count = 0
        words_count = 0
        for word in words:
            for _ in word:
                character_count += 1
            words_count += 1

        wps = wpm / 60
        rate_per_line = words_count / wps - (words_count - 1) * self.config.get("wait_between_words")
        rate = rate_per_line / character_count
        return rate

    def start(self):
        """
        runs the show
        :return:
        """
        for line in self.line_generator:
            words, times = self._prepare_line_of_text(line)
            for index, (word, time) in enumerate(zip(words, times)):
                words_before = words[0:index]
                words_after = words[index + 1:len(words)]

                print(
                    f"\r{' '.join(words_before)}"
                    f"{' ' if index > 0 else ''}"
                    f"{word}"
                    f"{' ' if index < len(words) else ''}"
                    f"{Fore.LIGHTBLACK_EX}{' '.join(words_after).strip()}{Fore.RESET}",
                    end="",
                    flush=True)

                sleep(time)
                sleep(self.config.get("wait_between_words"))

            print()
            sleep(self.config.get("wait_between_lines"))
