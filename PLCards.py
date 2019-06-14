#!/usr/bin/env python
# coding: utf-8

# In[72]:


import random

class Game:
    def __init__(self):
        self.time = 0
        self.over = False

    def populate_deck(self, file):
        deck = []
        iterator = 1
        f = open(file, "r")
        for line in f:
            
            player = line.split(',')
           
            if player != ['\n']:
                name = player[0]
                team = player[1].strip()
                rating = int(player[2].strip())
                availability = (player[3].strip()).rstrip()
                deck.append(Card(iterator, name, team, rating, availability))
                iterator += 1

        return deck

    def generate_players(self):
        p1name = input("Enter Player 1's name: ")
        p2name = input("Enter Player 2's name: ")

        player1 = Player(p1name)
        player2 = Player(p2name)
        





class Card:
    def __init__(self, num, name, team, rating, availability):
        self.id = num
        self.name = name
        self.team = team
        self.rating = rating
        self.availability = availability
        
    def cardPrint(self):
        print(self.name + "    Team: " + self.team + " Rating: " + str(self.rating) + " Rarity: " + self.availability)
    


class Player:
    def __init__(self, name):
        self.deck = []
        self.name = name
        self.score = 0

    def drawCard(self, deck):
        self.deck.append(deck.pop(0))

    def printHand(self):
        print(self.name + "'s hand is: ")
        for i in range(len(self.deck)):
            selector = i + 1
            sentence = "[" + str(selector) + "] to play this player"
            print(" %-20s %-20s %-13s %-15s" % (self.deck[i].name, "Team: " + self.deck[i].team, "Rating: " + str(self.deck[i].rating), "Rarity: " + self.deck[i].availability), sentence)

   #def playCard(self, cardID):




        

def runGame():
    game = Game()
    deck = game.populate_deck("data.txt")
    #newdeck = [x for x in deck if x.team == "ManCity"]
    random.shuffle(deck)

    player1 = Player("Yeks")
    player2 = Player("Quan")

    for i in range(5):
        player1.drawCard(deck)
        player2.drawCard(deck)

    while(game.over == False):

        player1.printHand()
        player2.printHand()
        print(len(deck))
        game.over = True



runGame()

