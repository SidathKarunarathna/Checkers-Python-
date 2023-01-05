import pygame
from .constants import RED,WHITE,BLUE,SQUARE_SIZE,BLACK,WIDTH,HEIGHT
from .board import Board


class Game:
    def __init__(self,win):
        self._init()
        self.win=win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.winner()
        pygame.display.update()
    
    def _init(self):
        self.selected=None
        self.board=Board()
        self.turn =RED
        self.valid_moves={}

    def reset(self):
        self._init()

    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected=None
                self.select(row,col)
        
        piece=self.board.get_piece(row,col)
        if piece!=0 and piece.color==self.turn:
            self.selected=piece
            self.valid_moves=self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece ==0 and (row,col) in self.valid_moves:
            self.board.move(self.selected,row,col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self,moves):
        for move in moves:
             row,col=move
             pygame.draw.circle(self.win,BLUE,(col*SQUARE_SIZE+SQUARE_SIZE//2,row*SQUARE_SIZE+SQUARE_SIZE//2),15)
    
    def change_turn(self):
        self.valid_moves={}
        if self.turn==RED:
            self.turn=WHITE
        else:
            self.turn=RED
    
    def winner(self):
        winner= self.board.winner()
        if winner!=None:
            if winner ==RED:
                winnertext="BLACK WINS"
            else:
                winnertext="WHITE WINS"

            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(winnertext, True, WHITE, BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH// 2, HEIGHT // 2)
            self.win.blit(text, textRect)
    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        self.board =board
        self.change_turn()
        

