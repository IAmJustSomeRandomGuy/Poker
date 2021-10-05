class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


ace_c = Card("clubs", 14)
two_c = Card("clubs", 2)
three_c = Card("clubs", 3)
four_c = Card("clubs", 4)
five_c = Card("clubs", 5)
six_c = Card("clubs", 6)
seven_c = Card("clubs", 7)
eight_c = Card("clubs", 8)
nine_c = Card("clubs", 9)
ten_c = Card("clubs", 10)
jack_c = Card("clubs", 11)
queen_c = Card("clubs", 12)
king_c = Card("clubs", 13)

ace_d = Card("diamonds", 14)
two_d = Card("diamonds", 2)
three_d = Card("diamonds", 3)
four_d = Card("diamonds", 4)
five_d = Card("diamonds", 5)
six_d = Card("diamonds", 6)
seven_d = Card("diamonds", 7)
eight_d = Card("diamonds", 8)
nine_d = Card("diamonds", 9)
ten_d = Card("diamonds", 10)
jack_d = Card("diamonds", 11)
queen_d = Card("diamonds", 12)
king_d = Card("diamonds", 13)

ace_s = Card("spades", 14)
two_s = Card("spades", 2)
three_s = Card("spades", 3)
four_s = Card("spades", 4)
five_s = Card("spades", 5)
six_s = Card("spades", 6)
seven_s = Card("spades", 7)
eight_s = Card("spades", 8)
nine_s = Card("spades", 9)
ten_s = Card("spades", 10)
jack_s = Card("spades", 11)
queen_s = Card("spades", 12)
king_s = Card("spades", 13)

ace_h = Card("hearts", 14)
two_h = Card("hearts", 2)
three_h = Card("hearts", 3)
four_h = Card("hearts", 4)
five_h = Card("hearts", 5)
six_h = Card("hearts", 6)
seven_h = Card("hearts", 7)
eight_h = Card("hearts", 8)
nine_h = Card("hearts", 9)
ten_h = Card("hearts", 10)
jack_h = Card("hearts", 11)
queen_h = Card("hearts", 12)
king_h = Card("hearts", 13)

# I could have used nums instead of words and the looking for indexes
deck = [
    ace_c, two_c, three_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c,
    ace_d, two_d, three_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d,
    ace_s, two_s, three_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s,
    ace_h, two_h, three_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h
]
deck1 = ['ace of clubs (A♣)', 'two of clubs (2♣)', 'three of clubs (3♣)', 'four of clubs (4♣)',
         'five of clubs (5♣)', 'six of clubs (6♣)', 'seven of clubs (7♣)', 'eight of clubs (8♣)',
         'nine of clubs (9♣)', 'ten of clubs (10♣)', 'jack of clubs (J♣)', 'queen of clubs (Q♣)',
         'king of clubs (K♣)', 'ace of diamonds (A♦)', 'two of diamonds (2♦)', 'three of diamonds (3♦)',
         'four of diamonds (4♦)', 'five of diamonds (5♦)', 'six of diamonds (6♦)', 'seven of diamonds (7♦)',
         'eight of diamonds (8♦)', 'nine of diamonds (9♦)', 'ten of diamonds (10♦)', 'jack of diamonds (J♦)',
         'queen of diamonds (Q♦)', 'king of diamonds (K♦)', 'ace of spades (A♠)', 'two of spades (2♠)',
         'three of spades (3♠)', 'four of spades (4♠)', 'five of spades (5♠)', 'six of spades (6♠)',
         'seven of spades (7♠)', 'eight of spades (8♠)', 'nine of spades (9♠)', 'ten of spades (10♠)',
         'jack of spades (J♠)', 'queen of spades (Q♠)', 'king of spades (K♠)', 'ace of hearts (A♥)',
         'two of hearts (2♥)', 'three of hearts (3♥)', 'four of hearts (4♥)', 'five of hearts (5♥)',
         'six of hearts (6♥)', 'seven of hearts (7♥)', 'eight of hearts (8♥)', 'nine of hearts (9♥)',
         'ten of hearts (10♥)', 'jack of hearts (J♥)', 'queen of hearts (Q♥)', 'king of hearts (K♥)',
         ]
deck2 = ['ace of clubs (A♣)', 'two of clubs (2♣)', 'three of clubs (3♣)', 'four of clubs (4♣)',
         'five of clubs (5♣)', 'six of clubs (6♣)', 'seven of clubs (7♣)', 'eight of clubs (8♣)',
         'nine of clubs (9♣)', 'ten of clubs (10♣)', 'jack of clubs (J♣)', 'queen of clubs (Q♣)',
         'king of clubs (K♣)', 'ace of diamonds (A♦)', 'two of diamonds (2♦)', 'three of diamonds (3♦)',
         'four of diamonds (4♦)', 'five of diamonds (5♦)', 'six of diamonds (6♦)', 'seven of diamonds (7♦)',
         'eight of diamonds (8♦)', 'nine of diamonds (9♦)', 'ten of diamonds (10♦)', 'jack of diamonds (J♦)',
         'queen of diamonds (Q♦)', 'king of diamonds (K♦)', 'ace of spades (A♠)', 'two of spades (2♠)',
         'three of spades (3♠)', 'four of spades (4♠)', 'five of spades (5♠)', 'six of spades (6♠)',
         'seven of spades (7♠)', 'eight of spades (8♠)', 'nine of spades (9♠)', 'ten of spades (10♠)',
         'jack of spades (J♠)', 'queen of spades (Q♠)', 'king of spades (K♠)', 'ace of hearts (A♥)',
         'two of hearts (2♥)', 'three of hearts (3♥)', 'four of hearts (4♥)', 'five of hearts (5♥)',
         'six of hearts (6♥)', 'seven of hearts (7♥)', 'eight of hearts (8♥)', 'nine of hearts (9♥)',
         'ten of hearts (10♥)', 'jack of hearts (J♥)', 'queen of hearts (Q♥)', 'king of hearts (K♥)',
         ]

# Not needed so far
clubs = [ace_c, two_c, three_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c]
diamonds = [ace_d, two_d, three_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_d, queen_d, king_d]
spades = [ace_s, two_s, three_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s]
hearts = [ace_h, two_h, three_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h]
