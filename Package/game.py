import pygame
from .constants import RED,WHITE,BLUE,SQUARE_SIZE,BLACK,WIDTH,HEIGHT,GREY,DARK
from .board import Board


class Game:
    def __init__(self,win):
        self._init()
        self.win=win
    
    def update(self):
        self.board.draw(self.win)
        self.score_board()
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
                winnertext="PLAYER WINS"
            else:
                winnertext="COMPUTER WINS"

            font = pygame.font.Font('freesansbold.ttf', 72)
            text = font.render(winnertext, True, WHITE, BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH// 2, HEIGHT // 2)
            self.win.blit(text, textRect)
    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        pygame.time.delay(1000)
        self.board =board
        self.change_turn()
    
    def score_board(self):
        pygame.draw.rect(self.win,GREY,(WIDTH,0,300,HEIGHT))
        font = pygame.font.Font('freesansbold.ttf', 32)
        player = font.render("PLAYER", True, DARK, GREY)
        playerRect=player.get_rect()
        playerRect.center=((WIDTH+300+WIDTH)//2,748)
        self.win.blit(player,playerRect)
        computer = font.render("COMPUTER", True, DARK, GREY)
        computerRect=computer.get_rect()
        computerRect.center= ((WIDTH+300+WIDTH)//2,52)
        self.win.blit(computer,computerRect)



        

