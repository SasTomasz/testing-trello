from dotenv import dotenv_values

from src.testing_trello.main_workflow import Board

if __name__ == '__main__':
    env_variables = dotenv_values(".env")
    api_key = env_variables["TRELLO_API_KEY"]
    api_token = env_variables["TRELLO_API_TOKEN"]

    board = Board("my_test_board", api_key, api_token)
    print(board.board_body.json())
