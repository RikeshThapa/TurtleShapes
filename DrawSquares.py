import turtle

def draw_square(format = "classic"):
    window = turtle.Screen()
    window.bgcolor("red")
    i = 0
    brad = turtle.Turtle()
    if format not in ["arrow", "turtle", "circle", "square", "triangle", "classic"]:
        brad.shape("classic")
    else:
        brad.shape(format)
    
    while i<4:
        brad.forward(100)
        brad.right(90)
        i+=1
    window.exitonclick()

draw_square("turtle")
    
