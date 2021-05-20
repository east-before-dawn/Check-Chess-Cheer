from NormalPiece import NormalPiece

class Shi(NormalPiece):
    def __init__(self, x, y, color):
        NormalPiece.__init__(self, x, y, color)

    """
    找该棋子的图片路径
    """
    def get_image_path(self):
        if self.selected == True:
            if self.color == 'red':
                return "images/Rshi_S.gif"
            else:
                return "images/Bshi_S.gif"
        else:
            if self.color == 'red':
                return "images/Rshi.gif"
            else:
                return "images/Bshi.gif"

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

        # shi只能走米字格的斜边，且只能走一步
        if not (self.is_north() and 3 <= prex <= 5 and 0 <= prey <= 2) and\
                not (self.is_south() and 3 <= prex <= 5 and 7 <= prey <= 9):
            print('shi不能超出米字格！',prex,prey)
            return False

        if abs(dx) != 1 or abs(dy) != 1:
            print("只能斜着走一步")
            return False

        return True