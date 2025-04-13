from typing import Optional
from tabulate import tabulate


def print_combo_mastery_table(
    ids_with_cm_file="output/ids-with-cm",
    cards_file="output/cards-w-id-and-rarity",
    output_file: Optional[str] = None,
    as_table: bool = True
):
    # Load card ID → name mapping
    card_lookup = {}
    with open(cards_file, "r") as f:
        for line in f:
            parts = line.strip().split(" ", 2)
            if len(parts) == 3:
                card_id, _, name = parts
                card_lookup[card_id] = name

    # Parse cm levels and look up names
    cm_entries = []
    with open(ids_with_cm_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "-" not in line:
                continue
            unit_id, cm_level = line.split("-", 1)
            name = card_lookup.get(unit_id)
            if name:
                try:
                    cm_entries.append((int(cm_level), name))
                except ValueError:
                    pass  # skip malformed cm_level

    # Sort: first by name (asc), then by cm (desc)
    cm_entries.sort(key=lambda x: x[1])  # sort by name
    cm_entries.sort(key=lambda x: x[0], reverse=True)  # sort by cm descending

    # Format as table or simple lines
    if as_table:
        table = tabulate(cm_entries, headers=["CM", "Name"], tablefmt="github")
        output = table
    else:
        output = "\n".join(f"{cm} | {name}" for cm, name in cm_entries)

    if output_file:
        with open(output_file, "w") as f:
            f.write(output + "\n")
        print(f"Wrote output to {output_file}")
    else:
        print(output)