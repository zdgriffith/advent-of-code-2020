from pathlib import Path

fields = {'hcl', 'pid', 'ecl', 'hgt', 'iyr', 'byr', 'eyr'}


def parse_fields(row):
    return {k: v for k, v in [kv.split(":") for kv in row.split(" ")]}


def validate_fields(passport):
    return set(passport.keys()).issuperset(fields)


if __name__ == "__main__":
    passports = [{}]
    fpath = Path(__file__).parent / "input.txt"
    with fpath.open() as f:
        for r in f.readlines():   
            if not r.strip():
                passports.append({})
                continue
            passports[-1] |= parse_fields(r.strip())
    print(sum([validate_fields(p) for p in passports]))
