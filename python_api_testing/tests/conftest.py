from http import HTTPStatus

import pytest
from python_api_testing.src import base_workflow
from dotenv import dotenv_values

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


@pytest.fixture()
def create_a_new_board():
    board_name = "automate-api-tests"
    create_response = base_workflow.create_a_new_board(board_name, api_key, api_token)
    yield create_response
    board_id = create_response.json()["id"]
    delete_response = base_workflow.delete_a_board(board_id, api_key, api_token)
    if delete_response.status_code == HTTPStatus.OK:
        print("Board deleted after test")


@pytest.fixture()
def get_info_about_lists_on_the_board():
    def _get_info_about_lists_on_the_board(board_id):
        return base_workflow.get_info_about_lists_on_board(board_id, api_key, api_token)
    return _get_info_about_lists_on_the_board
