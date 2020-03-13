import random
#diamond = "d"
#spade = "s"
#heart="h"
#club="c"
"""
Things I need to implement:
    Card ranking to check which hand would win and give the pot to the coresponding player
    If every player has folded then the player left wins and give the pot to the coresponding player
    Fix a method for all in
    Make it that after everyone has bet and you already payed x amount by raising that when you check it doesn't make you pay more
    Add an option to either just play one game/round or go until people run out of money
    ***Train an Ai dataset by making them play against each other***
    ***Make Visual representation and be able to play agaisnt the best Ai***

"""
class Player():
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name


players = [Player(10000,"Bob"), Player(10000,"Tom"), Player(10000,"Tim")]


class TexasHoldem():
    def __init__(self, players):
        self.folded_players = []
        self.amount_of_players = 0
        self.pot = 0
        self.curbet = 0
        self.turns = 0
        self.dealer = None
        self.small_blind = None
        self.big_blind = None
        self.last_turn = None
        self.players = {}
        self.amounts = {}
        self.player_cards = {}
        self.blinds = {}
        self.cardslist = ['2d', '2s', '2h', '2c', '3d', '3s', '3h', '3c', '4d', '4s', '4h', '4c', '5d', '5s', '5h', '5c', '6d', '6s', '6h', '6c', '7d', '7s', '7h', '7c', '8d', '8s', '8h', '8c', '9d', '9s', '9h', '9c', '10d', '10s', '10h', '10c', 'Jd', 'Js', 'Jh', 'Jc', 'Qd', 'Qs', 'Qh', 'Qc', 'Kd', 'Ks', 'Kh', 'Kc', 'Ad', 'As', 'Ah', 'Ac']
        self.newdeck = self.shuffle(self.cardslist)
        self.cards = []
        self.deck = False
        self.game = True
        self.first_turn = True
        for i in players:
            self.amount_of_players += 1
            self.players["Player{0}".format(self.amount_of_players)] = i.name
            self.amounts["Player{0}".format(self.amount_of_players)] = i.amount
            
        
        if self.first_turn == True:
            for key in self.players:
                self.deal(key)
            if self.amount_of_players == 2:
                self.dealer = self.players['Player1']
                self.small_blind = self.players['Player1']
                self.big_blind = self.players['Player2']
            else:
                self.small_blind = self.players['Player1']
                self.big_blind = self.players['Player2']
    
        
        
    
    
    
    def shuffle(self, cards):
        random.shuffle(cards)
        return cards
    
    def deal(self, whom):
        cards = []
        for i in self.newdeck:
            cards.append(i)
            self.newdeck.remove(i)
            break
        for i in self.newdeck:
            cards.append(i)
            self.newdeck.remove(i)
            break
        self.player_cards[whom] = cards 
    
    def turn(self, whoseturn):
        for i in self.folded_players:
            if whoseturn == i:
                print("You Folded")
                return
        
        
        if (self.turns % 4) == 3:
            self.curbet = 0
            if len(self.cards) == 5:
                self.game = False
            
            if len(self.cards) == 4:
                j = 0
                for i in self.newdeck:
                    if j == 1:
                        break
                    self.cards.append(i)
                    self.newdeck.remove(i)
                    j+= 1
                self.turns = 0

            if len(self.cards) == 3:
                j = 0
                for i in self.newdeck:
                    if j == 1:
                        break
                    self.cards.append(i)
                    self.newdeck.remove(i)
                    j+= 1
                self.turns = 0

            if len(self.cards) == 0:
                j = 0
                for i in self.newdeck:
                    if j == 3:
                        break
                    self.cards.append(i)
                    self.newdeck.remove(i)
                    j+= 1
                self.turns = 0
            
            
            
            
#switch order or break after each



        
        self.print_screen(whoseturn)
        if self.first_turn == True:
            if self.players[whoseturn] == self.small_blind:
                self.bet(whoseturn, 100)
                #self.curbet == 100
                self.first_turn = True
            elif self.players[whoseturn] == self.big_blind:
                self.bet(whoseturn, 200)
                self.first_turn = False
                self.curbet += 200
        else:
            action = input("What Do You Want To Do?(check, raise, fold)")
            if action.lower() == 'check':
                if self.curbet < self.amounts[whoseturn]:
                    self.bet(whoseturn, self.curbet)
                    self.turns += 1

                else:
                    print("You only have:" , self.amounts[whoseturn])

            if action.lower() == 'raise':
                x = input("Enter An Amount You Want To Raise:")
                if (self.curbet + int(x)) < self.amounts[whoseturn]:
                    self.bet(whoseturn, self.curbet + int(x))
                    self.curbet += int(x)
                    self.turns = 0
                else:
                    print("You only have:" , self.amounts[whoseturn])

            if action.lower() == 'fold':
                self.folded_players.append(whoseturn)
                self.turns += 1

        print(self.turns)
        self.check()
        self.last_turn == whoseturn
            
    
    def check(self):
        #Ace High; 2 pair; Three pair; straight; Flush; Full House; Four of a kind; Straight Flush; Royal Flush
        if self.folded_players == self.amount_of_players - 1:
            for i in self.players:
                if i != self.folded_players:
                    self.amounts[i] += self.pot
                    self.pot = 0


    def final(self):
        #for i in player
        pass


    def print_screen(self, whoseturn):
        print("\n","CARDS:",self.cards)
        print("\n")
        print(whoseturn, "\n","Pot:",self.pot)
        print("\n")
        print(self.player_cards[whoseturn])
        print("\n")
    
    
    
    def bet(self, whom, amount):
        self.amounts[whom] -= amount
        self.pot += amount
    
    
    
    def main(self):
        #print(self.amount_of_players, self.players, self.amounts)
        while self.game == True:   
            for key in self.players:
                self.turn(key) 
        
        #print(self.amounts)
        
        #print(self.player_cards)
        



if __name__ == "__main__":
    TexasHoldem(players).main()