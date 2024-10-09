import re
import json
from pathlib import Path
from pprint import pprint


def sorter(x: Path) -> int:
    with x.open("r") as fp:
        loaded = json.load(fp)
        return loaded["meta"]["order"]


def main():
    book_path = Path() / "boky"
    bookfiles = list(book_path.iterdir())
    bookfiles.sort(key=sorter)

    number = 0
    for bookfile in bookfiles:
        with bookfile.open("r") as fp:
            loaded = json.load(fp)
            # if loaded["meta"]["order"] < 39:
            #     continue

            for chapter in range(1, loaded["meta"]["chapter_number"] + 1):
                for verset in loaded[str(chapter)]:
                    number += 1
                #     text = loaded[str(chapter)][verset]
                #     number += len(re.findall("", text))

    print(number)


if __name__ == "__main__":
    main()
