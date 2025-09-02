import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['blue', 'green', 'orange', 'cyan', 'yellow', 'black', 'brown', 'red', 'purple', 'pink']

def get_number_of_turtle():
    while True:
        racers = input("Enter the number of racer turtles you want (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number is not in range, try 2-10.")
        else:
            print("Input is not numeric, try again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing (Bottom to Top)")
    return screen

def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    start_x = -WIDTH//2 + spacing
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.penup()
        racer.setheading(90)  # Face upward
        racer.setpos(start_x + i * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randint(1, 10)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2 - 20:  # finish line check (top edge)
                return racer.pencolor()

def main():
    racers = get_number_of_turtle()
    screen = init_turtle()
    random.shuffle(COLORS)
    selected_colors = COLORS[:racers]
    turtles = create_turtles(selected_colors)
    winner = race(turtles)
    print("The winner is:", winner)
    time.sleep(5)

if __name__ == "__main__":
    main()
