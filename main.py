import screen_setting
import fruit
import random

game_win = screen_setting.Game_Screen()

fruits = ["apple", "avocado", "banana", "cherry", "grapes", "orange", "strawberry"]
fruit_list = []

this_fruit = None

def init():
    global fruit_list
    for i in range(0, len(fruits)):
        fruit_list.append(fruit.Fruit(game_win.surface, fruit_type=fruits[i]))

def get_fruit():
    global this_fruit
    this_fruit = fruit_list[random.randrange(0, len(fruit_list))]
    this_fruit.posY = 500
    this_fruit.posX = random.randrange(0, this_fruit.fruit_sprite.get_width())
    this_fruit.isVisible = True
    this_fruit.set_speed()


def run():
    init()
    get_fruit()
    while True:
        game_win.update()
        this_fruit.update()
        this_fruit.draw()
        if this_fruit.posY >= 500 or not this_fruit.isVisible:
            get_fruit()
            continue

if __name__=='__main__':
    run()