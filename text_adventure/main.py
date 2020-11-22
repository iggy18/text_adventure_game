import random
activeGame = True
in_forest = False
lock = False
key = False
inRoom = False
lookOnce = True
have_turned = False
house_elf = False
coins = 0

def generateRandom():
  secret = random.randint(1,3)
  return secret

def generate_less_random():
  secret = random.randint(1,2)
  return secret

def generate_more_random():
  secret = random.randint(1,10)
  return secret

def room():
  am_i_in_room = generate_less_random()
  if am_i_in_room == 2:
    global inRoom
    inRoom = True
    print("                I enter a room")
  else:
    print("                I walk through a hallway")

def nothing():
  print("                I dont see anything of interest")

def printSeen():
  print("                I have already checked this room")

def printLeft():
  print("                I turn left")

def printRight():
  print("                I turn right")

def printStraight():
  print("                I walk through a hallway")

def printNothing():
  print("                I dont see a lock")

def printFound():
  print("                I found a key!")

def printOptions():
  print("""
    you can help me navigate with these commands:
    left
    right
    walk
    look
    use key
    give coins
  """)

def printObjective():
  print("                 navigate me until I reach a room. when I reach a room I can look for a lock or a key. I think if I find a key I can use it to get out of here")

def print_elf_ending():
  print("                a small glowing door has apeared in the wall. it opened all on its own. on the other side of the door things seem a bit different. birds... trees... things you wouldn't expect to find in a computer... oh, and I have eyes now. I'm going to go through the door.")

def turnLeft():
  global have_turned
  if have_turned == False:
    have_turned = True
    printLeft()
    room()
  else:
    print("                I must walk before I can turn")

def walkStraight():
  global have_turned, lookOnce, inRoom, lock, house_elf
  house_elf = False
  have_turned = False
  lookOnce = True
  inRoom = False
  lock = False
  room = generateRandom()
  if room == 1:
    inRoom = True
    print("                I enter a room")
  else:
    print("                I walk through a hallway")

def turnRight():
  global have_turned
  if have_turned == False:
    have_turned = True
    printRight()
    room()
  else:
    print("                I must walk before I can turn")

def CheckForLock():
  global lookOnce
  lookOnce = False
  look = generateRandom()
  if look == 2:
    global lock 
    lock = True
    print("                I see a lock")
  else:
    printNothing()

def Check_For_Key():
  global key 
  if key == True:
    print("                I have a key")
  else:
    look = generateRandom() 
    if look == 3:
      key = True
      print("               I found a key!")

def check_for_coin():
  look = generate_more_random()
  if look == 7:
    global coins
    coins += 1
    print("               I found a bit coin. it looks valuable. I think I'll keep it")

def check_for_house_elf():
  look = generate_less_random()
  if look == 6:
    global house_elf
    house_elf = True
    print("                there is an odd little creature in the room. seems a bit out of place in this computer... it looks like a house elf. its approching me.... it says I can make me a door for three coins. what should I do?")


def useKey():
  if key == False:
    print("                I dont have a key")
  elif lock and key and inRoom == True:
    print("                I have exited the terminal. I can return home. but I wonder how I got trapped in there, or if it'll ever happen again...")
    global activeGame
    activeGame = False
  else:
    print("                nothing happened") 

def intro():


  print("hello user. I'm trapped in this terminal. can you help me out here? I cant see anything, data doesn't have any eyes. tell me what to do")

def game():
  command = input("what should I do?\n > ")
  command = command.lower()

  if command == "what should i do?":
    printObjective()

  elif command == "left":
    turnLeft()

  elif command == "right":
    turnRight()

  elif command == "walk":
    walkStraight()
  
  elif command == "what can i do?":
    printOptions()
  
  elif command == "look around":
    if lookOnce == False:
      printSeen()
    elif inRoom == True:
      CheckForLock()
      Check_For_Key()
      check_for_coin()
      check_for_house_elf()
    else:
      print("I am in a halway. I need to keep walking till I find a room.")    
  
  elif command == "use key":
    useKey()

  elif command == "give coins":
    if house_elf == True and coins >3:
      print_elf_ending()
      global activeGame
      activeGame = False
      global in_forest
      in_forest = True
    else:
      print(                "he says I dont have enough coins. I'll keep looking around. if I find enough coins he says he'll make a door")

  else:
    print("        I seem to be getting confused, what did you say?")

def forest():
  command = input("where should I go now? \n >")

while activeGame == True:
  game()

while in_forest == True:
  forest()