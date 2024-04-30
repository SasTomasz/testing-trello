import importlib.resources

import pytest
from dotenv import dotenv_values

from src.testing_trello.main_workflow import Board

env_path = str(importlib.resources.files("src").joinpath("testing_trello/.env"))
env = dotenv_values(env_path)
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


@pytest.fixture()
def create_a_new_board(request):
    def _create_a_new_board(board_name: str = "automate-api-tests"):
        board = Board(board_name, api_key, api_token)
        request.addfinalizer(lambda: board.delete_a_board())
        return board
    # It has to be a function reference instead of function call here
    return _create_a_new_board
