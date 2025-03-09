from food import Food

class Snake:
    def __init__(self, BODY_PARTS, SNAKE_COLOR, SPACE_SIZE, canvas, label, GAME_WIDTH, GAME_HEIGHT, score, window, SPEED, direction):
        self.body_size = BODY_PARTS
        self.snake_color = SNAKE_COLOR
        self.space_size = SPACE_SIZE
        self.game_width = GAME_WIDTH
        self.game_height = GAME_HEIGHT
        self.speed = SPEED

        self.canvas = canvas
        self.label = label
        self.score = score
        self.window = window
        self.direction = direction

        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def next_turn(self, food):
        x, y = self.coordinates[0]

        if self.direction == "up":
            y -= self.space_size
        elif self.direction == "down":
            y += self.space_size
        elif self.direction == "left":
            x -= self.space_size
        elif self.direction == "right":
            x += self.space_size

        self.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color, tag="snake")
        self.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            self.score += 1
            self.label.config(text="Score:{}".format(self.score))
            self.canvas.delete("food")
            food = Food(self.game_width, self.game_height, self.space_size, self.canvas, "#FF0000")
        else:
            del self.coordinates[-1]
            self.canvas.delete(self.squares[-1])
            del self.squares[-1]

        if self.is_collision():
            self.game_over()
        else:
            self.window.after(self.speed, self.next_turn, food)

    def change_direction(self, new_direction):
        global direction

        if new_direction == 'left':
            if self.direction != 'right':
                self.direction = new_direction
        elif new_direction == 'right':
            if self.direction != 'left':
                self.direction = new_direction
        elif new_direction == 'up':
            if self.direction != 'down':
                self.direction = new_direction
        elif new_direction == 'down': 
            if self.direction != 'up':
                self.direction = new_direction

    def is_collision(self):
        x, y = self.coordinates[0]

        if x < 0 or x >= self.game_width:
            print("Game Over")
            return True
        elif y < 0 or y >= self.game_height:
            print("Game Over")
            return True
        for body_part in self.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print("Game Over")
                return True
        return False

    def game_over(self):
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, font=('Ink Free', 70), text="Game Over", fill="red", tag="gameover")