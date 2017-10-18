#/usr/bin/python3
from tkinter import font, Label, mainloop, Tk, Frame
#import tkinter.font as tkFont
import sys
sys.path.append('models')
from board import Board


class View:

  def __init__(self):
    self.board = Board(4)

    self.initialize_board()
    self.BOX_SIZE = 200

    mainloop()

  def leftPressed(self, event):
    print("left")
    self.board.update_left()
    self.update_board()


  def rightPressed(self, event):
    print("right")
    self.board.update_right()
    self.update_board()

  def upPressed(self, event):
    print("up")
    self.board.update_up()
    self.update_board()

  def downPressed(self, event):
    print("down")
    self.board.update_down()
    self.update_board()

  def initialize_board(self):
    self.root = Tk()
    self.customFont = font.Font(root=self.root, size=20)
    self.grid = []
    for i in range(self.board.board_size):
      self.grid.append([])
      for j in range(self.board.board_size):
        value = self.board.tiles[i][j].value
        w = Frame(self.root, width=100, height=100, borderwidth=2, relief="solid")
        w.pack_propagate(0)
        label = Label(w, text=str(value), font=self.customFont, background=self.get_background(value))
        label.place(anchor='center', relx=50, rely=50)
        label.pack(expand=True, fill='both')
        w.grid(column=j, row=i)
        self.grid[i].append(label)
    self.score_label = Label(self.root, text="score: 0", font=self.customFont)
    self.score_label.pack()
    self.score_label.grid(column=self.board.board_size, row=self.board.board_size)
    self.root.bind("<Left>", self.leftPressed)
    self.root.bind("<Right>", self.rightPressed)
    self.root.bind("<Up>", self.upPressed)
    self.root.bind("<Down>", self.downPressed)

  def get_background(self, value):
      value_to_color = {
        0: '#FFFFFF',
        1: '#FFDDDD',
        2: '#FFBBBB',
        4: '#FF9999',
        8: '#FF7777',
        16: '#FF5555',
        32: '#FF3333',
        64: '#FF0000',
        128: '#00FF00',
        256: '#22FF22',
        512: '#44FF44',
        1024: '#66FF66',
        2048: '#88FF88',
        4096: '#AAFFAA'
      }
      return value_to_color[value]

  def update_board(self):
    self.score_label['text'] = 'score: ' + str(self.board.score)
    for i in range(self.board.board_size):
      for j in range(self.board.board_size):
        new_value = self.board.tiles[i][j].value
        self.grid[i][j]['text'] = new_value
        self.grid[i][j]['background'] = self.get_background(new_value)





  def update_view(self):
    return "lol"


if __name__=="__main__":
  view = View()
