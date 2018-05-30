import myTurtle

size = 5

ship = myTurtle.ship(4, 'horizontal')


def make_da_table():
    myTurtle.Screen().bgcolor('blue')
    myTurtle.Screen().bgpic('Evolut12.gif')


def game():
    make_da_table()


game()
myTurtle.mainloop()
