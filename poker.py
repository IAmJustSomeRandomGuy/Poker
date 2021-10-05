import random
import cards

p1_bal = 500
p2_bal = 500

in_game = True

blind = random.choice(range(2))

while in_game:
    player1 = []
    player1 = list(map(int, player1))
    player2 = []
    player2 = list(map(int, player2))
    p1 = []
    p2 = []
    table = []
    table = list(map(int, table))
    burned = []
    bet_pool = 0
    p1_call = True
    p2_call = True
    p1_raise = True
    p2_raise = True
    p1_folded = False
    p2_folded = False
    winner = None
    deck3 = cards.deck2.copy()
    fast_mode = False


    def drawn(drew):
        deck3.remove(drew)


    def draw(who=None):
        if who is None:
            who = burned
        card = random.choice(deck3)
        drawn(card)
        who.append(cards.deck1.index(card))


    def check_winner(player, score, name):

        global color_counter, dup2, straight_abc
        score.clear()

        club_counter = list()
        club_counter = list(map(int, club_counter))
        diamond_counter = list()
        diamond_counter = list(map(int, diamond_counter))
        spade_counter = list()
        spade_counter = list(map(int, spade_counter))
        heart_counter = list()
        heart_counter = list(map(int, heart_counter))
        card_nums = list()
        card_nums = list(map(int, card_nums))

        cheats = [0, 2, 1, 4, 5, 6, 8]

        for x in cheats:
            y = cards.deck[x]
            if y.suit == "clubs":
                club_counter.append(cards.deck.index(y))
            elif y.suit == "diamonds":
                diamond_counter.append(cards.deck.index(y))
            elif y.suit == "spades":
                spade_counter.append(cards.deck.index(y))
            elif y.suit == "hearts":
                heart_counter.append(cards.deck.index(y))
            card_nums.append(y.number)
        card_nums.sort()
        card_nums2 = list(set(card_nums.copy()))
        print(card_nums2)

        a1 = False
        b1 = False
        c1 = False
        d1 = False
        a = None
        b = None
        c = None
        d = None

        if len(card_nums2) >= 5:
            a1 = True
            a = card_nums2[0:5].copy()
            if 2 in card_nums2 and 14:
                d = a.copy()
                d.insert(0, 1)
                d.pop()
                d1 = True
        if len(card_nums2) >= 6:
            b1 = True
            b = card_nums2[1:6].copy()
        if len(card_nums2) >= 7:
            c1 = True
            c = card_nums2[2:7].copy()

        color = False
        straight = False

        if len(club_counter) >= 5:
            color = True
            color_counter = club_counter
        if len(diamond_counter) >= 5:
            color = True
            color_counter = diamond_counter
        if len(spade_counter) >= 5:
            color = True
            color_counter = spade_counter
        if len(heart_counter) >= 5:
            color = True
            color_counter = heart_counter

        if d1 and d == list(range(min(d), max(d) + 1)) and len(d) != 1:
            straight = True
            straight_abc = d
        if a1 and a == list(range(min(a), max(a) + 1)) and len(a) != 1:
            straight = True
            straight_abc = a
        if b1 and b == list(range(min(b), max(b) + 1)) and len(b) != 1:
            straight = True
            straight_abc = b
        if c1 and c == list(range(min(c), max(c) + 1)) and len(c) != 1:
            straight = True
            straight_abc = c

        straight_flushd = 0
        if d is not None:
            if color and straight is True:
                for x in color_counter:
                    if cards.deck[x].number in d:
                        straight_flushd += 1
                        if straight_flushd == 5:
                            straight_abc = d
        straight_flusha = 0
        if a is not None:
            if color and straight is True:
                for x in color_counter:
                    if cards.deck[x].number in a:
                        straight_flusha += 1
                        if straight_flusha == 5:
                            straight_abc = a
        straight_flushb = 0
        if b is not None:
            if color and straight is True:
                for x in color_counter:
                    if cards.deck[x].number in b:
                        straight_flushb += 1
                        if straight_flushb == 5:
                            straight_abc = b
        straight_flushc = 0
        if c is not None:
            if color and straight is True:
                for x in color_counter:
                    if cards.deck[x].number in c:
                        straight_flushc += 1
                        if straight_flushc == 5:
                            straight_abc = c

        dup = list()
        dups = list()
        for x in card_nums2:
            dup.append(card_nums.count(x))
        dup = list(map(int, dup))

        for x in range(len(card_nums2)):
            if dup[x] >= 2:
                dups.append(card_nums2[x])
        dups = list(map(int, dups))

        for x in range(len(dup)):
            if 1 in dup:
                dup.remove(1)

        dup1 = dup.copy()
        if dup1.count(2) >= 1:
            dup2 = [dups[dup1.index(2)]]
        if dup1.count(2) == 2:
            dup2.append(dups[dup1.index(2, dup1.index(2) + 1, 3)])
        dup.append(1)
        dup.sort(reverse=True)

        if 'dup2' not in locals():
            if len(dups) > 1:
                dups.sort(reverse=True)
                dup2 = [dups[1]]
        if 'dup2' in locals():
            dup2.sort(reverse=True)
        if len(dup) == 0:
            dup = [1, 1]

        card_nums.sort(reverse=True)

        if straight_flusha == 5 or straight_flushb == 5 or straight_flushc == 5 or straight_flushd == 5:
            print(name + ' got a straight flush')
            score += [8, straight_abc[4]]
        elif dup[0] == 4:
            print(name + ' got four of a kind')
            score += [7, dups[dup1.index(4)]]
            card_nums3 = [x for x in card_nums2 if x not in dups]
            for x in range(1):
                score += [card_nums3[x]]
        elif dup[0] == 3 and dup[1] >= 2:
            print(name + ' got a full house')
            score += [6, dups[dup1.index(3)], dup2[0]]
        elif color:
            print(name + ' got a flush')
            color_counter.sort(reverse=True)
            score += [5]
            score += color_counter[:5]
        elif straight:
            print(name + ' got a straight')
            score += [4, straight_abc[4]]
        elif dup[0] == 3:
            print(name + ' got three of a kind')
            score += [3, dups[0]]
            card_nums3 = [x for x in card_nums2 if x not in dups]
            for x in range(2):
                score += [card_nums3[x]]
        elif dup[0] == 2 and dup[1] == 2:
            dups.sort(reverse=True)
            print(name + ' got two pairs')
            score += [2, dups[0], dups[1]]
            card_nums3 = [x for x in card_nums2 if x not in dups]
            for x in range(1):
                score += [card_nums3[x]]
        elif dup[0] == 2:
            print(name + ' got a pair')
            score += [1, dups[0]]
            card_nums3 = [x for x in card_nums2 if x not in dups]
            for x in range(3):
                score += [card_nums3[x]]
        else:
            print(name + ' got a high card')
            score += [0]
            for x in range(5):
                score += [card_nums[x]]

        print(score)
        print('')


    def betting(player):
        global p1_bal, bet_pool, bet, p2_bal, p1_folded, winner, other_player, player_calls
        if not fast_mode:
            if player == p1_bal:
                other_player = p2_bal
                player_calls = p2_call
            if player == p2_bal:
                other_player = p1_bal
                player_calls = p1_call
            if not p1_folded and not p2_folded:
                print('')
                while True:
                    bet = ''
                    print("Your chips: " + str(player))
                    print("Your Opponents chips: " + str(other_player))
                    try:
                        bet = int(input("How much would you like to bet? "))
                        print("")
                    except ValueError:
                        print('Put a number from 0 to ' + str(player))
                    if isinstance(bet, int):
                        if 0 <= bet <= player and bet <= other_player:
                            break

                if player_calls:
                    p1_bal = p1_bal - bet
                    p2_bal = p2_bal - bet
                    bet_pool += bet * 2
                print("Your chips: " + str(player))
                print("Bet pool: " + str(bet_pool))
                print('')
            else:
                if p1_folded:
                    winner = player2
                elif p2_folded:
                    winner = player1
                else:
                    die = 0 / 0


    draw(player1)
    draw(player1)

    print('You have drawn the ' + cards.deck1[player1[0]] + ' and the ' + cards.deck1[player1[1]])

    if blind % 2 == 0:
        print('You are the big blind')
        p1_bal = p1_bal - 50
        p2_bal = p2_bal - 25
        bet_pool += 75
        while True:
            if p2_call:
                p2_bal = p2_bal - 25
                bet_pool += 25
                break
            elif not p2_call:
                p2_folded = True
                break
    elif blind % 2 == 1:
        print('You are the small blind')
        p2_bal = p2_bal - 50
        p1_bal = p1_bal - 25
        bet_pool += 75
        while True:
            p1_call = input('Do you want to call the ante? ').lower()
            if p1_call == 'yes' or p1_call == 'y':
                p1_bal = p1_bal - 25
                bet_pool += 25
                break
            elif p1_call == 'no' or p1_call == 'n':
                p1_folded = True
                break

    else:
        die = 0 / 0

    draw(player2)
    draw(player2)

    betting(p1_bal)

    draw()

    draw(table)
    draw(table)
    draw(table)

    draw()

    draw(table)

    draw()

    draw(table)

    print('Table:')
    for i in range(len(table) - 2):
        print(' ' + cards.deck1[table[i]])

    betting(p1_bal)

    print(' ' + cards.deck1[table[3]])

    betting(p1_bal)

    print(' ' + cards.deck1[table[4]])

    betting(p1_bal)

    print('You:')
    for i in range(len(player1)):
        print(' ' + cards.deck1[player1[i]])
    print('')
    print('Opponent:')
    for i in range(len(player2)):
        print(' ' + cards.deck1[player2[i]])
    print('')

    check_winner(player1, p1, 'You')
    check_winner(player2, p2, 'Opponent')

    if winner is None:
        for x in range(min([len(p1), len(p2)])):
            if p1[x] > p2[x]:
                winner = player1
                break
            elif p2[x] > p1[x]:
                winner = player2
                break
        if p1 == p2:
            winner = [player1, player2]
        else:
            die = 0 / 0

    if winner == player1:
        print('You win')
        p1_bal += bet_pool
    elif winner == player2:
        print('Opponent wins')
        p2_bal += bet_pool
    elif winner == [player1, player2]:
        print("It's a tie")
        p1_bal += int(bet_pool / 2)
        p2_bal += int(bet_pool / 2)

    print('')

    print('Your chips: ' + str(p1_bal))
    print('Opponents chips: ' + str(p2_bal))

    if p1_bal == 0:
        print('Opponent won')
        print('')
        break

    if p2_bal == 0:
        print('You won')
        print('')
        break

    print('')
    print('')
    print('')
    blind += 1

esc = ''
while esc != 'exit':
    esc = input('If you want to leave type exit ')

# todo: 1) high card
# todo: 2) ai
# todo: 3) add player_hand to the end of the score
