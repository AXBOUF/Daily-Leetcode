import random as rd
import numpy as np
import seaborn as sns
# some changes
def dice_roll():
    lst=[]
    for i in range(6):
        dice_roll = rd.randint(1,6)
        lst.append(dice_roll)
    return lst

def avg_dice_roll(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + avg_dice_roll(lst[1:])






def main():
    print(dice_roll())
    print(avg_dice_roll(dice_roll()))

if __name__ == '__main__':
    main()



