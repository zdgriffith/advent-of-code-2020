from pathlib import Path


if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    total = 0
    with fpath.open() as f:
        questions = set()
        for r in f.readlines():
            r = r.strip()
            if not r:
                total += len(questions)
                questions = set()
            questions |= set([l for l in r])
        else:
            total += len(questions)
    print(total)
