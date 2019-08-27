def utility(board, p):
    score, i , j =  0, 0, 0
    if p == 1:
        for i in range(0, 19):
            for j in range(0, 19):
                score += getMaxScore(board, i, j)
        return score
    else:
        for i in range(0, 19):
            for j in range(0, 19):
                score += getMinScore(board, i, j)
        return score

def getMinScore(board, i, j):
    score, d, a, w, x, y = 0, 0, 0, 0, 0, 0
    if board[i][j] == 1:
        for x in range(max(j-2, 0), min(j+3, 19)):
            if board[i][j] == board[i][x]:
                d += 1
            else:
                if board[i][x] == 2 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d = 0
                        elif board[i][x-d-1] == 0:
                            d -= 1
                elif board[i][x] == 0 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d -= 1
                        elif board[i][x-d-1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score -= 40*a^2
        else:
            score -= 2*a
        d, a = 0, 0
        for y in range(max(i-2, 0), min(i+3, 19)):
            if board[i][j] == board[y][j]:
                d += 1
            else:
                if board[y][j] == 2 and d != 0:
                    if x-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d = 0
                        elif board[y-d-1][j] == 0:
                            d -= 1
                elif board[i][x] == 0 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d -= 1
                        elif board[y-d-1][j] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score -= 40 * a ^ 2
        else:
            score -= 2 * a
        d, a = 0, 0
        x = max(j-2, 0)
        y = max(i-2, 0)
        w = min(j-x, i-y)
        y = i - w
        for x in range(j-w, min(j+3, 19)):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 2 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 2:
                            d = 0
                        elif board[y-d-1][x-d-1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 2:
                            d -= 1
                        elif board[y-d-1][x-d-1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score -= 40 * a ^ 2
        else:
            score -= 2 * a
        d, a = 0, 0
        y = max(i - 2, 0)
        x = min(j + 2, 18)
        w = min(i - y, x - j)
        y = i - w
        x = j + w
        while x >= max(j-2, 0):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 2 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 2:
                            d = 0
                        elif board[y-d-1][x+d+1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 2:
                            d -= 1
                        elif board[y-d-1][x+d+1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
            x -= 1
        a = max(a, d)
        if a >= 3:
            score -= 40 * a ^ 2
        else:
            score -= 2 * a

    if board[i][j] == 2:
        for x in range(max(j-2, 0), min(j+3, 19)):
            if board[i][j] == board[i][x]:
                d += 1
            else:
                if board[i][x] == 1 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 1:
                            d = 0
                        elif board[i][x-d-1] == 0:
                            d -= 1
                elif board[i][x] == 0 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d += 1
                        elif board[i][x-d-1] == 1:
                            d -= 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score += 2*a^2
        else:
            score += 2*a
        d, a = 0, 0
        for y in range(max(i-2, 0), min(i+3, 19)):
            if board[i][j] == board[y][j]:
                d += 1
            else:
                if board[y][j] == 1 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 1:
                            d = 0
                        elif board[y-d-1][j] == 0:
                            d -= 1
                elif board[y][j] == 0 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d -= 1
                        elif board[y-d-1][j] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score += 2 * a ^ 2
        else:
            score += 2 * a
        d, a = 0, 0
        x = max(j-2, 0)
        y = max(i-2, 0)
        w = min(j-x, i-y)
        y = i - w
        for x in range(j-w, min(j+3, 19)):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 1 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 1:
                            d = 0
                        elif board[y-d-1][x-d-1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 1:
                            d -= 1
                        elif board[y-d-1][x-d-1] == 2:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score += 2 * a ^ 2
        else:
            score += 2 * a
        d, a = 0, 0
        y = max(i - 2, 0)
        x = min(j + 2, 18)
        w = min(i - y, x - j)
        y = i - w
        for x in range(max(j-2, 0), j + w + 1):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 1 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 1:
                            d = 0
                        elif board[y-d-1][x+d+1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 1:
                            d -= 1
                        elif board[y-d-1][x+d+1] == 2:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score += 2 * a ^ 2
        else:
            score += 2 * a
    return score


def getMaxScore(board, i, j):
    score, d, a, w, x, y = 0, 0, 0, 0, 0, 0
    if board[i][j] == 1:
        for x in range(max(j-2, 0), min(j+3, 19)):
            if board[i][j] == board[i][x]:
                d += 1
            else:
                if board[i][x] == 2 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d = 0
                        elif board[i][x-d-1] == 0:
                            d -= 1
                elif board[i][x] == 0 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d -= 1
                        elif board[i][x-d-1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score -= 2*a^2
        else:
            score -= 2*a
        d, a = 0, 0
        for y in range(max(i-2, 0), min(i+3, 19)):
            if board[i][j] == board[y][j]:
                d += 1
            else:
                if board[y][j] == 2 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d = 0
                        elif board[y-d-1][j] == 0:
                            d -= 1
                elif board[y][j] == 0 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d -= 1
                        elif board[y-d-1][j] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score -= 2 * a ^ 2
        else:
            score -= 2 * a
        d, a = 0, 0
        x = max(j-2, 0)
        y = max(i-2, 0)
        w = min(j-x, i-y)
        y = i - w
        for x in range(j-w, min(j+3, 19)):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 2 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 2:
                            d = 0
                        elif board[y-d-1][x-d-1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 2:
                            d -= 1
                        elif board[y-d-1][x-d-1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score -= 2 * a ^ 2
        else:
            score -= 2 * a
        d, a = 0, 0
        y = max(i - 2, 0)
        x = min(j + 2, 18)
        w = min(i - y, x - j)
        y = i - w
        for x in range(max(j-2, 0), j + w + 1):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 2 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 2:
                            d = 0
                        elif board[y-d-1][x+d+1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 2:
                            d -= 1
                        elif board[y-d-1][x+d+1] == 1:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score -= 2 * a ^ 2
        else:
            score -= 2 * a

    if board[i][j] == 2:
        for x in range(max(j-2, 0), min(j+3, 19)):
            if board[i][j] == board[i][x]:
                d += 1
            else:
                if board[i][x] == 1 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 1:
                            d = 0
                        elif board[i][x-d-1] == 0:
                            d -= 1
                elif board[i][x] == 0 and d != 0:
                    if x-d-1 >= 0:
                        if board[i][x-d-1] == 2:
                            d += 1
                        elif board[i][x-d-1] == 1:
                            d -= 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score += 40*a^2
        else:
            score += 2*a
        d, a = 0, 0
        for y in range(max(i-2, 0), min(i+3, 19)):
            if board[i][j] == board[y][j]:
                d += 1
            else:
                if board[y][j] == 1 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 1:
                            d = 0
                        elif board[y-d-1][j] == 0:
                            d -= 1
                elif board[y][j] == 0 and d != 0:
                    if y-d-1 >= 0:
                        if board[y-d-1][j] == 2:
                            d -= 1
                        elif board[y-d-1][j] == 1:
                            d += 1
                a = max(a, d)
                d = 0
        a = max(a, d)
        if a >= 3:
            score += 40 * a ^ 2
        else:
            score += 2 * a
        d, a = 0, 0
        x = max(j-2, 0)
        y = max(i-2, 0)
        w = min(j-x, i-y)
        y = i - w
        for x in range(j-w, min(j+3, 19)):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 1 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 1:
                            d = 0
                        elif board[y-d-1][x-d-1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x-d-1 >= 0:
                        if board[y-d-1][x-d-1] == 1:
                            d -= 1
                        elif board[y-d-1][x-d-1] == 2:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score += 40 * a ^ 2
        else:
            score += 2 * a
        d, a = 0, 0
        y = max(i - 2, 0)
        x = min(j + 2, 18)
        w = min(i - y, x - j)
        y = i - w
        for x in range(max(j-2, 0), j + w + 1):
            if board[i][j] == board[y][x]:
                d += 1
            else:
                if board[y][x] == 1 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 1:
                            d = 0
                        elif board[y-d-1][x+d+1] == 0:
                            d -= 1
                elif board[y][x] == 0 and d != 0:
                    if y-d-1 >= 0 and x+d+1 <= 18:
                        if board[y-d-1][x+d+1] == 1:
                            d -= 1
                        elif board[y-d-1][x+d+1] == 2:
                            d += 1
                a = max(a, d)
                d = 0
            y += 1
            if y > 18:
                break
        a = max(a, d)
        if a >= 3:
            score += 40 * a ^ 2
        else:
            score += 2 * a
    return score