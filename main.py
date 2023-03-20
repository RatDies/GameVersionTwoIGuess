# Global variables -----------------------------------------------------------
import sys
import random
map = [
  ["Enemy", "Empty", "Discover", "Merchant"],
  ["Empty", "Empty", "Start", "Discover"],
  ["Enemy", "Empty", "Empty", "Merchant"],
  ["Npc", "Enemy", "Enemy", "Discover"]
]
#invenstuff
inventory =  ("Objects", "Tools", "Weapons", "Key items")
object = []
tool = []
weapon = []
keyitem = []
number_of_objects = 0
number_of_tools = 0
number_of_weapons = 0
number_of_keyitems = 0
#invenstuff
row = 1
col = 2
mainmenu = ["Walk", "Open Inventory", "Quit"]
directions = ("north", "east", "south", "west")


# Functions ------------------------------------------------------------------
def movement():
  '''Movement Functions'''
  global row, col
  while True:
    print("\nWhat Direction?")
    for action in directions:
      print(f"- {action}")
    action_input = input("Action: ")    
    if action_input.lower() in directions:
      if action_input.lower() == "north":
        row -= 1
      if action_input.lower() == "east":
        col += 1
      if action_input.lower() == "south":
        row += 1
      if action_input.lower() == "west":
        col -= 1
      #print(f"{row},{col}")
      print(f"You decide to go {action_input}!")
      break
    else:
      print("Cant do that you silly billy!\n")


# inventory ------------------------------------------------------------------
def inventorysystem():
  while True:
    if current_location == "Empty":
      print("\nYou open your backpack")
      for invifunc in inventory:
        print(f"- {invifunc}")
      invifunc = input("Action: ")
      if invifunc.lower() in inventory:
        if invifunc.lower() == "objects":
          print(f"\nyou have {number_of_objects} objects")
          print(f"- {object}")
          inspect_input = input("Inspect: ")
          if inspect_input == "ROCK":
            print("\nThis is a rock.")
          else:
            print("You dont have that. Yet....")
          
        if invifunc.lower() == "tools":
          print(f"\nYou have {number_of_tools} tools")
          print(f"- {tool}")
          inspect_input = input("Inspect: ")
          
          
        if invifunc.lower() == "weapons":
          print(f"\nYou have {number_of_weapons} weapons")
          print(f"- {weapon}")
          inspect_input = input("Inspect: ")
          
          
        if invifunc.lower() == "key items":
          print(f"\nYou have {number_of_keyitems} key items")
          print(f"- {keyitem}")
          inspect_input = input("Inspect: ")
          
          
        break
      else:
        print("Cant do that you silly billy!\n")
    else:
      print("You cant do that here. Find a field.")
      break
      
# Main -----------------------------------------------------------------------
while True:
  current_location = map[row][col]
  if current_location == "Start" :
    print("\nLets start this adventure!")
    
  elif current_location == "Empty" :
    print("\nYou found a calm open field.")
    print("Now is a good time to look at your inventory\n")

  elif current_location == "NewEmpty":
    print("\nNothing to see here\n")
    
  elif current_location == "Discover" : 
    print("\nYou found a point of discovery!")
    print("Would you like to explore it?")
    print("- yes")
    print("- no")
    conformation = input("Action: ")
    if conformation.lower() == "yes":
      if random.randint(0,4) == 0:
        print("\nyou found a unlocked treasure chest.")
        print("unfortunatly it's empty.\n")
        map[row][col] = "NewEmpty"

      if random.randint(0,4) == 1:
        print("\nYou found a random key. Congrats! \(0o0)/")
        object.append('Key')
        number_of_objects += 1
        map[row][col] = "NewEmpty"

      if random.randint(0,4) == 2:
        print("You found a rusted short sword. Let's keep it!")
        weapon.append('Rusted short sword')
        number_of_weapons += 1
        map[row][col] = "NewEmpty"

      if random.randint(0,4) == 3:
        print("You found a locked treasure chest!")
        if object 
          print("you use a key.\n")
          print("\nyou found an artifact of the old world.")
          print("You dont seem strong enouch to use it's power.")
          print("Maybe leveling up will work.\n")
        if object
          print("You need a key to open this!")
        
      if random.randint(0,4) == 4:
        print("\nYou found a legendary item, ROCK.") 
        object.append('ROCK')
        number_of_objects += 1
        map[row][col] = "NewEmpty"
    if conformation.lower() == "no":
      print("\nAlrighty!\n")
    
      
  elif current_location == "Merchant" :
    print("\nyou spot a merchant.") 
    print('"Ah, traveler. welcome to my shop."') 
    print('"oh it seems you dont have any money. begone with you!"\n')
  
  elif current_location == "Npc" :
    print("You spot a shabby old man. He begins shouting at you in incoherrent words. you decide to move on.\n")
  
  elif current_location == "Enemy" :
    print("You spot an enemy!") 
    print("he seems a bit too strong for you right now.")
    print("lets just move on, shall we?\n")
 
  print("What Would you like to do?")
  for action in mainmenu:
      print(f"- {action}")
  action_input = input("Action: ")
  if action_input == "walk":
    movement()
  if action_input == "open inventory":
    inventorysystem()
  if action_input == "quit":
    sys.exit()
  #else:
    #print("Wah wah! Inncorect input. try again!\n")

# Invi things