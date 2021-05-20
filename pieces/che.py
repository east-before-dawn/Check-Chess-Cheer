from NormalPiece import NormalPiece


class Che(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
    找该棋子的图片路径
    """

    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rche_S.gif"
            else:
                return "images/Bche_S.gif"
        else:
            if self.color == 'red':
                return "images/Rche.gif"
            else:
                return "images/Bche.gif"

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
        # che只能走直线
        if abs(dx) != 0 and abs(dy) != 0:
            return False

        # 直线中间不能有棋子
        x, y = self.x, self.y
        sx = dx / abs(dx) if dx != 0 else 0
        sy = dy / abs(dy) if dy != 0 else 0
        if dx == 0:
            while True:
                y += sy
                if y == prey:
                    break
                if (x, y) in chessboard.all_pieces:
                    return False
        else:
            while True:
                x += sx
                if x == prex:
                    break
                if (x, y) in chessboard.all_pieces:
                    return False

        return True
