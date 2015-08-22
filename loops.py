#Yo dawg i heard you like loops, so i put a loop on your loop so you can loop while you loop
# ~~ https://github.com/DevonWC

import random
import sys
import multiprocessing
import re
import urllib.request
import math

# 0 = heads, 1 = tails

def flipCoin():

    return random.randint(0, 1)


def getCoinSide(c):

    if c == 1:
        return "Tails"
    else:
        return "Heads"

    return True

def toss(n):
    total_flips = 0
    row_check = 0
    row_counter = 0

    while row_counter < n:
        coin_side = flipCoin()
        total_flips = total_flips+1
        if coin_side == row_check:
            row_counter = row_counter+1
        else:
            row_counter = 1
            row_check = coin_side

    return total_flips

def perfect_toss(toss_value):
    toss_check = 0
    total_toss = 0
    toss_counter = 0

    while toss_check != toss_value:
        toss_check = toss(toss_value)
        total_toss = total_toss+1
        toss_counter = toss_counter + toss_check
        #print("You had to try", total_toss, "times to get a perfect toss row, resulting in a total of", toss_counter, "coin tosses")
    return total_toss, toss_counter

avg_flips = 1
t = 1
while t < 10:
    prev = avg_flips
    avg_toss = 0
    avg_flips = 0
    for x in range(1,101):
        value = perfect_toss(t)
        avg_toss = avg_toss + value[0]
        avg_flips = avg_flips + value[1]
        if x == 100:
            t = t+1
            avg_flips = avg_flips/x
            avg_toss = avg_toss/x
            print("Running perfect_toss", x, "times with value", t, "you have an average of", math.ceil(avg_toss),"tosses, and", math.ceil(avg_flips), "flips \nThere was a aproximate", math.ceil(((avg_flips-prev)/prev)*100), "% increase in flips from last run\n")
