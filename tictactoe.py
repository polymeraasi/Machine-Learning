"""
Tic Tac Toe Player
"""
import copy

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
    Returns player who has the next turn on a board. The player X will start.
    """

    count = 1
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != EMPTY:
                count += 1

    if count % 2 == 1:
        return X
    if count % 2 == 0:
        return O


def actions(board):
    """
    Returns set of all possible actions (row, col) available on the board (- those
    that are still empty).
    """

    action = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                action.add((row, col))
    return action

def result(board, action):
    """
    Returns the board that results from making move (row, col) on the board.
    If action is not a valid action for the board (3x3), the program should raise an exception.
    Original board is first deep copied before making changes to it. The returned board is a 'sum'
    of the original, plus the move which the player makes.
    """

    row, col = action
    if row > len(board) or row < 0 or col > len(board) or col < 0:
        raise IndexError

    copy_b = copy.deepcopy(board)  # making a deep copy
    copy_b[row][col] = player(board)
    return copy_b

def winner(board):
    """
    Returns the winner of the game, if there is one. One can win the game with three of
    their moves in a row horizontally, vertically, or diagonally.
    """

    # horizontal winner
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == O:
                return O
            if board[row][0] == X:
                return X

    # vertical winner
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == O:
                return O
            if board[0][col] == X:
                return X

    # diagonal winner 2 possible diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == O:
            return O
        if board[0][0] == X:
            return X

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == O:
            return O
        if board[0][2] == X:
            return X

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise (not over or a tie).
    """

    if winner(board) == O or winner(board) == X:
        return True

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False   # game still ongoing
    return True    # a tie

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == O:
            return -1
        if winner(board) == X:
            return 1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    turn = player(board)

    # O plays min, X plays max
    if turn == O:
        score, move = minValue(board)
        return move
    elif turn == X:
        score, move = maxValue(board)
        return move

def maxValue(board):
    """
    Returns the maximum score of the possible outcomes, hence the
    maximazing (-> X) player's turn.
    """

    if terminal(board):
        return utility(board), None

    max = float('-inf')
    move = None    # initial move
    for action in actions(board):
        score, act = minValue(result(board, action))
        if score > max:
            max = score
            move = action
    return max, move

def minValue(board):
    """
    Returns the minimum score of the possible outcomes, hence the
    minimazing (-> O) player's turn.
    """

    if terminal(board):
        return utility(board), None

    min = float('inf')
    move = None   # initial move
    for action in actions(board):
        score, act = maxValue(result(board, action))
        if score < min:
            min = score
            move = action
    return min, move
