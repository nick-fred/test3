class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["梅花", "方块", "红桃", "黑桃"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand():
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        for card in self.cards:
            rep += str(card) + "\t"
        return rep

    def add(self, card):
        self.cards.append(card)

    def remove(self):
        self.cards.remove(card)


class Poker(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print("牌发完了")


if __name__ == "__main__":
    print("开始发牌。。。。")
    plays = [Hand(), Hand(), Hand(), Hand()]
    poker = Poker()
    poker.populate()
    poker.shuffle()
    poker.deal(plays, 13)
    n = 1
    for hand in plays:
        print("牌手", n, end=":")
        print(hand)
        n = n + 1
    input("\n 结束 按enter 键 离开")