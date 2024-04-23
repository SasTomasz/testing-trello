from http import HTTPStatus

from dotenv import dotenv_values
from assertpy import assert_that

from python_api_testing.src.models.board_model import board_main_keys

env = dotenv_values("../../.env")
api_key = env.get("TRELLO_API_KEY")
api_token = env.get("TRELLO_API_TOKEN")


def test_create_new_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board()
    board_response = board.board_body
    assert assert_that(board_response.status_code).is_equal_to(HTTPStatus.OK)


def test_new_board_should_have_a_correct_name(create_a_new_board):
    expected_board_name = "my-new-board"
    board = create_a_new_board(expected_board_name)
    assert assert_that(board.board_name).is_equal_to(expected_board_name)


def test_new_board_should_return_a_correct_keys(create_a_new_board):
    board = create_a_new_board()
    board_response = board.board_body
    assert assert_that(board_response.json()).contains_key(*board_main_keys)


def test_adding_new_card_should_return_status_200(create_a_new_board):
    card_name = "automate_api_test_card"
    board = create_a_new_board
    first_list_id = board.board_id

    card_response = board.create_a_new_card(card_name, first_list_id)
    assert assert_that(card_response.status_code).is_equal_to(200)

