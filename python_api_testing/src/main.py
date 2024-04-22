from main_workflow import Board, List
from dotenv import dotenv_values

if __name__ == '__main__':
    env_variables = dotenv_values("../../.env")
    api_key = env_variables["TRELLO_API_KEY"]
    api_token = env_variables["TRELLO_API_TOKEN"]

    board = Board("my_test_board", api_key, api_token)
    my_test_board_list = board.create_a_new_list_on_board("my_test_list")
    my_test_board_list_data = my_test_board_list.get_list_data()
    print(my_test_board_list_data.content)

