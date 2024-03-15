"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
T = "Tie"
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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if count % 2 == 0:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    listOfActions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                listOfActions.append((i, j))
    return listOfActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if board[action[0]][action[1]] == None:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise NameError('Invalid Move')

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    return T

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][1] != None:
            return True
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[1][i] != None:
            return True
    if board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[1][1] != None:
        return True
    if board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[1][1] != None:
        return True
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if count == 0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][1] != None:
            if board[i][1] == X:
                return 1
            return -1
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[1][i] != None:
            if board[1][i] == X:
                return 1
            return -1
    if board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[1][1] != None:
        if board[1][1] == X:
            return 1
        return -1
    if board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[1][1] != None:
        if board[1][1] == X:
            return 1
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return optimumAction(board)[1]

def optimumAction(board):
    actio = actions(board)
    playe = player(board)
    if playe == X:
        action = None
        ma = -2
        for i in range(len(actio)):
            new_board = result(board, actio[i])
            if terminal(new_board):
                utilit = utility(new_board)
                if utilit == 1:
                    return (1, actio[i])
                if utilit == 0:
                    ma = 0
                    action = actio[i]
                continue
            else:
                new_action = optimumAction(new_board)[0]
                if max(new_action, ma) == new_action:
                    ma = new_action
                    action = actio[i]
        return (ma, action)
    else:
        action = None
        mi = 2
        for i in range(len(actio)):
            new_board = result(board, actio[i])
            if terminal(new_board):
                utilit = utility(new_board)
                if utilit == -1:
                    return (-1, actio[i])
                if utilit == 0:
                    mi = 0
                    action = actio[i]
                continue
            else:
                new_action = optimumAction(new_board)[0]
                if min(new_action, mi) == new_action:
                    mi = new_action
                    action = actio[i]
        return (mi, action)

def min(a, b):
    if a > b:
        return b
    else:
        return a

def max(a, b):
    if a > b:
        return a
    else:
        return b