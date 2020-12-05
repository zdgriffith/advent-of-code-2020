from pathlib import Path

from one import parse_fields, validate_fields


ranges = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "cm": (150, 193),
    "in": (59, 76),
}
hcl_chars = set([str(i) for i in range(10)] + [c for c in "abcdef"])
valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def in_range(val, low, high):
    if not val.isdigit():
        return False
    return (int(val) >= low) and (int(val) <= high)


def validate_height(height):
    if height[-2:] not in ranges:
        return False
    return in_range(height[:-2], *ranges[height[-2:]])


def validate_hcl(hcl):
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    if set(hcl[1:]).difference(hcl_chars):
        return False
    return True


def validate_data(field, value):
    if field in ranges:
        return in_range(value, *ranges[field])
    elif field == "hgt":
        return validate_height(value)
    elif field == "hcl":
        return validate_hcl(value)
    elif field == "ecl":
        return value in valid_eye_colors
    elif field == "pid":
        return (len(value) == 9) and value.isdigit()
    else:
        return True


def validate(passport):
    if not validate_fields(passport):
        return False
    for field, value in passport.items():
        if not validate_data(field, value):
            return False
    return True


if __name__ == "__main__":
    passports = [{}]
    with Path("input.txt").open() as f:
        for r in f.readlines():   
            if not r.strip():
                passports.append({})
                continue
            passports[-1] |= parse_fields(r.strip())
    print(sum([validate(p) for p in passports]))
