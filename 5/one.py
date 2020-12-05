from pathlib import Path


def bin_sum(sections):
    total = 0
    for i, is_back in enumerate(sections):
        if is_back:
            total += 2**i
    return total 


def parse_sections(sections, key):
    return reversed([0 if i == key else 1 for i in sections])


def convert_ids(seat_list):
    ids = []
    for sections in seat_list:
        row = bin_sum(parse_sections(sections[:7], "F"))
        col = bin_sum(parse_sections(sections[7:], "L"))
        ids.append(row * 8 + col)
    return ids


if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    with Path(fpath).open() as f:
        ids = convert_ids([r.strip()for r in f.readlines()])
    print(max(ids))
