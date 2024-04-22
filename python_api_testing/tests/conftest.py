import pytest
from dotenv import dotenv_values

from python_api_testing.src.main_workflow import Board

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


@pytest.fixture()
def create_a_new_board():
    board = Board("automate-api-tests", api_key, api_token)
    yield board
    board.delete_a_board()
