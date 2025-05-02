from collections import Counter
import re

def read_file(file_path:str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter = Counter(words)
    number_of_words: int = len(lowered_text.split())

    print(f"Number of Words in this Text are: {number_of_words} ")
    print(60 * "-")
    return word_counts.most_common()


def main():
    text: str = input("Enter Your Text: ").strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    for word, count in word_frequencies:
        print(f"{word}: {count} ")


if __name__ == "__main__":
    main()
