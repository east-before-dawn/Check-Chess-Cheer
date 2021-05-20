
from NormalPiece import NormalPiece


class Ma(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
        找该棋子的图片路径
        """

    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rma_S.gif"
            else:
                return "images/Bma_S.gif"
        else:
            if self.color == 'red':
                return "images/Rma.gif"
            else:
                return "images/Bma.gif"

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
        # 不能走直线
        if dx == 0 or dy == 0:
            return False
        # 只能走日字
        if abs(dx) + abs(dy) !=3:
            return False
        # 不能吃蹩马腿
        if (x if abs(dx) == 1 else x+dx/2, y if abs(dy) == 1 else y + (dy/2)) in chessboard.all_pieces:
            return False

        return True

