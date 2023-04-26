def printFixed():
    print("This is a fixed end beam")
    print("The vertical lines represent the wall the beam is fixed to")
    print()
    print(" |____________")
    print("A|____________|B")
    print(" |")

    
def printSimply():
    print("This is a cantilever beam:")
    print("[/\] represents a pin support, [O] represents a roller support")
    print()
    print(" ______________")
    print("A|_____________|")
    print(" /\\            O")

def printOverhang():
    print("This is an overhanging beam")
    print()
    print(" ________________")
    print("A|_______________|B")
    print("     /\\     O")


def fixedProps():
    forces = {}
    running = True
    length = int(input("How long would you like the beam to be in meters: "))
    print()
    print("Enter the forces you would like on the fixed beam!")
    print()
    while running == True:
        enter = input("Press [f] to enter another force, or press [q] if you are content with your forces you added: ")
        print()
        if enter == "f":
            magnitude = int(input("How many Newtons would you like your force to be: "))
            print()
            dist = int(input("How far from the fixed end would you like this force to be in meters: "))
            print()
            if dist > length:
                print("ERROR: Force cannot be farther from the fixed end than the length of the beam!")
                print()
            else:
                forces[dist] = magnitude
        elif enter == "q":
            running = False
        else:
            print("ERROR: Invalid character entered")
            print()
    return length, forces

def simplyProps():
    forces = {}
    running = True
    length = int(input("How long would you like the beam to be in meters: "))
    print()
    print("Enter the forces you would like on the simply supported beam!")
    print()
    while running == True:
        enter = input("Press [f] to enter another force, or press [q] if you are content with your forces you added: ")
        print()
        if enter == "f":
            magnitude = int(input("How many Newtons would you like your force to be: "))
            print()
            dist = int(input("How far from the fixed end would you like this force to be in meters: "))
            print()
            if dist > length:
                print("ERROR: Force cannot be farther from the fixed end than the length of the beam!")
                print()
            else:
                forces[dist] = magnitude
        elif enter == "q":
            running = False
        else:
            print("ERROR: Invalid character entered")
            print()
    return length, forces
    



