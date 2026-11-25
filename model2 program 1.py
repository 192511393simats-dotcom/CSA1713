board = [" "] * 9

def check_win(b, p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    return any(all(b[i] == p for i in w) for w in wins)

def minimax(b, depth, alpha, beta, is_max):
    if check_win(b, "O"):
        return 10 - depth

    if check_win(b, "X"):
        return depth - 10

    if " " not in b:
        return 0

    if is_max:
        best = -1000

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, alpha, beta, False)
                b[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = 1000

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, alpha, beta, True)
                b[i] = " "
                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

def best_move():
    best = -1000
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, -1000, 1000, False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    print("Best move selected by AI:", move + 1)

best_move()
