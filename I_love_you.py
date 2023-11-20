# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:06:42 2023

@author: DELL
"""

import turtle

# Function to draw a heart
def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Function to write "I love you" inside the heart
def write_love_phrase():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.color("white")
    turtle.write("I love you", align="center", font=("Arial", 16, "normal"))

# Main function
def main():
    turtle.speed(2)
    turtle.bgcolor("black")
    turtle.color("red")
    draw_heart()
    write_love_phrase()
    turtle.hideturtle()
    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
