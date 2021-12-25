from turtle import Turtle, Screen
import random

tim = Turtle()
timo = Turtle()
tims = Turtle()
tima = Turtle()
time = Turtle()
timu = Turtle()

screen = Screen()
screen.title("Carrera de tortugas")
screen.setup(500, 400)
screen.colormode(255)

players = [tim, timo, tims, tima, time, timu]
for player in players:
    player.shape("turtle")


def colors(colores):
    color = random.choice(colores)
    colores.remove(color)
    return color


def place_players(players):
    posy = 80
    colores = ["blue", "red", "green", "teal", "black", "pink"]
    for player in players:
        player.color(colors(colores))
        player.speed(2)
        player.penup()
        player.goto(-235, posy)
        posy -= 25


def carrera():
    place_players(players)
    user_bet = screen.textinput("Haz tu apuesta", prompt="¿Qué tortuga ganará la carrera? Escribe el color: ")
    final = False
    while not final:
        for player in players:
            player.forward(random.randint(0, 5))
            if player.xcor() > 215:
                if player.pencolor() == user_bet:
                    print("Has ganado la apuesta, el ganador es:", player.pencolor())
                    screen.textinput("NIM", "Name of first player:")
                    final = True
                else:
                    print("Has perdido la apuesta, el ganador es:", player.pencolor())
                    final = True


carrera()
screen.mainloop()
