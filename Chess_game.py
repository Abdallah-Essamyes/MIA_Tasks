import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Piece images
PIECE_IMAGES = {
    'pawn': 'rook.png',
    'rook': 'rook.png',
    'knight': 'rook.png',
    'bishop': 'rook.png',
    'queen': 'rook.png',
    'king': 'rook.png'
}


class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.image = pygame.image.load(PIECE_IMAGES[name])
        self.rect = self.image.get_rect()

    def get_moves(self, board, x, y):
        moves = []
        if self.name == 'pawn':
            direction = 1 if self.color == 'white' else -1
            moves.append((x, y + direction))
        elif self.name == 'rook':
            for i in range(8):
                moves.append((x, i))
                moves.append((i, y))
        elif self.name == 'knight':
            knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
            for dx, dy in knight_moves:
                moves.append((x + dx, y + dy))
        elif self.name == 'bishop':
            for i in range(1, 8):
                moves.append((x + i, y + i))
                moves.append((x - i, y + i))
                moves.append((x + i, y - i))
                moves.append((x - i, y - i))
        elif self.name == 'queen':
            for i in range(8):
                moves.append((x, i))
                moves.append((i, y))
                moves.append((x + i, y + i))
                moves.append((x - i, y + i))
                moves.append((x + i, y - i))
                moves.append((x - i, y - i))
        elif self.name == 'king':
            king_moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in king_moves:
                moves.append((x + dx, y + dy))
        return moves


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, x, y):
        self.board[x][y] = piece

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None

    def draw(self, screen):
        for y in range(8):
            for x in range(8):
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, WHITE if (x + y) % 2 == 0 else BLACK, rect)
                if self.board[x][y]:
                    screen.blit(self.board[x][y].image, rect)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()

    board = Board()
    board.place_piece(Piece('rook', 'white'), 0, 0)
    board.place_piece(Piece('knight', 'white'), 1, 0)
    board.place_piece(Piece('bishop', 'white'), 2, 0)
    board.place_piece(Piece('queen', 'white'), 3, 0)
    board.place_piece(Piece('king', 'white'), 4, 0)
    for i in range(8):
        board.place_piece(Piece('pawn', 'white'), i, 1)

    board.place_piece(Piece('rook', 'black'), 0, 7)
    board.place_piece(Piece('knight', 'black'), 1, 7)
    board.place_piece(Piece('bishop', 'black'), 2, 7)
    board.place_piece(Piece('queen', 'black'), 3, 7)
    board.place_piece(Piece('king', 'black'), 4, 7)
    for i in range(8):
        board.place_piece(Piece('pawn', 'black'), i, 6)

    running = True
    selected_piece = None
    while running:
        screen.fill(GREEN)
        board.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                if selected_piece:
                    if (x, y) in selected_piece.get_moves(board, selected_piece.rect.x // SQUARE_SIZE,
                                                          selected_piece.rect.y // SQUARE_SIZE):
                        board.move_piece((selected_piece.rect.x // SQUARE_SIZE, selected_piece.rect.y // SQUARE_SIZE),
                                         (x, y))
                    selected_piece = None
                else:
                    piece = board.board[x][y]
                    if piece:
                        selected_piece = piece

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
