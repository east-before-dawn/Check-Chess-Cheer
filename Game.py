from tkinter import messagebox
from ChessBoard import *
from ChessView import ChessView
import time

"""
把逻辑坐标转换成物理坐标
"""
def real_position(x):
    return x*55 + 30          # 棋盘方格为55X55大小，棋盘外围大约为30

"""
把物理坐标转换成逻辑坐标
"""
def logic_position(x):
    return round((x-30)/55)        # 四舍五入

class Game:
    mode = 0  # 游戏模式，0为 人 vs AI， 1为 AI vs AI， 默认为0
    def __init__(self, mode = 0, human_color = "red"):
        self.mode = mode
        if mode == 0:
            self.human_color = human_color
            self.AI_color = "black" if human_color == "red" else "red"
            self.cur_player = "human"           # 当前棋盘操纵者

        self.chessboard = ChessBoard()
        self.chessview = ChessView(game=self, chessboard=self.chessboard)
        self.chessview.draw_board()             # 绘制棋盘
        self.chessview.showMsg("check-chess-cheer")


    """
    游戏开始
    """
    def start(self):
        self.chessview.showMsg(self.cur_player + "...")
        self.chessview.start()




    def click(self, event):
        # 如果cur是None，则表示游戏结束
        if self.cur_player == None:
            return
        # 如果是人机，并且cur_player是AI
        if self.mode == 0 and self.cur_player == 'AI':
            return
        # 如果是AI对AI
        if self.mode == 1:
            return
        x = logic_position(event.x)
        y = logic_position(event.y)
        change, done = self.chessboard.select(x, y, self.human_color)
        if change:      # 棋盘发生变化
            self.chessview.draw_board()
            self.chessview.update()
            if done:    # human已经下完棋，先判断是否产生胜负，没有则，轮到AI
                if self.check_end():  # 判断是否结束，判断输赢
                    self.cur_player = None

                else:
                    # AI
                    self.cur_player = "AI"
                    self.chessview.showMsg("AI...")
                    self.chessview.update()
                    self.AI_play()  # AI下棋
                    self.chessview.draw_board()  # 显示棋盘
                    self.chessview.update()
                    if self.check_end():  # 判断是否结束，判断输赢
                        self.cur_player = None


                    else:
                        # AI下完，轮到玩家
                        self.cur_player = "human"
                        self.chessview.showMsg("human...")
                        self.chessview.update()
            return



    def check_end(self):                        # 返回是否已结束
        human_win = False
        AI_win = False
        pieces = self.chessboard.all_pieces
        if self.chessboard.king_ftf():        # 两王面对面时，结束？？？？是吗
            if self.cur_player == "human":
                human_win = True
            else:
                AI_win = True
        else:
            for (x, y) in pieces.keys():
                if pieces[x, y].is_king:
                    if pieces[x, y].color == self.human_color:
                        human_win = True
                    else:
                        AI_win = True

        if not human_win:
            self.chessview.showMsg("check-chess-cheer")
            r = messagebox.showinfo('', '你输了...')
            self.chessview.update()
            return True
        elif not AI_win:
            self.chessview.showMsg("check-chess-cheer")
            r = messagebox.showinfo('', '你赢了！')
            self.chessview.update()
            return True

        return False

    def quit(self):
        self.chessview.quit()

    def AI_play(self):

        for (x,y) in self.chessboard.all_pieces:
            if self.chessboard.all_pieces[x, y].color == self.AI_color:
                all_can_move = self.chessboard.all_pieces[x, y].findAll(self.chessboard)
                if not all_can_move:
                    continue
                self.chessboard.all_pieces[x, y].move(all_can_move[0][0], all_can_move[0][1], self.chessboard)
                return








