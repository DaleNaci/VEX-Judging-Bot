import requests

from .config import API_KEY, BASE_URL


def get_match_list(id: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    endpoint = f"/events/{id}/divisions/1/matches?team=141070"

    response = requests.get(BASE_URL+endpoint, headers=headers)
    response.raise_for_status()

    return response.json()