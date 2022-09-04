import random

run = True

class Character():

  def __init__(self, name, maxhealth, maxmeter,  attack, speed, status):

    self.name = name
    self.maxhealth = maxhealth
    self.maxmeter = maxmeter
    self.attack = attack
    self.speed = speed
    self.thisSpeed = speed
    self.status = status

    self.meter = maxmeter
    self.health = maxhealth
    self.statusLength = 0;

    if name == "Player 1":
      self.skill = ["Heal Up", "Poison Blade", "Fire Bomb"]
    if name == "Don Capuchino":
      self.skill = ["Right Hand", "Left Hand", "Lunging Lariat"]


def HealUp(player1):
  player1.health = player1.maxhealth
  player1.meter = player1.maxmeter
  player1.status = "None"
  player1.statusLength = 0


def printEnemies(characters):
  baddies = []
  k = 0
  listy = 1
  while k < len(characters):
    #Choose Target
    if characters[k].name != "Player 1" and characters[k].health > 0: 
      print(str(listy) + ": " + characters[k].name + "  Health: " + str(characters[k].health))
      baddies.append(characters[k])
      listy = listy + 1
    k = k + 1
  return baddies

# function orders enemies based on speed, top to bottom
def printOrder(enemys):

  i = 0
  
  while i < len(enemys) - 1:
    n = 0
    while n < len(enemys) - 1:
      if enemys[n].thisSpeed < enemys[n + 1].thisSpeed:
        temp = enemys[n + 1]
        enemys[n + 1] = enemys[n];
        enemys[n] = temp
      n = n + 1
    i = i + 1


  return enemys


def GameFeed(enemys):
  killed = False # if player1 killed
  while len(enemys) > 1 and killed == False:
      
      
      
      speedMult = random.uniform(1.3, 0.7)

      varySpeed = 0
      
      while varySpeed < len(enemys):
        
        enemys[varySpeed].thisSpeed = enemys[varySpeed].thisSpeed * speedMult        
        #print(speedMult)
        #print(str(enemys[varySpeed].thisSpeed) + " " + str(enemys[varySpeed].name))
        varySpeed = varySpeed + 1
        
      printOrder(enemys)
      Fight(enemys)
      
      k = 0
      #search enemies
      while k < len(enemys):
        #if char health is 0
        if enemys[k].health <= 0:
          if enemys[k].name == "Player 1": # and they have the name player1
            print("You Lose")
            killed = True #kill program
            return 0;

          else:
            enemys.pop(k) # otherwise, remove the unnecessary character
        k = k + 1
       # h = 0
      #while h < len(enemys):
        #print(enemys[h].name)
       # h = h + 1
    
  if len(enemys) == 1:

    print("You Win")

def Heal(characters, amount, loss):
  if characters.health < characters.maxhealth and characters.meter >= 6:

    characters.health = characters.health + amount
    characters.meter = characters.meter - loss
    print( characters.name + " health increased to " + str(characters.health)) 


def Fight(characters):
  i = 0
  # find player object
  while i < len(characters):
    attack = ""
    looker = 0
    player1 = []
    
    while looker < len(characters):
      

      if characters[looker].name == "Player 1":
        player1 = characters[looker]
      looker = looker + 1

    
    
    # Player Menu
    if characters[i].name == "Player 1":
      
      if characters[i].health <= 0 or len(characters) <= 1:
        return 0;

      print("What Move will you perform?\n \n1. Attack \n2. Skills")
      attack = input()
      
      if attack == "1":
        print("Which enemy?")
        baddies = printEnemies(characters)
        chooseWho = int(input()) - 1
        DamageCalc(baddies[int(chooseWho)], player1, 1, "None")
      if attack == "2":
        print("Which skill?")
        # Note: put skills into character classes
        skillChoose = 0
        while skillChoose < len(player1.skill):
          print(str(skillChoose + 1) + ". " + player1.skill[skillChoose]);
          skillChoose = skillChoose + 1

        skill = input()
        if skill == "1":
          #Note: make function
          Heal(characters[i], 30, 6);
          
        elif skill == "2":
          if characters[i].meter > 10:
            baddies = printEnemies(characters)
            chooseWho = int(input()) - 1
            print("You used Poison Blade")
            DamageCalc(baddies[int(chooseWho)], player1, 0.75, "Poison")
            
        elif skill == "3":
            print("You used Fire Bomb")
            k = 0
            listy = 1
            while k < len(characters):
              #Choose Target
              if characters[k].name != "Player 1": 
                DamageCalc(characters[k], player1, 0.5, "None")
              k = k + 1
            

      

    #Enemy Menu
    elif characters[i].health > 0:
      
      move = round(random.uniform(0, 2))

      if characters[i].name == "Don Capuchino": #if Boss

        # check for charge from last turn
        if characters[i].status == "Charge R":
          print("The Don unleashes his Right Hand")
          DamageCalc(player1, characters[i], 200, "None")
          characters[i].status = "None"
        elif characters[i].status == "Charge L":
          print("The Don unleashes his Left Hand")
          DamageCalc(player1, characters[i], 100, "Poison")
          characters[i].status = "None"
        #if there ain't any charge
        else:
          if move == 0:

            #if characters[i].status == "None":
              DamageCalc(characters[i], characters[i], 0, "Charge R") #puts charge on himself
              print(characters[i].name + " shouts 'Here's a Right' ");

          elif move == 1:

            #if characters[i].status == "None":
              DamageCalc(characters[i], characters[i], 0, "Charge L") #puts charge on himself
              print(characters[i].name + " shouts 'Here's a Left' ");

          else:
            DamageCalc(player1, characters[i], 10, "None")
          pass


      else :
        DamageCalc(player1, characters[i], 1, "None")
        pass

      if characters[i].status == "Poison" and characters[i].statusLength > 0:
        characters[i].health = characters[i].health - 10
        print(characters[i].name + " took 10 damage from poison")
        characters[i].statusLength = characters[i].statusLength - 1
      input()
      pass

    i = i + 1



def DamageCalc(target, attacker, modifier, status):
  if status == "Poison":
    target.status = "Poison"
    target.statusLength = target.statusLength + 3
  elif status == "Charge R":
    target.status = "Charge R"
  elif status == "Charge L":
    target.status = "Charge L"

  target.health = target.health - (attacker.attack * modifier)
  print("\n" + attacker.name + " attacked")
  soundfx = ["Kerchoo!", "Kabeem!", "Ongaloo!", "Slash!", "Fuham!"]
  choseFx = random.choice(soundfx)
  print(choseFx)
  print(target.name + " took " + str(attacker.attack * modifier) + " damage\nRemaining Health: " + str(target.health))
  if target.health <= 0:
    print(target.name + " has been K.O.'d!")
    target.health = target.health - 1
  





while run == True:

  print("Welcome to the Game. What would you like to do?\n \n 0. Quit Game\n 1. Play Game\n ")
  endGame = input()
  if endGame == "0":
    run = False
  if endGame == "1":
    

    #name, maxhealth, maxmeter,  attack, speed, status
    player1 = Character("Player 1", 100, 100, 20, 10, "None")
    
    #battles

    enemysHive = [Character("Murderous Hornet", 20, 30, 10, 9, "None"),
    Character("Foreman Wasp", 20, 30, 10, 12, "None"),
    Character("Killer Queen Bee", 10, 30, 10, 11, "None")]

    enemysForest = [Character("Vicious Bear", 20, 30, 10, 9, "None"), 
    Character("Biter Ants", 20, 30, 10, 12, "None"), 
    Character("Camo Man", 10, 30, 10, 11, "None"), 
    Character("Tribal Elephant", 10, 30, 10, 11, "None")]

    enemysOcean = [Character("Black-and-Blue Orca", 20, 30, 10, 9, "None"), 
    Character("Sadistic Dolphin", 20, 30, 10, 12, "None"), ]
    
    Boss = [Character("Don Capuchino", 200, 30, 2, 1, "None")]

    retry = True

    while retry == True:
      print("--------------------------")
      print("     --- The Hive ---     ")
      print("--------------------------")
      enemys = enemysHive
      enemys.append(player1)
      GameFeed(enemys)
      if player1.health > 0:
        retry = False
      HealUp(player1)

    retry = True

    while retry == True:
      print("--------------------------")
      print("     --- The Forest ---   ")
      print("--------------------------")
      enemys = enemysForest
      enemys.append(player1)
      GameFeed(enemys)
      if player1.health > 0:
        retry = False
      HealUp(player1)

    retry = True
    
    while retry == True:
      print("--------------------------")
      print("     --- The Ocean ---   ")
      print("--------------------------")
      enemys = enemysOcean
      enemys.append(player1)
      GameFeed(enemys)
      if player1.health > 0:
        retry = False
      HealUp(player1)

    retry = True

    while retry == True:
      print("--------------------------")
      print("     --- The House --- ")
      print("--------------------------")
      enemys = Boss
      enemys.append(player1)
      GameFeed(enemys)
      if player1.health > 0:
        retry = False
      HealUp(player1)
    

    print("Game Over")
    run = False

