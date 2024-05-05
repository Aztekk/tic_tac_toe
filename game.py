from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(filepath: str, result: str) -> None:
    with open(filepath, 'a') as f:
        f.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:

            try:
                row = int(input('Строка:'))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                if isinstance(row, str):
                    raise ValueError
                col = int(input('Столбец:'))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError
                if isinstance(row, str):
                    raise ValueError
                if game.board[row][col] != " ":
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Ход должен быть не отрицательным '
                    + f'и меньше {game.field_size}'
                )
                print('Попробуйте ещё раз')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, col, current_player)
        print('Ход сделан!')
        game.display()

        if game.check_win(current_player):
            result = f'Выиграл {current_player}'
            print(result)
            save_result('result.txt', result)
            running = False
        if game.is_board_full():
            result = 'Ничья'
            print(result)
            save_result('result.txt', result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
