import requests
from http import HTTPStatus


class BoardsOperations:
    def __init__(self, api_key: str, api_token: str) -> None:
        self.api_key = api_key
        self.api_token = api_token

    def get_info_about_all_available_boards(self) -> requests.Response:
        url = 'https://api.trello.com/1/members/me/boards'

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.api_token,
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response


class Board:
    def __init__(self, name: str, api_key: str, api_token: str) -> None:
        self.name = name
        self.api_key = api_key
        self.api_token = api_token
        self.board_id = None
        self.last_response = self.__create_a_new_board()

    def __create_a_new_board(self) -> requests.Response:
        url = "https://api.trello.com/1/boards/"

        query = {
            'name': self.name,
            'key': self.api_key,
            'token': self.api_token
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )
        self.set_board_id(response.json()["id"])
        return response

    def delete_a_board(self) -> None:
        url = f"https://api.trello.com/1/boards/{self.board_id}"

        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        response = requests.request(
            "DELETE",
            url,
            params=query
        )

        self.set_last_response(response)

        if response.status_code == HTTPStatus.OK:
            print("Board successfully deleted")
        else:
            print("Board was not deleted")

    def set_board_id(self, board_id: int) -> None:
        self.board_id = board_id

    def set_last_response(self, response: requests.Response) -> None:
        self.last_response = response

    def get_last_response(self) -> requests.Response:
        return self.last_response

    def get_board_id(self) -> int:
        return self.board_id
