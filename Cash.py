from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

change = change * 100

coins = 0

coins += int(change) // 25

change = change % 25

coins += change // 10

change = change % 10

coins += change // 5

change = change % 5

coins += change // 1

print("coins: ", int(coins))