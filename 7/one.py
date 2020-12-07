from pathlib import Path


def parse_rules(rule):
    parent, children = rule.split(" contain ")
    parent = parent.replace(" bags", "")
    if "no other bags" in rule:
        return {parent: {}}
        
    relations = {parent: {}}
    children = children.replace(" bags", "").replace(" bag", "").replace(".", "").split(", ")
    for child in children:
        child_num = int(child.split(" ")[0])
        child_color = " ".join(child.split(" ")[1:])
        relations[parent] |= {child_color: child_num}
    return relations


def get_all_content(color_rules, color, multiplier=1):
    children = []
    total = 0
    for child, amount in color_rules[color].items():
        sub_children, sub_total = get_all_content(color_rules, child, amount)
        children.append(child)
        children.extend(sub_children)
        total += multiplier * amount
        total += multiplier * sub_total
    return children, total

if __name__ == "__main__":  
    fpath = Path(__file__).parent / "input.txt"
    with fpath.open() as f:
        color_rules = {}
        for r in f.readlines():
            color_rules |= parse_rules(r.strip())

    has_gold = 0 
    for color in color_rules:
        children, _ = get_all_content(color_rules, color)
        has_gold += "shiny gold" in children
    print(has_gold)
