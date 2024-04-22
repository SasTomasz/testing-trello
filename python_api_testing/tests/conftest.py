from http import HTTPStatus

import pytest
from dotenv import dotenv_values

from python_api_testing.src import base_workflow
from python_api_testing.src.main_workflow import Board

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


@pytest.fixture()
def create_a_new_board():
    board = Board("automate-api-tests", api_key, api_token)
    yield board.get_last_response()
    board.delete_a_board()


@pytest.fixture()
def get_info_about_lists_on_the_board():
    def _get_info_about_lists_on_the_board(board_id):
        return base_workflow.get_info_about_lists_on_board(board_id, api_key, api_token)
    return _get_info_about_lists_on_the_board
