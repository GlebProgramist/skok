from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.score = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            self.score = False
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score = True
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=colour)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        canvas.bind_all('<KeyPress-Left>', self.turn_left)
        canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos [2] >= self.canvas_width:
            self.x = 0


class Game_Manager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.started = False
        self.canvas.bind_all('<Button-1>', self.start_game)

    def start_game(self, evt):
        self.started = True

tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

i = 0
game = Game_Manager(canvas)
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
game_over_text = canvas.create_text(200, 100, text = 'Game Over', state='hidden')
score_text = canvas.create_text(400, 10, text=i)
while 1:
    if ball.hit_bottom == False and game.started == True:
        ball.draw()
        paddle.draw()
    if ball.score == True:
        i += 1
        canvas.itemconfig(score_text, text = i)
    if ball.hit_bottom == True:
        canvas.itemconfig(game_over_text, state = 'normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
