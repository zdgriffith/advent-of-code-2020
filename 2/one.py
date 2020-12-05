from pathlib import Path


def is_valid(row):
    policy, password = row.split(": ")
    valid_range, letter = policy.split(" ")
    low, high = (int(i) for i in valid_range.split("-"))
    counts = password.count(letter)
    return (counts >= low) & (counts <= high)


if __name__ == "__main__":
    count = 0
    fpath = Path(__file__).parent / "input.txt"
    with fpath.open() as f:
        for r in f.readlines():
            count += is_valid(r.strip())
    print(count) 

