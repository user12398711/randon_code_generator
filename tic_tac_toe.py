matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_matrix():
    for r in range(3):
        for c in range(3):
            print(" " + str(matrix[r][c]) + " ", end="")
        print()


def check_if_winner():
    from collections import Counter

    # rows
    for r in range(3):
        for k, v in Counter(matrix[r]).items():
            if k in ["X", "O"] and v == 3:
                return k, True

    # columns
    for r in range(3):
        for k, v in Counter([matrix[r][0], matrix[r][1], matrix[r][2]]).items():
            if k in ["X", "O"] and v == 3:
                return k, True

    # diagonals
    for k, v in Counter([matrix[0][0], matrix[1][1], matrix[2][2]]).items():
        if k in ["X", "O"] and v == 3:
            return k, True

    for k, v in Counter([matrix[2][0], matrix[1][1], matrix[0][2]]).items():
        if k in ["X", "O"] and v == 3:
            return k, True

    return None, False


def main():
    while True:
        cmd = str(input("Enter command: ")).strip()

        if cmd == "exit":
            break

        elif cmd == "game":
            symbol = str(input("Enter player symbol[x, o]: ")).strip().upper()
            symbol = symbol if symbol in ["X", "O"] else "X"
            count = 0
            while count < 9:
                cord_x, cord_y = (
                    str(input(f"Enter {symbol} co-ordinate(eg: 1,2): ")).strip().split(",")
                )
                cord_x, cord_y = int(cord_x), int(cord_y)
                if matrix[cord_x][cord_y] not in ["X", "O"]:
                    matrix[cord_x][cord_y] = symbol

                    print_matrix()
                    winner, state = check_if_winner()
                    if state:
                        print("********", winner, "won", "********")
                        break

                    count += 1
                    if symbol == "O":
                        symbol = "X"
                    else:
                        symbol = "O"
        else:
            print("invalid command")


main()
