
from NormalPiece import NormalPiece


class Shuai(NormalPiece):
    is_king = True

    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
        找该棋子的图片路径
    """
    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rshuai_S.gif"
            else:
                return "images/Bshuai_S.gif"
        else:
            if self.color == 'red':
                return "images/Rshuai.gif"
            else:
                return "images/Bshuai.gif"

    """
        判断该逻辑位置(prex,prey)能不能落子
    """
    def can_move(self, prex, prey, chessboard):
        x, y = self.x, self.y
        dx, dy = prex - self.x, prey - self.y
        # 越界
        if prex < 0 or prex > 8 or prey < 0 or prey > 9:
            return False
        # 点到己方棋子
        if (prex, prey) in chessboard.all_pieces and chessboard.all_pieces[prex, prey].color == self.color:
            return False
        # 只能走一步
        if abs(dx) + abs(dy) != 1:
            return False
        # 不能走出米字格
        if not (self.is_north() and 3 <= prex <= 5 and 0 <= prey <= 2) and not (
                self.is_south() and 3 <= prex <= 5 and 7 <= prey <= 9):
            return False
        """
        将和帅是不能在同一条直线上直接对面的，两者中间必须有棋子隔着，不然后手走的那一方就输了。
        """
        return True