from NormalPiece import NormalPiece


class Xiang(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
    找该棋子的图片路径
    """

    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rxiang_S.gif"
            else:
                return "images/Bxiang_S.gif"
        else:
            if self.color == 'red':
                return "images/Rxiang.gif"
            else:
                return "images/Bxiang.gif"

    """
    判断该逻辑位置(prex,prey)能不能落子
    """

    def can_move(self, prex, prey, chessboard):
        dx, dy = prex-self.x, prey-self.y
        # 越界
        if prex < 0 or prex > 8 or prey < 0 or prey > 9:
            return False
        # 点到己方棋子
        if (prex, prey) in chessboard.all_pieces and chessboard.all_pieces[prex, prey].color == self.color:
            return False
        # 点到河对面，xiang不能过河
        if (self.is_north() and prey > 4) or (self.is_south() and prey < 5):
            return False
        # xiang走田
        if abs(dx) != 2 or abs(dy) != 2:
            return False
        # 田中间不能有棋子
        sx, sy = dx / abs(dx), dy / abs(dy)
        if (self.x + sx, self.y + sy) in chessboard.all_pieces:
            return False

        return True
