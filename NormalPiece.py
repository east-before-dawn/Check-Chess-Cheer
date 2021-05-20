class NormalPiece:
    selected = False
    is_king = False

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    """
    判断该逻辑位置(prex,prey)能不能落子
    """
    def can_move(self, prex, prey, chessboard):
        pass

    """
    走棋
    """
    def move(self, prex, prey, chessboard):
        if (prex, prey) in chessboard.all_pieces:          # 吃子，将对方棋子挪出棋盘
            chessboard.delete(prex, prey)
        chessboard.delete(self.x, self.y)
        self.x = prex
        self.y = prey
        chessboard.all_pieces[self.x, self.y] = self
        return  True

    """
    找出所有能落子的逻辑位置
    """
    def findAll(self, chessboard):
        can_move = []
        for x in range(9):
            for y in range(10):
                if (x, y) in chessboard.all_pieces and chessboard.all_pieces[x, y].color == self.color:
                    continue
                if self.can_move(x, y, chessboard):
                    can_move.append((x, y))
        return can_move

    """
    判断南北
    """
    def is_south(self):
        return self.color == "black"
    def is_north(self):
        return self.color == "red"