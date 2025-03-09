from random import shuffle
from tkinter import *
from tkinter.messagebox import showerror, showinfo

WIDTH = 600
HEIGHT = 600
CELL_AMOUNT = 5
CELL_BG = "blue"
CELL_FG = "white"
CELL_CLICKED = "black"
FONT = f'Impact {HEIGHT//15}'

root = Tk()
root.title("Counting bro!")

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


class Game:
    table = []
    current = 0

    def start(self):
        self.table = [i for i in range(1, (CELL_AMOUNT**2)+1)]
        shuffle(self.table)
        self.table = [self.table[i:i + CELL_AMOUNT] for i in range(0, CELL_AMOUNT**2, CELL_AMOUNT)]

        self.current = 0

        for y in range(CELL_AMOUNT):
            for x in range(CELL_AMOUNT):
                self.paint(y, x, CELL_BG, self.table[x][y])

    def click(self, event):
        x = event.x // (WIDTH//CELL_AMOUNT)
        y = event.y // (HEIGHT//CELL_AMOUNT)
        if self.table[y][x] - self.current == 1:
            self.current = self.table[y][x]
            self.table[y][x] = -1
            self.paint(x, y, CELL_CLICKED)
            if self.current == CELL_AMOUNT**2:
                self.win()
        else:
            self.game_over()

    def game_over(self):
        showerror(*["Game Over!"] * 2)
        self.start()

    def win(self):
        showinfo("Congrats!", "You won!")
        self.start()

    @staticmethod
    def paint(x, y, c, num=-1):
        w = (WIDTH//CELL_AMOUNT)
        h = (HEIGHT//CELL_AMOUNT)
        ex = x * w
        ey = y * h
        canvas.create_rectangle(ex, ey, ex + w, ey + h, fill=c)
        if ~num:
            canvas.create_text(ex + w/2, ey + h/2, text=num, font=FONT, fill=CELL_FG)


game = Game()
game.start()

canvas.bind("<Button-1>", game.click)

root.mainloop()
