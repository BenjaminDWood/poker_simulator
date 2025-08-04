#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
import pprint
import time

Deck = list(range(1,53))

Deck[0]= 'Ace of Hearts'
Deck[1]= 'Ace of Spades'
Deck[2]= 'Ace of Diamonds'
Deck[3]= 'Ace of Clubs'
Deck[4]= 'Two of Hearts'
Deck[5]= 'Two of Spades'
Deck[6]= 'Two of Diamonds'
Deck[7]= 'Two of Clubs'
Deck[8]= 'Three of Hearts'
Deck[9]= 'Three of Spades'
Deck[10]= 'Three of Diamonds'
Deck[11]= 'Three of Clubs'
Deck[12]= 'Four of Hearts'
Deck[13]= 'Four of Spades'
Deck[14]= 'Four of Diamonds'
Deck[15]= 'Four of Clubs'
Deck[16]= 'Five of Hearts'
Deck[17]= 'Five of Spades'
Deck[18]= 'Five of Diamonds'
Deck[19]= 'Five of Clubs'
Deck[20]= 'Six of Hearts'
Deck[21]= 'Six of Spades'
Deck[22]= 'Six of Diamonds'
Deck[23]= 'Six of Clubs'
Deck[24]= 'Seven of Hearts'
Deck[25]= 'Seven of Spades'
Deck[26]= 'Seven of Diamonds'
Deck[27]= 'Seven of Clubs'
Deck[28]= 'Eight of Hearts'
Deck[29]= 'Eight of Spades'
Deck[30]= 'Eight of Diamonds'
Deck[31]= 'Eight of Clubs'
Deck[32]= 'Nine of Hearts'
Deck[33]= 'Nine of Spades'
Deck[34]= 'Nine of Diamonds'
Deck[35]= 'Nine of Clubs'
Deck[36]= 'Ten of Hearts'
Deck[37]= 'Ten of Spades'
Deck[38]= 'Ten of Diamonds'
Deck[39]= 'Ten of Clubs'
Deck[40]= 'Jack of Hearts'
Deck[41]= 'Jack of Spades'
Deck[42]= 'Jack of Diamonds'
Deck[43]= 'Jack of Clubs'
Deck[44]= 'Queen of Hearts'
Deck[45]= 'Queen of Spades'
Deck[46]= 'Queen of Diamonds'
Deck[47]= 'Queen of Clubs'
Deck[48]= 'King of Hearts'
Deck[49]= 'King of Spades'
Deck[50]= 'King of Diamonds'
Deck[51]= 'King of Clubs'


# In[17]:


Players = []
if len(Deck) == 52:
    while True:
        print("How many players would you like in your game? (2-11)") #Add blank for naming as 'Player 1' etc.
        no_players = int(input())
        if no_players in range(2,12): #Check that there is a valid number of players
            for x in range(no_players):
                msg = "Player " + str(x+1) + " Name:"
                if x == 0: #Allows user to skip individually naming players and assigns random names
                    print(str(msg) + " (Leave blank for random names)")
                    first_name = str(input())
                    if first_name == "":
                        rand_names = ['David','John','Meryl','Eva','Hal','Emma','Jack','Rose','Roy','Naomi','Frank']
                        Players = random.sample(rand_names,k=no_players)
                        break
                    Players.append(str(first_name))
                else:
                    print(str(msg))
                    Players.append(str(input()))
            break
        else:
            print("Please select between 2 and 11 players")
                  
#Summary of game setup printed below
    print("This game will be played by:", end=" ")
    
    if len(Players) == 2:
        print(*Players, sep=" and ")
    elif len(Players) > 2:
        print(f"{', '.join(Players[:-1])}, and {Players[-1]}")
    
    time.sleep(2)

    print("Let's get ready to rumble!!!")
    time.sleep(2)
else:
    print("Deck has not been shuffled! Please return to start.")


# In[18]:


print("The cards are dealt...")
time.sleep(2)
for p in Players:
    cards = random.sample(Deck, k=2)
    for d in cards:
            Deck.remove(d)         
    print(p + "'s hand:", end=" ")
    print(*cards, sep=" and ")
    #Adding in a conditional timer
    if len(Players) <=5:
        time.sleep(1)
    else:
        time.sleep(0.5)
time.sleep(3)


# In[22]:


if len(Deck) == 52 - len(Players)*2:
    print("Feeling floppy?")
    time.sleep(2)
else:
    print("An error has occurred. Perhaps " + random.choice(Players) + " has been cheating? Please restart game.")


# In[20]:


Deck.remove(random.choice(Deck)) #Burns a single card

flop = random.sample(Deck, k=3)
print('Flop: ', end=" ")
print(*flop, sep=", ")
comCar = flop.copy()

for card in flop:
    Deck.remove(card)

time.sleep(2)


# In[25]:


if len(Deck) == 52 - (len(Players)*2 + 4):
    print("Time to Turn!")
else:
    print("An error has occurred. Maybe a card has been lost up " + random.choice(Players) + "'s sleeve? Please restart game.")
time.sleep(2)


# In[24]:


Deck.remove(random.choice(Deck))

turn = random.choice(Deck)
print('Turn: ' + turn)
comCar.append(str(turn))
time.sleep(1)
print("Community cards:", end=" ")
print(*comCar, sep=", ")

Deck.remove(turn)
time.sleep(2)


# In[8]:


if len(Deck) == 52 - (len(Players)*2 + 6):
    print("Ready to River?")
else:
    print("An error has occurred. Please restart game.")

time.sleep(2)


# In[9]:


Deck.remove(random.choice(Deck))

river = random.choice(Deck)
print('River: ' + str(river))
comCar.append(str(river))
time.sleep(1)
print("Community cards:", end=" ")
print(*comCar, sep=", ")


Deck.remove(river)
time.sleep(5)


# In[10]:


if len(Deck) == 52 - (len(Players)*2 + 8):
                 print("A succesful game!")
else:
        print("You done messed up.")

