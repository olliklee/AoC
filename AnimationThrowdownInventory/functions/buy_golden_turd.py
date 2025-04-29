import requests
import time
from typing import Optional


def _buy_golden_turd_item(user_id: str, password_hash: str) -> Optional[str]:
    """Kauft ein Item aus dem Store und gibt die unit_id zurück."""
    url = "https://cb-live.synapse-games.com/api.php"
    params = {"message": "buyStoreItem", "user_id": user_id}
    data = {
        "password": password_hash,
        "cost_type": "2",
        "item_id": "63",
        "quantity": "1"
    }

    response = requests.post(url, params=params, data=data)
    result = response.json()

    if not result.get("result"):
        print(f"Fehler: {result.get('result_message', ['Unbekannter Fehler'])[0]}")
        return None

    return result.get("new_units", [{}])[0].get("unit_id")


def buy_golden_turd_items(user_id: str, password_hash: str, count: int = 1):
    for i in range(count):
        unit_id = _buy_golden_turd_item(user_id, password_hash)

        if unit_id:
            print(f"Erhalten: {unit_id}")

        if i < count - 1:  # Nicht warten nach dem letzten Durchlauf
            time.sleep(4)
