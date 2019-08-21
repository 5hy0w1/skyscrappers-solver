import time


class Solution:
    def __init__(self, clues):
        self.size = int(len(clues) / 4)
        self.top_constrait = clues[:self.size]
        self.right_constrait = clues[self.size: self.size * 2]
        self.bottom_constrait = clues[self.size * 2:self.size * 3:]
        self.left_constrait = clues[self.size * 3:]
        self.left_constrait.reverse()
        self.bottom_constrait.reverse()
        self.row_empty_fields = [self.size for _ in range(self.size)]
        self.col_empty_fields = [self.size for _ in range(self.size)]
        self._init_board()
        self._init_possibles()

    def _get_impossibles(self, constrait):
        if constrait >= 2 and constrait < self.size:
            constrait = [self.size - i for i in range(constrait - 1)]
            return constrait
        return []

    def _clue_constrait_horisontal(self, side):  # side == 0 -> left, side == -1 -> right
        for index, const in enumerate(self.left_constrait if not side else self.right_constrait):
            if const == 1:
                self.possibles[index][side] = [self.size]
            elif const == self.size:
                if not side:
                    self.possibles[index] = [[i + 1] for i in range(self.size)]
                else:
                    self.possibles[index] = [[i + 1] for i in reversed(range(0, self.size))]
            elif const != 0:
                imp = self._get_impossibles(const)
                if not side:
                    for i in range(len(imp)):
                        if type(self.possibles[index][i]) == list:
                            self.possibles[index][i] = list(set(self.possibles[index][i]) - set(imp))
                        imp.pop(-1)
                else:
                    for i in range(self.size - 1, self.size - len(imp) - 1, -1):
                        if type(self.possibles[index][i]) == list:
                            self.possibles[index][i] = list(set(self.possibles[index][i]) - set(imp))
                        imp.pop(-1)

    def _clue_constrait_verical(self, side):  # side == 0 -> top, side == -1 -> bottom
        constraits = self.bottom_constrait if side else self.top_constrait
        for index, const in enumerate(constraits):
            if const == 1:
                if side:
                    self.possibles[side][index] = [self.size]
            elif const == 6:
                if not side:
                    for i in range(self.size):
                        self.possibles[i][index] = [i + 1]
                else:
                    for i in range(self.size):
                        self.possibles[self.size - 1 - i][index] = [i + 1]
            elif const != 0:
                imp = self._get_impossibles(const)
                if not side:
                    for i in range(len(imp)):
                        if type(self.possibles[i][index]) == list:
                            self.possibles[i][index] = list(set(self.possibles[i][index]) - set(imp))
                            imp.pop(-1)
                else:
                    for i in range(self.size - 1, self.size - len(imp) - 1, -1):
                        if type(self.possibles[i][index]) == list:
                            self.possibles[i][index] = list(set(self.possibles[i][index]) - set(imp))
                            imp.pop(-1)

    def _init_board(self):
        self.board = [[0 for j in range(self.size)] for i in range(self.size)]

    def _init_possibles(self):
        self.possibles = [[[i for i in range(1, self.size + 1)] for i in range(self.size)] for i in range(self.size)]

    def _count_visible(self, line):
        res = 0
        curr = 0
        for i in line:
            if i > curr:
                res += 1
                curr = i
        return res

    def _check_unique(self, i, j, val):
        for x in range(self.size):
            if val == self.board[i][x]:
                return False
        for x in range(self.size):
            if val == self.board[x][j]:
                return False
        return True

    def _find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def _all_filled(self, line):
        for i in line:
            if i == 0:
                return False
        return True

    def valid_value(self, i, j, val):
        unique = self._check_unique(i, j, val)
        self.board[i][j] = val
        if all((
            unique,
            self.valid_row(i),
            self.valid_col(j)
        )):
            return True
        else:
            self.board[i][j] = 0
            return False

    def valid_row(self, i):
        if self._all_filled(self.board[i]):
            return all((
                self.left_constrait[i] == self._count_visible(self.board[i]) or self.left_constrait[i] == 0,
                self.right_constrait[i] == self._count_visible(reversed(self.board[i])) or self.right_constrait[i] == 0
            ))
        else:
            return True

    def valid_col(self, j):
        if self._all_filled(self._column(j)):
            return all((
                self.top_constrait[j] == self._count_visible(self._column(j)) or self.top_constrait[j] == 0,
                self.bottom_constrait[j] == self._count_visible(self._column(j, True)) or self.bottom_constrait[j] == 0
            ))
        else:
            return True

    def set_value(self, i, j, val):
        self.board[i][j] = val
        self.col_empty_fields[j] -= 1
        self.row_empty_fields[i] -= 1

    def _column(self, col, r=False):
        if not r:
            for i in range(self.size):
                yield self.board[i][col]
        else:
            for i in reversed(range(self.size)):
                yield self.board[i][col]

    def solve(self):
        global tries
        if tries % 40000 == 0:
            print(f'try #{tries}')
        find = self._find_empty()
        if not find:
            return True
        row, col = find
        for i in self.possibles[row][col]:
            if self.valid_value(row, col, i):
                self.board[row][col] = i
                tries += 1
                if self.solve():
                    return True
                self.board[row][col] = 0
            # self.possibles[row][col].remove(i)
        return False

    def optimize(self):
        self._clue_constrait_verical(0)
        self._clue_constrait_verical(-1)
        self._clue_constrait_horisontal(0)
        self._clue_constrait_horisontal(-1)

    def print_board(self):
        print('  ', end='')
        for i in self.top_constrait:
            print(' ', i, end='')
        print('\n  ', '-' * self.size * 3)
        for i in range(self.size):
            for j in range(self.size):
                if j == 0:
                    print(self.left_constrait[i], '|', self.board[i][j], end='')
                elif j == self.size - 1:
                    print(' ', self.board[i][j], '|', self.right_constrait[i], end='')
                else:
                    print(' ', self.board[i][j], end='')
            print()
        print('  ', '-' * self.size * 3)
        print('  ', end='')
        for i in self.bottom_constrait:
            print(' ', i, end='')
        print()


try:
    tries = 0
    clues = [int(i) for i in input("Введите ограничения по часовой стрелке, начиная с левого верхнего угла:\n")]
    sol = Solution(clues)
    print("Введите уже известные чиисла в формате {строка}{столбец}{число} (123), для прекращения введите \"stop\":\n")
    data = '0'

    while data.isdecimal():
        data = input()
        if data.isdecimal():
            sol.board[int(data[0])][int(data[1])] = int(data[2])
    print("Начальная доска:\n")

    sol.print_board()
    input("Нажмите ENTER, чтобы подтвердить")
    print("\n")
    start = time.time()
    if sol.size > 5:
        print("\n\nВы ввели число большее 5, поиск решения может затянуться\n\n")
    sol.optimize()
    sol.solve()
    end = time.time()
    print('-' * (sol.size * 3), '\n')
    sol.print_board()
    print(f"Решено за {round(end-start,2)} секунд")
    print(f"Количество попыток: {tries}")
    input("Нажмите ENTER, чтобы выйти")
except KeyboardInterrupt:
    print("\nИсполнение прекращено пользователем")
    exit()
