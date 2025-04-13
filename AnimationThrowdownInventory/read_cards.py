import requests


# Output file
def generate_cards_file(user_id, password_hash):
    output_file = "output/cards-w-id-and-rarity.txt"

    url = f"https://cb-live.synapse-games.com/api.php?message=init&user_id={user_id}"
    data = {'password': password_hash}
    response = requests.post(url, data=data)

    # Save to temporary file (optional)
    with open("temp/user.json", "w") as f:
        f.write(response.text)

    print("retrieved user.json")

    # Parse and format card data
    card_data = response.json().get("card_data", [])
    formatted_lines = []

    for card in card_data:
        card_id = card.get("id")
        rarity = card.get("rarity")
        name = card.get("name", "").strip()
        if card_id and rarity and name:
            formatted_lines.append(f"{card_id} {rarity} {name}")

    # Remove duplicates and sort
    formatted_lines = sorted(set(formatted_lines))

    # Write to file
    with open(output_file, "w") as f:
        for line in formatted_lines:
            f.write(line + "\n")

    print(f"wrote {output_file}")
