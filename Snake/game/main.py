from tkinter import *
from food import Food
from snake import Snake

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('Ink Free', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: snake.change_direction("left"))
window.bind('<Right>', lambda event: snake.change_direction("right")) 
window.bind('<Up>', lambda event: snake.change_direction("up"))
window.bind('<Down>', lambda event: snake.change_direction("down"))

snake = Snake(BODY_PARTS, SNAKE_COLOR, SPACE_SIZE, canvas, label, GAME_WIDTH, GAME_HEIGHT, score, window, SPEED, direction)
food = Food(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas, FOOD_COLOR)

snake.next_turn(food)

window.mainloop()