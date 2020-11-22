from main import *

def game():
  command = input("what would you like to do?\n > ")
  command = command.lower()

  if command == "what should i do?":
    printObjective()

  elif command == "turn left":
    turnLeft()

  elif command == "turn right":
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
      print("you are in a halway. keep walking till you find a room.")    
  
  elif command == "use key":
    useKey()

  elif command == "give coins":
    if house_elf == True and coins >3:
      print_elf_ending()
      global activeGame
      activeGame = False
    else:
      print(                "you dont have enough coins. keep looking around. if you find enough coins ill make you a door")

  else:
    print("        you seem to be getting confused")
