#!/usr/bin/env python
# coding: utf-8

# In[72]:


import random

class Player:
    def __init__(self, name, team, rating, availability):
        self.name = name
        self.team = team
        self.rating = rating
        self.availability = availability
        
    def playerPrint(self):
        print(self.name + " plays for " + self.team + " and is rated " + str(self.rating) + " and availability is " + self.availability)
    


# In[73]:


def populate_players(file):
    players = []
    f = open(file, "r")
    for line in f:
        
        player = line.split(',')
       
        if player != ['\n']:
            name = player[0]
            team = player[1].strip()
            rating = int(player[2].strip())
            availability = (player[3].strip()).rstrip()
            players.append(Player(name, team, rating, availability))
            
    return players
        


# In[81]:


deck = populate_players("data.txt")

newdeck = [x for x in deck if x.team == "ManCity"]
newdeck = random.shuffle(deck)

for p in deck:
 
   p.playerPrint()

    


# In[ ]:





# In[ ]:




