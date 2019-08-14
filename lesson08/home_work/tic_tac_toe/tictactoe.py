import re
from prompter import yesno


class Board:
    """
        constructor for a class Board:
        length - side length of square field
        winning_line - character sequence for victory
        turn_pattern - user input pattern
        board - filling the game field with a symbol
    """
    def __init__(self, length=3, winning_line=3):
        self.len = length
        self.turn_pattern = r'^\d?\d \d?\d$'
        self.board = (' ' * self.len + '\n') * self.len
        self.winning_line = winning_line

    """
        override string method to print the game field 
    """
    def __str__(self):
        result = '   '
        for i in range(self.len):
            result += '{:>3}'.format(str(i+1))
        result += '\n'
        for i in range(self.len):
            result += '{:>3}'.format(str(i+1))
            for j in range(self.len):
                result += '{:>3}'.format(self.board[i*(self.len+1)+j])
            result += '\n'

        return result

    """
        the method determines the possibility of the player’s move. changes "*" to the player's symbol on the playing
        field
    """
    def make_turn(self, turn, point):
        if re.match(self.turn_pattern, turn):
            a, b = turn.split(' ')
            a = int(a)
            b = int(b)
            tmp = list(self.board)
            if a > self.len or b > self.len or b == None:
                print("Ход невозможен")
                return False
            elif tmp[(a-1)*(self.len+1) + (b-1)] != ' ':
                print("Ход невозможен")
                return False
            tmp[(a-1)*(self.len+1) + (b-1)] = point
            self.board = "".join(tmp)
            return True
        else:
            return False

    """
        helper method. return symbol by coordinates
    """
    def _get_char_at(self, a, b):
        return self.board[a*(self.len+1) + b]

    """
        method checks victory
    """
    def is_win(self, char):
        if self._get_max_line(char) == self.winning_line:
            print(self)
            return True
        return False

    """
        method checks free calls
    """
    def free_calls(self):
        tmp = list(self.board)
        for i in tmp:
            if i == ' ':
                return True
                break
        print(self)
        return False

    """
        helper method. a and b is coordinate, char is symbol, mod_a and mod_b is direction line    
    """
    def _get_line(self, a, b, char, mod_a, mod_b):
        result_len = 0
        for i in range(self.winning_line):
            if (a + i*mod_a) < self.len \
                    and (a + i*mod_a) > -1 \
                    and (b + i*mod_b) < self.len \
                    and (b + i*mod_b) > -1 \
                    and self._get_char_at(a + i*mod_a, b + i*mod_b) == char:
                result_len += 1
            else:
                break
        return result_len

    """
        method determines the length of consecutive symbols
    """
    def _get_max_line(self, char):
        max_len = 0
        current_len = 0
        for i in range(self.len):
            for j in range(self.len):
                if self._get_char_at(i, j) == char:
                    current_len = self._get_line(i, j, char, 0, 1)
                    if current_len > max_len:
                        max_len = current_len
                    current_len = self._get_line(i, j, char, 1, 0)
                    if current_len > max_len:
                        max_len = current_len
                    current_len = self._get_line(i, j, char, 1, 1)
                    if current_len > max_len:
                        max_len = current_len
                    current_len = self._get_line(i, j, char, 1, -1)
                    if current_len > max_len:
                        max_len = current_len
        return max_len

class Game:
    """
        helper method. print rules of the game
    """
    @staticmethod
    def print_rules():
        print(
            "Ход задаётся 2мя координатами через пробел от 1 до 3,\n"
            "первое число номер строки, второе - номер столбца\n")

    """
        initial method of the program
    """
    @staticmethod
    def start_game():
        answer_begin = yesno("Начать игру?")
        if answer_begin:
            answer = input("Выберите режим игры:\n"
                           "Режим    х       о\n"
                           "1   Человек Человек\n"
                           "2   Человек    ИИ\n")
            if answer == '1':
                game = Game(HumanPlayer('Игрок 1'), HumanPlayer('Игрок 2'))
            elif answer == '2':
                game = Game(HumanPlayer('Игрок'), AIPlayer('Компьютер'))
            game._play()

    """
        constructor for a class Game:
        board - object of class Board
        player1 and player2 - object of classes HumanePlayer and AIPlayer
    """
    def __init__(self, player1, player2):
        Game.print_rules()
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    """
        round game
    """
    def _play(self):
        while True:
            if not self._make_turn(self.player1, 'x'):
                break
            if not self._make_turn(self.player2, 'o'):
                break

    """
        binding method. from Board class object 
    """
    def _make_turn(self, player, char):
        turn = player.make_turn(self.board, char)
        if turn:
            if not self.board.make_turn(turn, char):
                self._make_turn(player, char)
            if self.board.is_win(char):
                print(f'{player.name} победил!')
                return False
            if not self.board.free_calls():
                print('Ничья!')
                return False
        else:
            print(f'{player.name} прервал игру.')
            return False
        return True


class Player:
    def make_turn(self, board, char):
        pass

    def __init__(self, name):
        self.name = name


class HumanPlayer(Player):
    def make_turn(self, board, char):
        print(board)
        turn = input(f'{self.name}, введите Ваш ход (exit чтобы закончить):\n')
        if turn == 'exit':
            return False
        else:
            return turn


class AIPlayer(Player):
    def make_turn(self, board, char):
        print(board)
        list_turns = []
        for i in range(board.len):
            for j in range(board.len):
                list_turns.append((i, j, self._get_weight(board, i, j, char, 'x' if char == 'o' else 'o')))

        best_turn = (-1, -1, 0)
        for i in list_turns:
            if i[2] > best_turn[2]:
                best_turn = i
        return str(best_turn[0] + 1) + ' ' + str(best_turn[1] + 1)

    def _get_weight(self, board, a, b, char, char2):
        if board._get_char_at(a, b) != ' ':
            return 0
        else:
            return self._wl(board, a, b, char, char2, 0, 1) \
                   + self._wl(board, a, b, char, char2, 0, -1) \
                   + self._wl(board, a, b, char, char2, 1, 0) \
                   + self._wl(board, a, b, char, char2, 1, 1) \
                   + self._wl(board, a, b, char, char2, 1, -1) \
                   + self._wl(board, a, b, char, char2, -1, 0) \
                   + self._wl(board, a, b, char, char2, -1, 1) \
                   + self._wl(board, a, b, char, char2, -1, -1)

    def _wl(self, board, a, b, char, char2, mod_a, mod_b):
        result = 0.1
        last_char = ''
        for i in range(1, 3):
            if a + i * mod_a >= board.len or a + i * mod_a < 0 or b + i * mod_b >= board.len or b + i * mod_b < 0:
                result = result / 2
                break
            if board._get_char_at(a + i * mod_a, b + i * mod_b) == ' ':
                result += 0.1 / i
                last_char = ' '
            elif board._get_char_at(a + i * mod_a, b + i * mod_b) == char:
                if last_char == char or last_char == '':
                    result += 0.2 * i ** 2
                    if i == 3:
                        result += 100
                else:
                    break
                last_char = char
            elif board._get_char_at(a + i * mod_a, b + i * mod_b) == char2:
                if last_char == char2 or last_char == '':
                    result += 0.1 * i ** 2
                    if i == 3:
                        result += 50
                else:
                    break
                last_char = char2
        return result


Game.start_game()
