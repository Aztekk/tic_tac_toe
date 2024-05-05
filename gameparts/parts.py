class Board:
    """Класс, который описывает игровое поле"""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player: str) -> bool:
        """Check if player win

        Args:
            player (str): 'X' or 'Y' - player label

        Returns:
            bool: win or not
        """
        # Check vertical or horizontal win
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or all(
                [self.board[j][i] == player for j in range(3)]
            ):
                return True
        # Check diagonal win
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or self.board[0][2]
            == self.board[1][1]
            == self.board[2][0]
            == player
        ):
            return True

        return False

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
