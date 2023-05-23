import screen_setting
import fruit
import random

game_win = screen_setting.Game_Screen()

fruits = ["apple", "avocado", "banana", "cherry", "grapes", "orange", "strawberry"]
fruit_list = []

for i in range(0, len(fruits)):
    fruit_list.append(fruit.Fruit(game_win.surface, fruit_type=fruits[i]))



isGameOn = True

while isGameOn:
    game_win.update()
    fruit_list[0].draw()
    fruit_list[0].update()
