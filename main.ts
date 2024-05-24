GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Down, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    if (direction != "up") {
        direction = "down"
    }
})
function pixel_X_Position (n: number) {
    return n % 8
}
function pixelPosition (x: number, y: number) {
    return x + y * 8
}
function newFood () {
    while (true) {
        food = randint(0, 63)
        for (let value of theSnake) {
            if (theSnake[value] == food) {
                break;
            } else {
                return
            }
        }
    }
}
function pixel_Y_Position (o: number) {
    return (o - o % 8) / 8
}
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Left, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    if (direction != "right") {
        direction = "left"
    }
})
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Right, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    if (direction != "left") {
        direction = "right"
    }
})
function move () {
    if (direction == "up") {
        theSnake.unshift((snakeHead + 56) % 64)
    } else if (direction == "down") {
        theSnake.unshift((snakeHead + 8) % 64)
    } else if (direction == "left") {
        theSnake.unshift(pixelPosition((snakeHead + 7) % 8, pixel_Y_Position(snakeHead)))
    } else if (direction == "right") {
        theSnake.unshift(pixelPosition((snakeHead + 1) % 8, pixel_Y_Position(snakeHead)))
    }
    display.setPixelColorAt(theSnake[0], GAME_ZIP64.colors(ZipLedColors.Green))
    display.setPixelColorAt(theSnake.pop(), GAME_ZIP64.colors(ZipLedColors.Black))
}
GAME_ZIP64.onButtonPress(GAME_ZIP64.ZIP64ButtonPins.Up, GAME_ZIP64.ZIP64ButtonEvents.Down, function () {
    if (direction != "down") {
        direction = "up"
    }
})
let snakeHead = 0
let food = 0
let direction = ""
let display: GAME_ZIP64.ZIP64Display = null
let theSnake: number[] = []
theSnake = [27]
display = GAME_ZIP64.createZIP64Display()
display.setBrightness(50)
direction = "up"
let alive = true
food = randint(0, 63)
basic.forever(function () {
    while (alive) {
        snakeHead = theSnake[0]
        display.clear()
        display.setPixelColorAt(food, GAME_ZIP64.colors(ZipLedColors.Red))
        for (let index = 0; index <= theSnake.length - 1; index++) {
            display.setPixelColorAt(theSnake[index], GAME_ZIP64.colors(ZipLedColors.Green))
        }
        if (snakeHead == food) {
            theSnake.unshift(food)
            newFood()
        }
        basic.pause(200)
        move()
        display.show()
    }
    while (!(alive)) {
    	
    }
})
