import random
import sys


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12

        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        for i in range(len(self.all_hands)):
            points, hand_string = self.is_royal(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_straight_flush(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_four_kind(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_full_house(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_flush(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_straight(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_three_kind(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_two_pair(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_one_pair(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)
            points, hand_string = self.is_high_card(self.all_hands[i])
            if points != 0:
                hand_points.append(points)
                hand_type.append(hand_string)
                print('Player ' + str(i + 1) + ' : ' + hand_string)

        # determine winner and print

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and hand[i].suit == hand[i + 1].suit

        if not same_suit:
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and hand[i].rank == 14 - i

        if not rank_order:
            return 0, ''

        points = 10 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Royal Flush'

    # Determine if a hand is a straight flush
    def is_straight_flush(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and hand[i].suit == hand[i + 1].suit

        if not same_suit:
            return 0, ''

        rank_order = True
        for i in range(len(hand) - 1):
            rank_order = rank_order and hand[i].rank == hand[i + 1].rank + 1

        if not rank_order:
            return 0, ''

        points = 9 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Straight Flush'

    # Determine if a hand is four of a kind
    def is_four_kind(self, hand):
        count = 0

        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                count += 1

        # I'm assuming the loop is checking the condition a total of
        # 4 times. Thus the amount of positive checks should be 3
        if count != 3:
            return 0, ''

        points = 8 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Four of a Kind'

    # Determine if a hand is a full house
    def is_full_house(self, hand):
        count_dict = {}

        for i in range(len(hand)):
            # add 1 to the value if the key already exists
            if hand[i].rank in count_dict:
                count_dict[hand[i].rank] += 1
            # otherwise add the key value pair
            else:
                count_dict[hand[i].rank] = 1

        if len(count_dict) != 2 or 1 in count_dict.values():
            return 0, ''

        # check if the 3 pair is sorted at the beginning of the hand
        if count_dict[hand[0].rank] == 3:
            points = 7 * 15 ** 5 + hand[0].rank * 15 ** 4 + \
                     hand[1].rank * 15 ** 3
            points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
            points = points + hand[4].rank
            return points, 'Full House'
        # check if the 3 pair is at the end of the hand
        elif count_dict[hand[0].rank] == 2:
            points = 7 * 15 ** 5 + hand[4].rank * 15 ** 4 + \
                     hand[3].rank * 15 ** 3
            points = points + hand[2].rank * 15 ** 2 + hand[1].rank * 15
            points = points + hand[0].rank
            return points, 'Full House'

    # Determine if a hand is a flush
    def is_flush(self, hand):
        same_suit = True
        # check if the hand has the same suits
        for i in range(len(hand) - 1):
            same_suit = same_suit and hand[i].suit == hand[i + 1].suit

        if not same_suit:
            return 0, ''

        points = 6 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Flush'

    # Determine if a hand is straight
    def is_straight(self, hand):
        rank_order = True
        # check if the hand is in ascending order
        for i in range(len(hand) - 1):
            rank_order = rank_order and hand[i].rank == hand[i + 1].rank + 1

        if not rank_order:
            return 0, ''

        points = 5 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Straight'

    # Determine if a hand is three of a kind
    def is_three_kind(self, hand):
        count = 0

        # The loop should only make comparisons around 3 times
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                count += 1

        if count != 2:
            return 0, ''

        points = 4 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Three of a Kind'

    # Determine if a hand has a 2 pairs of cards
    def is_two_pair(self, hand):
        count = 0
        # count how many times a pair shows up in the hand
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                count += 1

        if count != 2:
            return 0, ''

        points = 3 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'Two Pair'

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):
        one_pair = False
        pair = []
        non_pair = []
        pair_index = 0

        for i in range(len(hand) - 1):
            # if current card matches the next card add it to pair
            if hand[i].rank == hand[i + 1].rank:
                pair += str(hand[i].rank)
                pair += str(hand[i + 1].rank)
                one_pair = True
                pair_index = i
            # otherwise if there is no pair at index 3 add 3 and 4 to
            # non_pair index list
            elif i == 3:
                non_pair += str(i)
                non_pair += str(i + 1)
            # add index to non_pair list
            else:
                non_pair += str(i)

            # If the rank is the same as the previous card, remove it
            # from the non pair list
            if hand[i].rank == hand[i - 1].rank:
                non_pair.remove(str(i))

        if not one_pair:
            return 0, ''

        points = 2 * 15 ** 5 + hand[pair_index].rank * 15 ** 4 + \
            hand[pair_index + 1].rank * 15 ** 3
        points = points + hand[int(non_pair[0])].rank * 15 ** 2 + \
            hand[int(non_pair[1])].rank * 15
        points = points + hand[int(non_pair[2])].rank

        return points, 'One Pair'

    # Determine if a hand is a high card
    def is_high_card(self, hand):

        points = 1 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15
        points = points + hand[4].rank

        return points, 'High Card'


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()


if __name__ == "__main__":
    main()
