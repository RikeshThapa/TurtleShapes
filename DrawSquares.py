import turtle

def draw_square(format = "classic", color = "black", speed = 6):
    window = turtle.Screen()
    window.bgcolor("red")
    i = 0
    brad = turtle.Turtle()
    brad.color(color)
    brad.speed(speed)
    if format not in ["arrow", "turtle", "circle", "square", "triangle", "classic"]:
        brad.shape("classic")
    else:
        brad.shape(format)
    
    while i<4:
        brad.forward(100)
        brad.right(90)
        i+=1
    window.exitonclick()

draw_square("turtle", "blue", 1)
    
