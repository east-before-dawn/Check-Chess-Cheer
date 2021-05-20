from pieces.bing import *
from pieces.shuai import *
from pieces.pao import *
from pieces.shi import *
from pieces.xiang import *
from pieces.ma import *
from pieces.che import *

class ChessBoard:
    selected_pieces = None        # 被选中棋子
    all_pieces = dict()          # 棋盘，即棋盘上的棋子及其位置

    def __init__(self):
        ChessBoard.all_pieces[4, 0] = Shuai(4, 0, "red")

        ChessBoard.all_pieces[0, 3] = Bing(0, 3, "red")
        ChessBoard.all_pieces[2, 3] = Bing(2, 3, "red")
        ChessBoard.all_pieces[4, 3] = Bing(4, 3, "red")
        ChessBoard.all_pieces[6, 3] = Bing(6, 3, "red")
        ChessBoard.all_pieces[8, 3] = Bing(8, 3, "red")

        ChessBoard.all_pieces[1, 2] = Pao(1, 2, "red")
        ChessBoard.all_pieces[7, 2] = Pao(7, 2, "red")

        ChessBoard.all_pieces[3, 0] = Shi(3, 0, "red")
        ChessBoard.all_pieces[5, 0] = Shi(5, 0, "red")

        ChessBoard.all_pieces[2, 0] = Xiang(2, 0, "red")
        ChessBoard.all_pieces[6, 0] = Xiang(6, 0, "red")

        ChessBoard.all_pieces[1, 0] = Ma(1, 0, "red")
        ChessBoard.all_pieces[7, 0] = Ma(7, 0, "red")

        ChessBoard.all_pieces[0, 0] = Che(0, 0, "red")
        ChessBoard.all_pieces[8, 0] = Che(8, 0, "red")

        # south area
        ChessBoard.all_pieces[4, 9] = Shuai(4, 9, "black")

        ChessBoard.all_pieces[0, 6] = Bing(0, 6, "black")
        ChessBoard.all_pieces[2, 6] = Bing(2, 6, "black")
        ChessBoard.all_pieces[4, 6] = Bing(4, 6, "black")
        ChessBoard.all_pieces[6, 6] = Bing(6, 6, "black")
        ChessBoard.all_pieces[8, 6] = Bing(8, 6, "black")

        ChessBoard.all_pieces[1, 7] = Pao(1, 7, "black")
        ChessBoard.all_pieces[7, 7] = Pao(7, 7, "black")

        ChessBoard.all_pieces[3, 9] = Shi(3, 9, "black")
        ChessBoard.all_pieces[5, 9] = Shi(5, 9, "black")

        ChessBoard.all_pieces[2, 9] = Xiang(2, 9, "black")
        ChessBoard.all_pieces[6, 9] = Xiang(6, 9, "black")

        ChessBoard.all_pieces[1, 9] = Ma(1, 9, "black")
        ChessBoard.all_pieces[7, 9] = Ma(7, 9, "black")

        ChessBoard.all_pieces[0, 9] = Che(0, 9, "black")
        ChessBoard.all_pieces[8, 9] = Che(8, 9, "black")

    """
    判断有没有这种情况：两王面对面。中间没有任何棋子
    """
    def king_ftf(self):
        for (x, y) in self.all_pieces:
            if self.all_pieces[x, y].is_king :
                sy = 1 if self.all_pieces[x, y].is_north() else -1
                y += sy
                while y != 9 and y != 0:
                    if (x, y) in self.all_pieces :
                        if self.all_pieces[x, y].is_king:
                            return True
                        else:
                            return False
                    y += sy


    """
    移出棋子
    """
    def delete(self, x, y):
        del self.all_pieces[x, y]

    """
    根据用户在棋盘上点击的位置，来决定选子、走棋、吃子等，返回（棋盘是否发生变化，是否已经落子）
    """
    def select(self, x, y, player_color):
        print("select", x, y)
        # 点到当前选中的棋子，棋盘无变化
        if (x, y) in self.all_pieces and self.all_pieces[x, y].selected:
            return False, False
        # 点到己方棋子，选中棋子，棋盘发生变化
        if (x, y) in self.all_pieces and self.all_pieces[x, y].color == player_color:
            if self.selected_pieces:
                self.selected_pieces.selected = False           # 取消当前选中棋子的选中
            self.all_pieces[x, y].selected = True
            self.selected_pieces = self.all_pieces[x, y]
            return True, False
        # 点到可落子的位置
        if self.selected_pieces:
            if self.selected_pieces.can_move(x, y, self):
                self.selected_pieces.move(x, y, self)
                self.selected_pieces.selected = False
                self.selected_pieces = None
                return True, True
            return False, False
        # 点到其他位置，取消选中
        for key in self.all_pieces.keys():
            self.all_pieces[key].selected = False
        self.selected_pieces = None
        return True, False





