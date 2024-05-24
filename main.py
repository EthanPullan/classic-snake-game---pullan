def my_function():
    global direction
    if direction != "up":
        direction = "down"
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.DOWN,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function)

def pixel_X_Position(n: number):
    return n % 8
def pixelPosition(x: number, y: number):
    return x + y * 8
def newFood():
    global food
    while True:
        food = randint(0, 63)
        for value in theSnake:
            if theSnake[value] == food:
                pass
            else:
                return
def pixel_Y_Position(o: number):
    return (o - o % 8) / 8

def my_function2():
    global direction
    if direction != "right":
        direction = "left"
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.LEFT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function2)

def my_function3():
    global direction
    if direction != "left":
        direction = "right"
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.RIGHT,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function3)

def move():
    if direction == "up":
        theSnake.unshift((snakeHead + 56) % 64)
    elif direction == "down":
        theSnake.unshift((snakeHead + 8) % 64)
    elif direction == "left":
        theSnake.unshift(pixelPosition((snakeHead + 7) % 8, pixel_Y_Position(snakeHead)))
    elif direction == "right":
        theSnake.unshift(pixelPosition((snakeHead + 1) % 8, pixel_Y_Position(snakeHead)))
    display.set_pixel_color_at(theSnake[0], GAME_ZIP64.colors(ZipLedColors.GREEN))
    display.set_pixel_color_at(theSnake.pop(), GAME_ZIP64.colors(ZipLedColors.BLACK))

def my_function4():
    global direction
    if direction != "down":
        direction = "up"
GAME_ZIP64.on_button_press(GAME_ZIP64.ZIP64ButtonPins.UP,
    GAME_ZIP64.ZIP64ButtonEvents.DOWN,
    my_function4)

snakeHead = 0
food = 0
direction = ""
display: GAME_ZIP64.ZIP64Display = None
theSnake: List[number] = []
theSnake = [27]
display = GAME_ZIP64.create_zip64_display()
display.set_brightness(50)
direction = "up"
alive = True
food = randint(0, 63)

def on_forever():
    global snakeHead
    while alive:
        snakeHead = theSnake[0]
        display.clear()
        display.set_pixel_color_at(food, GAME_ZIP64.colors(ZipLedColors.RED))
        index = 0
        while index <= len(theSnake) - 1:
            display.set_pixel_color_at(theSnake[index], GAME_ZIP64.colors(ZipLedColors.GREEN))
            index += 1
        if snakeHead == food:
            theSnake.unshift(food)
            newFood()
        basic.pause(200)
        move()
        display.show()
    while not (alive):
        pass
basic.forever(on_forever)
