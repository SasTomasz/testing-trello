from http import HTTPStatus

from python_api_testing.src import base_workflow
from dotenv import dotenv_values

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


def test_create_new_board_should_return_status_200(create_a_new_board):
    board_response = create_a_new_board
    assert board_response.status_code == HTTPStatus.OK


def test_adding_new_card_should_return_status_200(create_a_new_board, get_info_about_lists_on_the_board):
    card_name = "automate_api_test_card"
    board_response = create_a_new_board
    board_id = board_response.json()["id"]
    first_list_id = get_info_about_lists_on_the_board(board_id).json()[0]["id"]

    function_result = base_workflow.create_new_card(card_name, first_list_id, api_key, api_token)
    assert function_result.status_code == 200

