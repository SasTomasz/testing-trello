# Trello API documentation is available at https://developer.atlassian.com/cloud/trello/rest/api-group-actions/

import requests
from dotenv import dotenv_values


def create_a_new_card(card_name: str, id_list: str, api_key: str, api_token: str) -> requests.Response:
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': id_list,
        'key': api_key,
        'token': api_token,
        'name': card_name
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return response


def get_info_about_all_available_boards(api_key: str, api_token: str) -> requests.Response:
    url = 'https://api.trello.com/1/members/me/boards'

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': api_key,
        'token': api_token,
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    return response


def create_a_new_list(name: str, board_id: str, api_key: str, api_token: str) -> requests.Response:

    url = "https://api.trello.com/1/lists"

    query = {
        'name': name,
        'idBoard': board_id,
        'key': api_key,
        'token': api_token
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    return response


def create_a_new_board(name: str, api_key: str, api_token: str) -> requests.Response:
    url = "https://api.trello.com/1/boards/"

    query = {
        'name': name,
        'key': api_key,
        'token': api_token
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    return response


def get_info_about_lists_on_board(board_id: str, api_key: str, api_token: str) -> requests.Response:
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': api_key,
        'token': api_token
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    return response


def delete_a_board(board_id: str, api_key: str, api_token: str) -> requests.Response:
    url = f"https://api.trello.com/1/boards/{board_id}"

    query = {
        'key': api_key,
        'token': api_token
    }

    response = requests.request(
        "DELETE",
        url,
        params=query
    )

    return response


if __name__ == '__main__':
    env_variables = dotenv_values("../../.env")
    trello_api_key = env_variables.get("TRELLO_API_KEY")
    trello_api_token = env_variables.get("TRELLO_API_TOKEN")

    create_board_response = create_a_new_board("my-test-board", trello_api_key, trello_api_token)
    created_board_id = create_board_response.json()["id"]
    lists_on_board_info = get_info_about_lists_on_board(created_board_id, trello_api_key, trello_api_token)
    print(lists_on_board_info.content)
