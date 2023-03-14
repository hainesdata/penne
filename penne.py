import numpy as np

class Board:
    def __init__(self, n):
        self.grid = np.zeros((n,n))
    
    def add_stone(self, stone):
        self.grid[stone.x][stone.y] = stone

    def remove_stones(self, stones):
        self.grid[stones[0].x][stones[0].y] = None
        self.grid[stones[1].x][stones[1].y] = None
        self.player.add_capture()

class Stone:
    def __init__(self, player, x, y):
        self.player = Player
        self.x = x
        self.y = y

class Player:
    def __init__(self, id, captures):
        self.id = id
        self.captures = captures

    def add_capture(self):
        self.captures += 1

class Game:
    def __init__(self, moves, board_size):
        self.moves = moves
        self.board_size = board_size

    def scan_array(capture_pattern, stone_seq, size):
        selected_ids = ''
        selected_stones = []
        is_match = False
        for stone in stone_seq:
            if len(selected_ids) == size
                selected_ids.pop(selected_ids[0])
                selected_stones.pop(selected_stones[0])
            selected_ids + stone.player.id
            selected_stones.append(stone)
            if capture_pattern in selected_ids:
                is_match = True
                break
        return is_match, selected_stones

    def check(stone_seq, last_player, validate='capture'):
        if last_player.id == 'X':
            if validate == 'capture':
                capture_pattern = 'XOOX'
            elif validate == 'win':
                capture_pattern = 'XXXXX'
            else:
                'Invalid validation type specified'
        elif last_player.id == 'O':
            if validate == 'capture':
                capture_pattern = 'OXXO'
            elif validate == 'win':
                capture_pattern = 'OOOOO'
        else:
            raise ValueError('Invalid PlayerID encountered, cannot retrieve player of last move')

        if validate == 'capture':
            size = 4
        elif validate == 'win':
            size = 5
        else:
            raise ValueError('Invalid capture type specified')

        detected, selected_stones = scan_array(capture_pattern, stone_seq, size)

        if detected:
            if validate == 'capture':
                board.remove_stones(stone_seq[selected_stones[1], selected_stones[2]])
                return 'NA'
            if validate == 'win':
                return last_player.id
        return 'NA'
                
    def detect(self, board, last_ player, validate='capture'):
        for j in board.grid.T:
            status = check(j, last_player, validate)
            if status != 'NA':
                return status

        for i in board.grid:
            status = check(i, last_player, validate)
            if status != 'NA':
                return status

        diagonals = []
        for offset in range(-board.grid.shape[0]+1, board.grid.shape[1]):
            diagonal = np.diagonal(board.grid, offset=offset)
            if diagonal.size > 0:
                diagonals.append(diagonal)
        for ij in diagonals:
            status = check(ij, last_player, validate)
            if status != 'NA':
                return status
        
        diagonals = []
        for offset in range(-board.grid.shape[0]+1, board.grid.shape[1]):
            diagonal = np.diagonal(np.fliplr(board.grid, offset=offset))
            if diagonal.size > 0:
                diagonals.append(diagonal)
        for ji in diagonals:
            status = check(ji, last_player, validate)
            if status != 'NA':
                return status

        return status
            
    def analyze(self, board, last_player):
        self.detect(board, last_player, 'capture')
        return self.detect(board, last_player, 'win')
        
    def play(self):
        board = Board(self.board_size)
        self.player_x = Player('X', 0)
        self.player_o = Player('O', 0)
        for move in self.moves:
            if self.moves.index(move)%2 == 0:
                stone = Stone(self.player_x, move[0], move[1])
            else:
                stone = Stone(self.player_o, move[0], move[1])
            board.add_stone(stone)
            status = self.analyze(board, stone.player)
            if status == 'X' or status == 'O' or status == 'T':
                return status
            else:
                continue
        raise ValueError('All moves exhausted, but no outcome was returned')
        
def main():
    moves = [X_i, Y_i]
    game = Game(moves, 19)

if __name__ == "__main__":
    main()
