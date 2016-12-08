import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    i = 0
    brad = turtle.Turtle()
    while i<4:
        brad.forward(100)
        brad.right(90)
        i+=1
    window.exitonclick()

draw_square()
    
