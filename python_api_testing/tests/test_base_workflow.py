from http import HTTPStatus

from dotenv import dotenv_values

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


def test_create_new_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board
    board_response = board.get_a_board_body()
    assert board_response.status_code == HTTPStatus.OK


def test_adding_new_card_should_return_status_200(create_a_new_board):
    card_name = "automate_api_test_card"
    board = create_a_new_board
    first_list_id = board.get_info_about_lists_on_board().json()[0]["id"]

    card_response = board.create_a_new_card(card_name, first_list_id)
    assert card_response.status_code == 200

