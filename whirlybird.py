def whirlybird():
    import math
    question = raw_input('Ask Me a Question: ')
    color = raw_input("Pick a color: ")
    color = len(color)
    color = int(color)
    numberone = raw_input('Pick a number: ')
    numberone = int(numberone)
    numbertwo = raw_input('Pick another number: ')
    numbertwo = int(numbertwo)
    total = color + numberone + numbertwo
    fortune = total % 4
    if fortune == 0:
        fortune = "Yes"
    elif fortune == 1:
        fortune = "No"
    elif fortune == 2:
        fortune = "Maybe..."
    else:
        fortune = "I'm not sure, try again."
    print fortune

whirlybird()
