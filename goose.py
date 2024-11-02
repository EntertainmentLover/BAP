import random

class ChessPiece:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return ' ' 
    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Этот метод должен быть реализован подклассами.")

class Pawn(ChessPiece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'
    def is_valid_move(self, start, end, board):
        direction = -1 if self.color == 'white' else 1
        start_row, start_col = start
        end_row, end_col = end

        if end_col == start_col:
            if board[end_row][end_col] == '.':
                if (end_row - start_row) == direction:
                    return True
                if (end_row - start_row) == 2 * direction and start_row in [1, 6]:
                    return board[start_row + direction][start_col] == '.'
        elif abs(end_col - start_col) == 1 and (end_row - start_row) == direction:
            if board[end_row][end_col] != '.':
                return True
        return False

class Rook(ChessPiece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'
    def is_valid_move(self, start, end, board):
        return self.validate_line_move(start, end, board)
    def validate_line_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != '.':
                    return False
            return True
        elif start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != '.':
                    return False
            return True
        return False

class Knight(ChessPiece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'
    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        return (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]

class Bishop(ChessPiece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'
    def is_valid_move(self, start, end, board):
        return self.validate_diagonal_move(start, end, board)
    def validate_diagonal_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        if abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while (row, col) != (end_row, end_col):
                if board[row][col] != '.':
                    return False
                row += row_step
                col += col_step
            return True
        return False

class Queen(ChessPiece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'
    def is_valid_move(self, start, end, board):
        return Rook(self.color).validate_line_move(start, end, board) or Bishop(self.color).validate_diagonal_move(start, end, board)

class King(ChessPiece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'
    def is_valid_move(self, start, end, board):
        return max(abs(start[0] - end[0]), abs(start[1] - end[1])) == 1

class Goose(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return 'G' if self.color == 'white' else 'g'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2  
            if board[mid_row][mid_col] != '.':
                return False        
            return True
        return False

    def move(self, start, end, board):
        board[start[0]][start[1]] = '.'
        board[end[0]][end[1]] = self  
        target_piece = board[end[0]][end[1]]
        if isinstance(target_piece, ChessPiece) and target_piece.color != self.color:
            dice_roll = random.randint(1, 6)
            print(f"Гусь бросил кубик: {dice_roll}")
            if dice_roll % 2 == 0:
                self.eat_piece(end, board)
        else:
            print("На конечной позиции нет фигуры для съедения!")

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'
        self.move_history = []
        self.undo_stack = []

    def create_board(self):
        board = [['.' for _ in range(8)] for _ in range(8)]
        board[0] = [Rook('black'), 
                    Knight('black'), 
                    Goose('black'), 
                    Queen('black'), 
                    King('black'), 
                    Bishop('black'), 
                    Knight('black'), 
                    Rook('black')]
        board[1] = [Pawn('black')] * 8
        board[6] = [Pawn('white')] * 8
        board[7] = [Rook('white'), 
                    Knight('white'), 
                    Goose('white'), 
                    Queen('white'), 
                    King('white'), 
                    Bishop('white'), 
                    Knight('white'), 
                    Rook('white')]
        return board

    def display_board(self):
        print("   a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            print(f"{8 - i}|", end=' ')
            for cell in row:
                print(str(cell), end=' ')
            print("|")
        print(" +-----------------+\n")

    def move_piece(self, start, end):
        start_row, start_col = start
        piece = self.board[start_row][start_col]
        if isinstance(piece, ChessPiece) and piece.color == self.current_turn:
            if isinstance(piece, Goose):
                piece.move(start, end, self.board)
                self.move_history.append(f"{piece} from {start} to {end}")
                self.undo_stack.append((start, end, piece))
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                if piece.is_valid_move(start, end, self.board):
                    self.undo_stack.append((start, end, piece))
                    self.move_history.append(f"{piece} from {start} to {end}")
                    self.board[end[0]][end[1]] = piece
                    self.board[start[0]][start[1]] = '.'      
                    if isinstance(piece, King):
                        if piece.color == 'white':
                            self.white_king_pos = end
                        else:
                            self.black_king_pos = end
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
                else:
                    print("Неверный ход!")
        else:
            print("Нет фигуры в стартовой позиции или неверный игрок.")

    def is_valid_move(self, piece, start, end):
        if piece == '.':
            print("Нет фигуры в стартовой позиции.")
            return False
        if (self.current_turn == 'white' and piece.color == 'black') or (self.current_turn == 'black' and piece.color == 'white'):
            print("Неверный игрок для этой фигуры.")
            return False
        if not piece.is_valid_move(start, end, self.board):
            print(f"Неверный ход для {piece} с {start} на {end}.")
            return False
        if self.is_king_in_check_after_move(start, end, piece):
            print("Ход приводит к шаху королю!")
            return False
        return True
    
    def undo_move(self):
        if self.undo_stack:
            start, end, piece = self.undo_stack.pop()
            self.board[start[0]][start[1]] = piece
            self.board[end[0]][end[1]] = '.'  
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            print(f"Ход отменен: {piece.__class__.__name__} с {end} на {start}")
        else:
            print("Нет ходов для отмены.")

    def is_king_in_check(self, king_pos, king_color):
        enemy_color = 'black' if king_color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, ChessPiece) and piece.color == enemy_color:
                    if piece.is_valid_move((row, col), king_pos, self.board):
                        return True
        return False

    def is_game_over(self):
        if self.is_king_in_check(self.get_king_position('white'), 'white'):
            if not self.has_legal_moves('white'):
                return "checkmate"
            return "check"
        if self.is_king_in_check(self.get_king_position('black'), 'black'):
            if not self.has_legal_moves('black'):
                return "checkmate"
            return "check"
        if not self.has_legal_moves('white') and not self.has_legal_moves('black'):
            return "draw"
        return "ongoing"

    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return (row, col)
        return None

    def has_legal_moves(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, ChessPiece) and piece.color == color:
                    for target_row in range(8):
                        for target_col in range(8):
                            if piece.is_valid_move((row, col), (target_row, target_col), self.board):
                                return True
        return False

def parse_position(pos):
    if len(pos) != 2 or pos[0] not in "abcdefgh" or pos[1] not in "12345678":
        raise ValueError("Неверный формат позиции. Используйте 'a1' - 'h8'.")
    return (8 - int(pos[1]), ord(pos[0]) - ord('a'))

def main():
    game = ChessBoard()
    game.display_board()

    while True:
        print(f"Ход: {game.current_turn}")
        action = input("Введите 'move' для хода, 'undo' для отмены, 'exit' для выхода: ").strip().lower()
        if action == 'move':
            try:
                start = parse_position(input("Введите начальную позицию (например, 'e2'): "))
                end = parse_position(input("Введите конечную позицию (например, 'e4'): "))
                game.move_piece(start, end)
                game.display_board()
                game_status = game.is_game_over()
                if game_status != "ongoing":
                    print(f"Игра завершена: {game_status}")
                    break
            except ValueError as e:
                print(e)
        elif action == 'undo':
            game.undo_move()
            game.display_board()
        elif action == 'exit':
            print("Игра завершена.")
            break

if __name__ == "__main__":
    main()
