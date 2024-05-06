from http import HTTPStatus

from assertpy import assert_that

from src.models.board_model import board_main_keys


def test_create_new_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board()
    board_response = board.board_body
    assert_that(board_response.status_code).is_equal_to(HTTPStatus.OK)


def test_delete_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board()
    board.delete_a_board()
    board_response_after_delete = board.board_body
    assert_that(board_response_after_delete.status_code).is_equal_to(HTTPStatus.OK)


def test_get_info_about_list_on_the_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board()
    response = board.get_info_about_lists_on_board()
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)


def test_create_new_list_on_the_board_should_return_status_200(create_a_new_board):
    board = create_a_new_board()
    created_list = board.create_a_new_list_on_board("new_test_list")
    list_data = created_list.get_list_data()
    assert_that(list_data.status_code).is_equal_to(HTTPStatus.OK)


def test_list_created_on_a_board_should_has_correct_name():
    pass


def test_create_new_list_on_the_board_should_return_correct_keys():
    assert False


def test_new_board_should_have_a_correct_name(create_a_new_board):
    expected_board_name = "my-new-board"
    board = create_a_new_board(expected_board_name)
    assert_that(board.board_name).is_equal_to(expected_board_name)


def test_new_board_should_return_a_correct_keys(create_a_new_board):
    board = create_a_new_board()
    board_response = board.board_body
    assert_that(board_response.json()).contains_key(*board_main_keys)


def test_adding_new_card_should_return_status_200(create_a_new_board):
    card_name = "automate_api_test_card"
    board = create_a_new_board
    first_list_id = board.board_id

    card_response = board.create_a_new_card(card_name, first_list_id)
    assert_that(card_response.status_code).is_equal_to(200)

