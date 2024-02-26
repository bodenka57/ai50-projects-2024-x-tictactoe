"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_num += 1
            elif cell == O:
                o_num += 1
    if x_num - o_num == 1:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
        for j in range(3):
            board_1[i][j] = board[i][j]
    i, j = action
    if board_1[i][j] is not None:
        raise Exception
    board_1[i][j] = player(board)
    return board_1


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def game_value(board):
    if terminal(board):
        return utility(board), None

    pl = player(board)

    if pl == X:

        # get a set with all possible actions and their values
        actions_set = set()
        for i, j in actions(board):
            board_r = result(board, (i, j))
            val, act = game_value(board_r)
            actions_set.add((val, (i, j)))

        # choose the maximal value
        value = -1
        action = (1,1)
        for val, act in actions_set:
            if val >= value:
                value = val
                action = act

        return value, action

    # the same for O
    if pl == O:
        actions_set = set()
        for i, j in actions(board):
            board_r = result(board, (i, j))
            val, act = game_value(board_r)
            actions_set.add((val, (i, j)))
        value = 1
        action = (1,1)
        for val, act in actions_set:
            if val <= value:
                value = val
                action = act
        return value, action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    value, action = game_value(board)
    return action
