from pathlib import Path

from one import convert_ids

if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    with Path(fpath).open() as f:
        ids = convert_ids([r.strip()for r in f.readlines()])

    for id in range(min(ids), max(ids)):
        if id not in ids and id + 1 in ids and id - 1 in ids:
            print(id)
