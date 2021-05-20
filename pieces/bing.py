
from NormalPiece import NormalPiece


class Bing(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
        找该棋子的图片路径
        """

    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rbing_S.gif"
            else:
                return "images/Bbing_S.gif"
        else:
            if self.color == 'red':
                return "images/Rbing.gif"
            else:
                return "images/Bbing.gif"

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
        # 不能后退
        if (self.is_north() and dy == -1) or (self.is_south() and dy == 1):
            return False
        # 过了河之后才能横着走，没过河只能直着走
        if dy == 0:
            if (self.is_north() and y < 5) or (self.is_south() and y > 4):
                return False

        return True