import random


def moveCarsForward(amount, alist):
    alist.pop(0)
    amount -= 1
    print("Car crosses road!")
    return amount, alist


def GenerateNewCars(alist, blist, clist, a, b, c):
    r = random.randint(1, 4)
    if r == 1:
        r2 = random.randint(1, 3)
        print("New car(s) (", r2, ") arravied to B", sep="")
        for i in range(r2):
            alist.append(0)
        a += r2
    elif r == 2:
        r2 = random.randint(1, 3)
        print("New car(s) (", r2, ") arravied to A east", sep="")
        for i in range(r2):
            blist.append(0)
        b += r2
    elif r == 3:
        r2 = random.randint(1, 3)
        print("New car(s) (", r2, ") arravied to A west", sep="")
        for i in range(r2):
            clist.append(0)
        c += r2
    return alist, blist, clist, a, b, c


def addTime(alist, blist, clist):
    for time in range(len(alist)):
        alist[time] += 1
    for time in range(len(blist)):
        blist[time] += 1
    for time in range(len(clist)):
        clist[time] += 1
    return alist, blist, clist


if __name__ == '__main__':
    NumAeast = 0
    NumAwest = 0
    NumB = 0
    TimeAeast = []
    TimeAwest = []
    TimeB = []
    Loop = 75  # amount of iterations
    x = 0
    while Loop != 0:
        if x == 1:
            if NumAeast == 0 and NumAwest == 0:  # If no car is on A road, change light
                print("A road empty")
                if NumB != 0:
                    x = 0
                    TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                    Loop -= 1  # time passes when light’s change
                    print("changing light because someone is waiting on B road")
            elif NumAeast != 0 and NumAwest != 0 and NumB != 0:
                if TimeB[0] >= 4 * TimeAeast[0] and TimeB[0] >= 4 * TimeAwest[0]:
                    # if first in B wait time is four times more than first in either part of A road change lights.
                    NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                    NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                    x = 0
                    Loop -= 1  # time passes when light’s change
                    TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                    print("A road, Change light")
                else:
                    if NumAeast != 0:
                        NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                    if NumAwest != 0:
                        NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                    print("Green on A road")
            elif NumAeast != 0 and NumB != 0:
                if TimeB[0] >= 4 * TimeAeast[0]:
                    # if first in B wait time is four times more than first in either part of A road change lights.
                    NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                    x = 0
                    Loop -= 1  # time passes when light’s change
                    TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                    print("Next on B road has waited four times longer than next on A road east, Change light")
                else:
                    if NumAeast != 0:
                        NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                    if NumAwest != 0:
                        NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                    print("Green on A road")
            elif NumAwest != 0 and NumB != 0:
                if TimeB[0] >= 4 * TimeAwest[0]:
                    # if first in B wait time is four times more than first in either part of A road change lights.
                    NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                    x = 0
                    Loop -= 1  # time passes when light’s change
                    TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                    print("Next on B road has waited four times longer than next on A road west, Change light")
                else:
                    if NumAeast != 0:
                        NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                    if NumAwest != 0:
                        NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                    print("Green on A road")
            else:
                if NumAeast != 0:
                    NumAeast, TimeAeast = moveCarsForward(NumAeast, TimeAeast)
                if NumAwest != 0:
                    NumAwest, TimeAwest = moveCarsForward(NumAwest, TimeAwest)
                print("Green on A road")
        elif x == 0:
            if NumB == 0:  # If no car is on A road, change light
                print("B road empty")
                if NumAeast != 0 or NumAwest != 0:
                    x = 1
                    TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                    Loop -= 1  # time passes when light’s change Else
                    print("changing light because someone is waiting on A road")
            else:
                if NumAeast != 0 and NumAwest:
                    if TimeB[0] * 4 <= TimeAeast[0] or TimeB[0] * 4 <= TimeAwest[0]:
                        # if first in A - east or A - west wait time is four times more than first in b change lights.
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        x = 1
                        TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                        Loop -= 1
                        print("Next on A road has waited four times longer than next on B road, Change light")
                    else:
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        print("Green on B road")
                elif NumAeast != 0:
                    if TimeB[0] * 4 <= TimeAeast[0]:
                        # if first in A - east or A - west wait time is four times more than first in b change lights.
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        x = 1
                        TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                        Loop -= 1
                        print("Next on A road east has waited four times longer than next on B road, Change light")
                    else:
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        print("Green on B road")
                elif NumAwest != 0:
                    if TimeB[0] * 4 <= TimeAwest[0]:
                        # if first in A - east or A - west wait time is four times more than first in b change lights.
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        x = 1
                        TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
                        Loop -= 1
                        print("Next on A road west has waited four times longer than next on B road, Change light")
                    else:
                        NumB, TimeB = moveCarsForward(NumB, TimeB)
                        print("Green on B road")
                else:
                    NumB, TimeB = moveCarsForward(NumB, TimeB)
                    print("Green on B road")
        TimeAeast, TimeAwest, TimeB, NumAeast, NumAwest, NumB = GenerateNewCars(TimeAeast, TimeAwest, TimeB, NumAeast, NumAwest, NumB)
        if NumB != 0:
            if TimeB[0] > 20:
                print("Traffic jam on B road")
        if NumAeast != 0:
            if TimeAeast[0] > 20:
                print("Traffic jam on A east road")
        if NumAwest != 0:
            if TimeAwest[0] > 20:
                print("Traffic jam on A west road")
        TimeB, TimeAeast, TimeAwest = addTime(TimeB, TimeAeast, TimeAwest)
        Loop -= 1
        print("Current sitsuation B, A east and A west:", NumB, TimeB, NumAeast, TimeAeast, NumAwest, TimeAwest)
