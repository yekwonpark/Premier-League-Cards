#!/usr/bin/env python
# coding: utf-8

# In[72]:


import random

class Game:
    def __init__(self):
        self.time = 0
        self.over = False
        self.p1turn = True
        self.deck = self.populate_deck("data.txt")

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

        return player1, player2

    def takeTurn(self, p1, p2):
        if self.p1turn == True:
            self.playCard(p1, p2)
        else:
            self.playCard(p2, p1)

    def playCard(self, firstp, secondp):
        i1 = -1
        firstp.printHand()
        while i1 > 5 or i1 < 0:
            i1 = int(input(firstp.name + "! Choose a player between 1-5: "))
            if i1 > 5 or i1 < 1:
                print("Invalid number, try again")
            i1 -= 1

        firstp.setPlayingCard(firstp.deck[i1])
        firstp.setCard(i1, self.deck.pop(0))
        print(firstp.name + " played: " + " %-22s %-20s %-13s %-15s" % (firstp.playingCard[0].name, "Team: " + firstp.playingCard[0].team, "Rating: " + str(firstp.playingCard[0].rating), "Rarity: " + firstp.playingCard[0].availability))


        i2 = -1
        secondp.printHand()
        while i2 > 5 or i2 < 0:
            i2 = int(input(secondp.name + "! Choose a player between 1-5: "))
            if i2 > 5 or i2 < 1:
                print("Invalid number, try again")
            i2 -= 1
    
        secondp.setPlayingCard(secondp.deck[i2])
        secondp.setCard(i2, self.deck.pop(0))
        print(secondp.name + " played: " + " %-22s %-20s %-13s %-15s" % (secondp.playingCard[0].name, "Team: " + secondp.playingCard[0].team, "Rating: " + str(secondp.playingCard[0].rating), "Rarity: " + secondp.playingCard[0].availability))


        self.war(firstp, secondp, i1, i2)

    def war(self, firstp, secondp, i1, i2):
        if firstp.playingCard[0].team == secondp.playingCard[0].team:
            self.penalties(firstp, secondp)
        else:
            self.rateCards(firstp, secondp, i1, i2)

    def penalties(self, p1, p2):
        print("Penalties!")
        p1score = 0
        p2score = 0

        # If doubled down
        if len(p1.playingCard) == 2:
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[2].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[2].name, "Rating: " + str(p1.playingCard[2].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[2].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[2].name, "Rating: " + str(p2.playingCard[2].rating), "Score: " + str(p2score)))
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[3].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[3].name, "Rating: " + str(p1.playingCard[3].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[3].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[3].name, "Rating: " + str(p2.playingCard[3].rating), "Score: " + str(p2score)))
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[4].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[4].name, "Rating: " + str(p1.playingCard[4].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[4].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[4].name, "Rating: " + str(p2.playingCard[4].rating), "Score: " + str(p2score)))

            # if tie
            if p1score == p2score:
                p1.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p2.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print("It's a tie!")

            # if p1 wins
            elif p1score > p2score:
                p1.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p1.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print(p1.name + " won!")
            else:
                p2.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p2.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print(p2.name + " won!")



        # If not doubled down
        else:
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[1].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[1].name, "Rating: " + str(p1.playingCard[1].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[1].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[1].name, "Rating: " + str(p2.playingCard[1].rating), "Score: " + str(p2score)))
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[2].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[2].name, "Rating: " + str(p1.playingCard[2].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[2].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[2].name, "Rating: " + str(p2.playingCard[2].rating), "Score: " + str(p2score)))
            p1.playingCard.append(self.deck.pop(0))
            p1score += p1.playingCard[3].rating
            print(p1.name + " got: " + " %-22s %-20s %-13s" % (p1.playingCard[3].name, "Rating: " + str(p1.playingCard[3].rating), "Score: " + str(p1score)))
            p2.playingCard.append(self.deck.pop(0))
            p2score += p2.playingCard[3].rating
            print(p2.name + " got: " + " %-22s %-20s %-13s" % (p2.playingCard[3].name, "Rating: " + str(p2.playingCard[3].rating), "Score: " + str(p2score)))

            # if tie
            if p1score == p2score:
                p1.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p2.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print("It's a tie!")

            # if p1 wins
            elif p1score > p2score:
                p1.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p1.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print(p1.name + " won!")
            else:
                p2.cardsWon.extend(p1.playingCard)
                p1.nullPlayingCard()
                p2.cardsWon.extend(p2.playingCard)
                p2.nullPlayingCard()
                print(p2.name + " won!")

    def rateCards(self, firstp, secondp, i1, i2):
        if firstp.playingCard[0].rating == secondp.playingCard[0].rating:
            self.penalties(firstp, secondp)
        elif firstp.playingCard[0].rating > secondp.playingCard[0].rating:
            firstp.cardsWon.append(firstp.playingCard[0])
            firstp.nullPlayingCard()
            firstp.cardsWon.append(secondp.playingCard[0])
            secondp.nullPlayingCard()
            print(firstp.name + " won!")
        else:
            # double up
            dodouble = False
            for p in firstp.deck:
                if p.team == firstp.playingCard[0].team:
                    dodouble = True
            if dodouble:
                self.doubleDown(firstp, secondp)
            else:
                secondp.cardsWon.append(firstp.playingCard[0])
                firstp.nullPlayingCard()
                secondp.cardsWon.append(secondp.playingCard[0])
                secondp.nullPlayingCard()
                print(secondp.name + " won!")

    def doubleDown(self, p1, p2):
        indices = p1.printHand(p1.playingCard[0].team)
        x = "x"
        while x not in indices and x != "p":
            x = input("Enter [p] to pass: ")

            if x != "p":
                x = int(x)

            if x not in indices and x != "p":
                print("Invalid input, try again")

        if x == "p":
            p2.cardsWon.append(p1.playingCard[0])
            p1.nullPlayingCard()
            p2.cardsWon.append(p2.playingCard[0])
            p2.nullPlayingCard()
            print(p2.name + " won!")
        else: 
            x -= 1
            p1.setPlayingCard(p1.deck[x])
            p1.setCard(x, self.deck.pop(0))
            print(p1.name + " played: " + " %-22s %-20s %-13s %-15s" % (p1.playingCard[1].name, "Team: " + p1.playingCard[1].team, "Rating: " + str(p1.playingCard[1].rating), "Rarity: " + p1.playingCard[1].availability))
            dodouble = False
            for p in p2.deck:
                if p.team == p2.playingCard[0].team:
                    dodouble = True
            if dodouble:
                indices = p2.printHand(p2.playingCard[0].team)
                x = "x"
                while x not in indices and x != "p":
                    x = input("Enter [p] to pass: ")
                    if x not in indices and x != "p":
                        print("Invalid input, try again")

                if x == "p":
                    p1.cardsWon.append(p1.playingCard[0])
                    p1.nullPlayingCard()
                    p1.cardsWon.append(p2.playingCard[0])
                    p2.nullPlayingCard()
                    print(p1.name + " won!")
                else: 
                    p2.setPlayingCard(p2.deck[x])
                    p2.setCard(x, self.deck.pop(0))
                    print(p2.name + " played: " + " %-22s %-20s %-13s %-15s" % (p2.playingCard[1].name, "Team: " + p2.playingCard[1].team, "Rating: " + str(p2.playingCard[1].rating), "Rarity: " + p2.playingCard[1].availability))
                    p1sum = p1.deck[0].rating + p1.deck[1].rating
                    p2sum = p2.deck[0].rating + p2.deck[2].rating

                    # if tie
                    if p1sum == p2sum:
                        self.penalties(p1, p2)
                    elif p1sum > p2sum:
                        p1.cardsWon.append(p1.playingCard[0])
                        p1.cardsWon.append(p1.playingCard[1])
                        p1.nullPlayingCard()
                        p1.cardsWon.append(p2.playingCard[0])
                        p1.cardsWon.append(p2.playingCard[1])
                        p2.nullPlayingCard()
                        print(p1.name + " won!")
                    else:
                        p2.cardsWon.append(p1.playingCard[0])
                        p2.cardsWon.append(p1.playingCard[1])
                        p1.nullPlayingCard()
                        p2.cardsWon.append(p2.playingCard[0])
                        p2.cardsWon.append(p2.playingCard[1])
                        p2.nullPlayingCard()
                        print(p2.name + " won!")

                    


            else:
                p1.cardsWon.append(p1.playingCard[0])
                p1.cardsWon.append(p1.playingCard[1])
                p1.nullPlayingCard()
                p1.cardsWon.append(p2.playingCard[0])
                p2.nullPlayingCard()
                print(p1.name + " won!")






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
        self.cardsWon = []
        self.playingCard = []

    def drawCard(self, deck, index):
        self.deck.insert(index, deck.pop(0))

    def setCard(self, index, card):
        self.deck[index] = card

    def setPlayingCard(self, card):
        self.playingCard.append(card)

    def nullPlayingCard(self):
        self.playingCard = []

    # two arguments for doubledown printhand
    def printHand(self, team = None):
        # if one argument
        if team == None:
            print(self.name + "'s hand: ")
            for i in range(len(self.deck)):
                selector = i + 1
                sentence = "[" + str(selector) + "] to play this player"
                print(" %-22s %-20s %-13s %-15s" % (self.deck[i].name, "Team: " + self.deck[i].team, "Rating: " + str(self.deck[i].rating), "Rarity: " + self.deck[i].availability), sentence)
        else:
            indices = []
            print(self.name + "'s hand: ")
            for i in range(len(self.deck)):
                selector = i + 1
                sentence = "[" + str(selector) + "] to play this player"
                if self.deck[i].team == team:
                    indices.append(selector)
                    print(" %-22s %-20s %-13s %-15s" % (self.deck[i].name, "Team: " + self.deck[i].team, "Rating: " + str(self.deck[i].rating), "Rarity: " + self.deck[i].availability), sentence)
                else:
                    print(" %-22s %-20s %-13s %-15s" % (self.deck[i].name, "Team: " + self.deck[i].team, "Rating: " + str(self.deck[i].rating), "Rarity: " + self.deck[i].availability))

            return indices

        
    
    





        

def runGame():
    game = Game()

    #newdeck = [x for x in deck if x.team == "ManCity"]
    random.shuffle(game.deck)

    p1, p2 = game.generate_players()

    # Setup - each draw 5 cards
    for i in range(5):
        p1.drawCard(game.deck, 0)
        p2.drawCard(game.deck, 0)

    while(game.over == False):
        print("Time: " + str(game.time) + ":00")
        print(p1.name + "'s cards won: " + str(len(p1.cardsWon)) + "\t" + p2.name + "'s cards won: " + str(len(p2.cardsWon)))

        game.takeTurn(p1, p2)
        game.p1turn = not game.p1turn
        game.time += 5
        if (game.time == 90):
            game.over = True

    print("Game Over!")

runGame()

