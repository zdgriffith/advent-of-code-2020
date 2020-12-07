from pathlib import Path

from one import parse_rules, get_all_content


if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    with fpath.open() as f:
        color_rules = {}
        for r in f.readlines():
            color_rules |= parse_rules(r.strip())

    _, total = get_all_content(color_rules, "shiny gold")
    print(total)
