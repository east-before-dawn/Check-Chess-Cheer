import tkinter
from PIL import Image, ImageTk


def callback(event):
    print(event.x, event.y)
    print(logic_position(event.x), logic_position(event.y))


"""
把逻辑坐标转换成物理坐标
"""


def real_position(x):
    return x*53.5 + 31          # 棋盘方格为55X55大小，棋盘外围大约为30


"""
把物理坐标转换成逻辑坐标
"""


def logic_position(x):
    return round((x-31)/53.5)        # 四舍五入


class ChessView:
    piece_images = dict()           # 保存棋盘所有棋子的PhotoImage对象
    can_move_img = []           # 有多少个可选位置就要有多少个PhotoImage对象，不然引用会被覆盖

    # 绘制棋盘盘面board
    root = tkinter.Tk()
    root.title("中国象棋")
    root.resizable(0, 0)
    can = tkinter.Canvas(root, width=494, height=546)
    can.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    # 通过PIL打开图片
    img = Image.open('images/board.jpg')
    # 通过PIL来生成PhotoImage对象，即可正常加载jpg文件
    photo = ImageTk.PhotoImage(img)
    can.create_image(0, 0, image=photo, anchor=tkinter.NW)

    """
    绘制棋盘棋子
    """

    def draw_board(self):
        ChessView.piece_images.clear()
        ChessView.can_move_img = []
        all_pieces = self.chessboard.all_pieces
        for (x, y) in all_pieces.keys():
            ChessView.piece_images[x, y] = tkinter.PhotoImage(
                file=all_pieces[x, y].get_image_path())
            ChessView.can.create_image(real_position(x), real_position(
                y), image=ChessView.piece_images[x, y])

        if self.chessboard.selected_pieces:      # 有选中的棋子时
            for (x, y) in self.chessboard.selected_pieces.findAll(self.chessboard):       # 找出所有可以走棋的位子

                self.can_move_img.append(
                    tkinter.PhotoImage(file="images/OOS.gif"))
                self.can.create_image(real_position(
                    x), real_position(y), image=self.can_move_img[-1])
                # self.can.create_image(real_position(x), real_position(y), image=tkinter.PhotoImage(file="images/OOS.gif"))

    def __init__(self, game, chessboard):
        self.game = game
        if self.game.mode == 0:
            self.can.bind('<Button-1>', self.game.click)
        self.chessboard = chessboard

    def showMsg(self, msg):
        print(msg)
        self.root.title(msg)

    def quit(self):
        self.root.quit()

    def start(self):
        self.root.mainloop()

    def update(self):
        self.root.update()
