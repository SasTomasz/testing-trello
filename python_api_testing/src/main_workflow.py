# Trello API documentation is on https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-group-actions

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


class List:
    def __init__(self, list_name: str, list_id: str, board_id: str, api_key: str, api_token) -> None:
        self.list_name = list_name
        self.list_id = list_id
        self.board_id = board_id
        self.api_key = api_key
        self.api_token = api_token

    def create_a_new_card(self, card_name: str) -> requests.Response:
        url = "https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'idList': self.list_id,
            'key': self.api_key,
            'token': self.api_token,
            'name': card_name
        }

        response = requests.request(
            "POST",
            url,
            headers=headers,
            params=query
        )

        return response

    def get_list_data(self) -> requests.Response:
        url = f"https://api.trello.com/1/lists/{self.list_id}"

        query = {
            'key': self.api_key,
            'token': self.api_token
        }

        response = requests.request(
            "GET",
            url,
            params=query
        )

        return response


class Board:
    def __init__(self, board_name: str, api_key: str, api_token: str) -> None:
        self.board_name: str = board_name
        self.__api_key: str = api_key
        self.__api_token: str = api_token

        # Initialize in __create_a_new_board method
        self.board_body: requests.Response = self.__create_a_new_board()
        self.board_id: str = self.board_body.json()["id"]

    def __create_a_new_board(self) -> requests.Response:
        url = "https://api.trello.com/1/boards/"

        query = {
            'name': self.board_name,
            'key': self.__api_key,
            'token': self.__api_token
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )
        self.board_id = response.json()["id"]
        self.board_body = response
        return response

    def delete_a_board(self) -> None:
        url = f"https://api.trello.com/1/boards/{self.board_id}"

        query = {
            'key': self.__api_key,
            'token': self.__api_token
        }

        response = requests.request(
            "DELETE",
            url,
            params=query
        )

        self.board_body = response

        if response.status_code == HTTPStatus.OK:
            print("Board successfully deleted")
        else:
            print("Board was not deleted")

    def get_info_about_lists_on_board(self) -> requests.Response:
        url = f"https://api.trello.com/1/boards/{self.board_id}/lists"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.__api_key,
            'token': self.__api_token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response

    def create_a_new_list_on_board(self, list_name: str) -> List:

        url = "https://api.trello.com/1/lists"

        query = {
            'name': list_name,
            'idBoard': self.board_id,
            'key': self.__api_key,
            'token': self.__api_token
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )
        if response.status_code == HTTPStatus.OK:
            list_id = response.json()["id"]
            list_on_board = List(list_name, list_id, self.board_id, self.__api_key, self.__api_token)
            return list_on_board
        else:
            raise ConnectionError(f"Error when creating a list occurred. Http status code: {response.status_code}")


class Card:
    def __init__(self, card_name: str, list_id: str, api_key: str, api_token: str) -> None:
        self.card_name = card_name
        self.list_id = list_id
        self.api_key = api_key
        self.api_token = api_token
