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
inventory =  ("objects", "tools", "weapons", "key items")
object = []
tool = []
weapon = ['Rusted short sword']
keyitem = []
number_of_objects = 0
number_of_tools = 0
number_of_weapons = 0
number_of_keyitems = 0
#invenstuff
row = 0#1
col = 0#2
mainmenu = ["walk", "open Inventory", "quit"]
directions = ("north", "east", "south", "west")
combat_actions = ["attack", "defend"]
HP = 12
enemy_HP = 20

# Functions ------------------------------------------------------------------
# Map isnt meant to end, should be unending
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
          print("- Close Backpack")
          inspect_input = input("Inspect: ")
          if inspect_input == "ROCK":
            print("\nThis is a rock.")
            break
          elif inspect_input == "close backpack":
            break
          else:
            print("You dont have that. Yet....")
          
        if invifunc.lower() == "tools":
          print(f"\nYou have {number_of_tools} tools")
          print(f"- {tool}")
          print("- Close Backpack")
          inspect_input = input("Inspect: ")
          
          
        if invifunc.lower() == "weapons":
          print(f"\nYou have {number_of_weapons} weapons")
          print(f"- {weapon}")
          print("- Close Backpack")
          inspect_input = input("Inspect: ")
          if inspect_input == "rusted short sword":
            print("\nThis sword is practically useless.") 
            print("But it's better than nothing.")
            break
          elif inspect_input == "close backpack":
            break
          else:
            print("You dont have that. Yet....")
          
        if invifunc.lower() == "key items":
          print(f"\nYou have {number_of_keyitems} key items")
          print(f"- {keyitem}")
          print("- Close Backpack")
          inspect_input = input("Inspect: ")
          if inspect_input == "Key":
            print("\nA key. Who knows what it could open.")
            break
          elif inspect_input == "close backpack":
            break
          else:
            print("You dont have that. Yet....")
          
          
        break
      else:
        print("Cant do that you silly billy!\n")
    else:
      print("best to find somewhere safe to do this...")
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
    print("\nYou already searched this area\n")
    
  elif current_location == "Discover" : 
    print("\nYou found a point of discovery!")
    print("Would you like to explore it?")
    print("- yes")
    print("- no")
    conformation = input("Action: ")
    if conformation.lower() == "yes":
      result = random.randint(0,7)
      if result == 0:
        print("\nyou found a unlocked treasure chest.")
        print("unfortunatly it's empty.\n")
        map[row][col] = "NewEmpty"
        
      elif result == 1:
        print("\nYou found a random key. Congrats! \(0o0)/")
        print("[KEY WAS ADDED TO OBJECTS]")
        object.append('Key')
        number_of_objects += 1
        map[row][col] = "NewEmpty"
      elif result == 2:
        print("\nYou found a random key. Congrats! \(0o0)/")
        print("[KEY WAS ADDED TO OBJECTS]")
        object.append('Key')
        number_of_objects += 1
        map[row][col] = "NewEmpty"

      elif result == 3:
        print("\nYou found a rusted short sword. Let's keep it!\n")
        print("[RUSTED SHORT SWORD WAS ADDED TO WEAPONS]")
        weapon.append('Rusted short sword')
        number_of_weapons += 1
        map[row][col] = "NewEmpty"

      elif result == 4:
        print("\nYou found a locked treasure chest!")
        for objects in object:
          if objects == 'Key':
            print("you use a key.")
            print("\nyou found an artifact of the old world.")
            print("You dont seem strong enouch to use it's power.")
            print("Maybe being a higher level will help.\n")
            object.remove('Key')
            number_of_objects -= 1
          else:
            print("You need a key to open this!\n")
      elif result == 5:
        print("\nYou found a locked treasure chest!")
        for objects in object:
          if objects == 'Key':
            print("you use a key.")
            print("\nyou found an artifact of the old world.")
            print("You dont seem strong enouch to use it's power.")
            print("Maybe being a higher level will help.\n")
            object.remove('Key')
            number_of_objects -= 1
          else:
            print("You need a key to open this!\n")
      elif result == 6:
        print("\nYou found a locked treasure chest!")
        for objects in object:
          if objects == 'Key':
            print("you use a key.")
            print("\nyou found an artifact of the old world.")
            print("You dont seem strong enouch to use it's power.")
            print("Maybe being a higher level will help.\n")
            object.remove('Key')
            number_of_objects -= 1
          else:
            print("You need a key to open this!\n")
        
      elif result == 7:
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
    print("\nA wild Boar appears!")
    for Weapons in weapon:
      if Weapons == 'Rusted short sword':
        print("The beast seems intent on killing you\n")
        print("What do you do?")
        for action in combat_actions:
          print(f"- {combat_actions}")
        print(f"You have {HP} HP")
        combat_input = input("Action: ")
        if combat_input == "defend":
          print("You defend and heal ")
          #system to heal player upon defendung but cnat go past max HP
          print("The boar cant get past your defensive stance. He dealt 1 damage")
        elif comabt_input == "attack":
          result = random.randint(0,3)
          if result == 0:
            print("You slash the boar leaving yourself open! Dealt 2 damage!")
            #ffghhf
            print("The boar quickly responds with a bite! He did 5 damage!")
            #jfjhfjhf
          if result == 1:
            print()
      else:
        print("he seems a bit too strong for you right now.")
        print("lets just move on, shall we?\n")
  
 
  print("What Would you like to do?")
  for action in mainmenu:
      print(f"- {action}")
  action_input = input("Action: ")
  if action_input == "walk":
    movement()
  elif action_input == "open inventory":
    inventorysystem()
  elif action_input == "quit":
    sys.exit()
  else:
    print("Wah wah! Inncorect input. try again!\n")

# Combat Testing
if current_location == "Enemy":
  print("\nA wild Boar appears!")
  print("The beast seems intent on killing you\n")
  print("What do you do?")
  print(f"- {combat_actions}")
  print(f"You have {HP} HP")