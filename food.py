from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("slowest")  # so we don't have to see how the new food gets generated
        self.create_food()

    def create_food(self):
        random_food_x = random.randint(-280, 280)
        random_food_y = random.randint(-280, 280)
        self.goto(random_food_x, random_food_y)
