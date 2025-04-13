def to_stars(rarity: int, level: int) -> str:
    max_level = {
        1: 3,
        2: 4,
        3: 5,
        4: 6,
        5: 7
    }.get(rarity, 6)

    stars = ""
    i = level
    while i > max_level:
        i -= max_level
        stars = "*" + stars

    return f"{i}{stars}"


def print_units_with_levels(
    cards_file="cards-w-id-and-rarity",
    levels_file="units-w-levels",
    output_file=None
):
    # Schritt 1: Caching unit_ID Variablen
    unit_vars = {}
    with open(cards_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" ", 2)
            if len(parts) < 3:
                continue
            unit_id, rarity, name = parts
            key = f"unit_{unit_id}"
            unit_vars[key] = f"{unit_id} {rarity} {name}"

    output_lines = []

    # Schritt 2: units-w-levels einlesen
    with open(levels_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split("-")
            unit_id = parts[0]
            try:
                level = int(parts[1])
            except (ValueError, IndexError):
                level = 0

            key = f"unit_{unit_id}"
            unit_data = unit_vars.get(key)

            if not unit_data:
                output_lines.append(f"Unknown unit: {unit_id}")
                continue

            _, rarity_str, name = unit_data.split(" ", 2)
            rarity = int(rarity_str)

            color = {
                1: "C",  # Common
                2: "R",  # Rare
                3: "E",  # Epic
                4: "L",  # Legendary
                5: "M"   # Mythic
            }.get(rarity, "?")

            stars = to_stars(rarity, level)
            output_lines.append(f"{color} {name}: {stars}")

    # Ausgabe
    if output_file:
        with open(output_file, "w") as f:
            f.write("\n".join(output_lines) + "\n")
        print(f"Wrote output to {output_file}")
    else:
        print("\n".join(output_lines))