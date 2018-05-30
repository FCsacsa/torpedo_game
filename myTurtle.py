import turtle

Screen = turtle.Screen

turtle.register_shape("11ship.gif")
turtle.register_shape("21ship.gif")
turtle.register_shape("12ship.gif")
turtle.register_shape("31ship.gif")
turtle.register_shape("13ship.gif")
turtle.register_shape("14ship.gif")
turtle.register_shape("41ship.gif")


def mainloop():
    turtle.mainloop()


class ship:

    def __init__(self, length=1, direction='horizontal'):
        self.t = turtle.Turtle(shape='square')
        self.length = length
        self.direction = direction
        self.pic()

    def goto(self, x, y):
        self.t.goto(x, y)

    def pic(self):
        if self.length == 1:
            if self.direction == 'vertical':
                self.t.shape("11ship.gif")
            elif self.direction == 'horizontal':
                self.t.shape("11ship.gif")
            else:
                print("Error 002: Wrong direction")
        elif self.length == 2:
            if self.direction == 'vertical':
                self.t.shape("21ship.gif")
            elif self.direction == 'horizontal':
                self.t.shape("12ship.gif")
            else:
                print("Error 002: Wrong direction")
        elif self.length == 3:
            if self.direction == 'vertical':
                self.t.shape("31ship.gif")
            elif self.direction == 'horizontal':
                self.t.shape("13ship.gif")
            else:
                print("Error 002: Wrong direction")
        elif self.length == 4:
            if self.direction == 'vertical':
                self.t.shape("41ship.gif")
            elif self.direction == 'horizontal':
                self.t.shape("14ship.gif")
            else:
                print("Error 002: Wrong direction")
        else:
            print("Error 001: Wrong length")
