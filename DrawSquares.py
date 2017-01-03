import turtle

def initialize_window(color = "white"):
    window = turtle.Screen()
    window.bgcolor(color)
    window.exitonclick()

def draw_square(format = "classic", color = "black", speed = 6):
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

def draw_circle(format = "classic", color="blue", speed = 6):
    chris = turtle.Turtle()
    chris.color(color)
    chris.speed(speed)
    if format not in ["arrow", "turtle", "circle", "square", "triangle", "classic"]:
        chris.shape("classic")
    else:
        chris.shape(format)
    chris.circle(120)

initialize_window()
draw_square("turtle", "red", 1)
draw_circle()
    
