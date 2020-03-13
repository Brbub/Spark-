class cards():
    def  __init__(self, hand1, hand2):
        self.hand1 = hand1
        self.hand2 = hand2

    def cmp(self,x, y):
        return (x > y) - (x < y)

    def ranking(self, hand1, hand2):
        hand1.sort()
        hand2.sort()

    def highest_card(self, hand1, hand2):
        for i in range(7):    
            if self.cmp(hand1[-i], hand2[-i]) == 1:
                return(hand2)
            elif self.cmp(hand1[-i], hand2[-i]) == -1:
                return(hand1)
            else:
                pass
    def main(self):
        self.ranking(self.hand1, self.hand2)
        print(self.highest_card(self.hand1, self.hand2))






hand1 = [1,5,5,6,9,13,14]
hand2 = [2,2,3,10,10,13,14]

cards(hand1, hand2).main()