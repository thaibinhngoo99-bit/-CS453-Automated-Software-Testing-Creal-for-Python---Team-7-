def draw():
    background('#2b3e50')
    for ball in balls:
        ball.move()
        ball.display()
    for box in boxes:
        box.move()
        box.display()