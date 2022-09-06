from random import randrange


def globalvariables():
    global ans4
    global answerHelp
    global answerTakeHelp
    global ans5
    global answerRun
    global answerFight


ans4 = ['Take help', 'take help', 'Offer help', 'offer help']
answerTakeHelp = ['Take help', 'take help']
answerHelp = ['Offer help', 'offer help']
ans5 = ['Run', 'run', 'Fight', 'fight']
answerRun = ['Run', 'run']
answerFight = ['Fight', 'fight']


def inventory():
    global mineralCount
    global fuelGal


mineralCount = 0
fuelGal = 0


def rand50():
    return (int)(randrange(0, 2)) & 1


def rand75():
    return rand50() | rand50()


for i in range(0, 0):
    print(rand75(), end="")

result2 = rand75()
# print(result2)
