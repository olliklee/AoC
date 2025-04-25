import requests


def generate_user_file (output_file, user_id, password_hash):

    url = f"https://cb-live.synapse-games.com/api.php?message=init&user_id={user_id}"
    data = {'password': password_hash}
    response = requests.post(url, data=data)

    with open(output_file, "w") as f:
        f.write(response.text)

    print(f"Generated {output_file}")