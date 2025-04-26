import json


def generate_decks_file(input_file):
    units_out = "output/units-w-levels.txt"
    cm_out = "output/ids-with-cm.txt"

    # Parse and format card data
    with open(input_file) as f:
        data = json.load(f)
        card_data = data['user_decks']
    
    # Process user_units
    unit_lines = []
    for unit in data.get("user_units", []):
        uid = unit.get("unit_id")
        level = unit.get("level")
        mastery = unit.get("mastery_level")
        if uid is not None and level is not None and mastery is not None:
            unit_lines.append(f"{uid} {level} {mastery}")
    
    unit_lines = sorted(unit_lines)
    with open(units_out, "w") as f:
        for line in unit_lines:
            # Replacing ', ' with '-' not necessary here, since we don't have commas.
            f.write(line + "\n")
    
    # debug output
    print(f"wrote {units_out}")
    print(f"{len(unit_lines)} lines in {units_out}")
    
    # Process user_combo_mastery
    cm_lines = []
    for cm in data.get("user_combo_mastery", []):
        cid = cm.get("id")
        level = cm.get("level")
        if cid is not None and level is not None:
            cm_lines.append(f"{cid} {level}")
    
    cm_lines = sorted(cm_lines)
    with open(cm_out, "w") as f:
        for line in cm_lines:
            f.write(line + "\n")
            
    # debug output
    print(f"wrote {cm_out}")
    print(f"{len(cm_lines)} lines in {cm_out}")