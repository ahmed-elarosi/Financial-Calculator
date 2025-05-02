from collections import Counter
import re


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words:list[str]: = re.findall(r"")