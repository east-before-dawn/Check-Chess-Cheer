from NormalPiece import NormalPiece

class Pao(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
    找该棋子的图片路径
    """
    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rpao_S.gif"
            else:
                return "images/Bpao_S.gif"
        else:
            if self.color == 'red':
                return "images/Rpao.gif"
            else:
                return "images/Bpao.gif"

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
        # pao只能走直线
        if abs(dx) != 0 and abs(dy) != 0:
            return False

        count = 0           # 用来记录处在该路径的棋子总数
        # 直线中间只能有0个或1个
        x, y = self.x, self.y
        sx = dx / abs(dx) if dx != 0 else 0
        sy = dy / abs(dy) if dy != 0 else 0
        if dx == 0:
            sy = dy / abs(dy)
            while True:
                y += sy
                if y == prey:
                    break
                if (x, y) in chessboard.all_pieces:
                    count += 1
        else:
            sx = dx / abs(dx)
            while True:
                x += sx
                if x == prex:
                    break
                if (x, y) in chessboard.all_pieces:
                    count += 1

        if count == 0 and (prex, prey) in chessboard.all_pieces and chessboard.all_pieces[prex, prey].color != self.color:
            return False
        if count == 1 and (prex, prey) not in chessboard.all_pieces:
            return False
        if count > 1:
            return False

        return True