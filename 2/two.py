from pathlib import Path


def is_valid(row):
    policy, password = row.split(": ")
    valid_range, letter = policy.split(" ")
    low, high = (int(i) for i in valid_range.split("-"))
    return (password[low - 1] == letter) ^ (password[high - 1] == letter)


if __name__ == "__main__":
    count = 0
    with Path("input.txt").open() as f:
        for r in f.readlines():
            count += is_valid(r.strip())
    print(count) 

