from random import randint

SUIT_SET = ['♠', '♣', '♥', '♦']

NUMBER_SET = ['A', '2', '3', '4', '5', 
              '6', '7', '8', '9', '10', 
              'J', 'Q', 'K']

class Card:
    def __init__(self, suit, num):
        self.suit = suit
        if not isinstance(num, str):
            self.number = str(num)
        else:
            self.number = num
    
    def __str__(self):
        text_list = ['[']
        text_list.append(self.suit)
        text_list.append(self.number)
        text_list.append(']')
        return ''.join(text_list)
    

class Deck:
    def __init__(self):
        self.suits = {}
        for suit in SUIT_SET:
            self.suits[suit] = {}
    
    def initial_fill(self):
        for suit in self.suits:
            for i in range(13):
                self.suits[suit][NUMBER_SET[i]] = Card(suit, NUMBER_SET[i])

    def show_deck(self):
        text_list = ['[Deck]\n']
        for suit in self.suits:
            text_list.append(suit)
            text_list.append(': ')
            for card in self.suits[suit]:
                text_list.append(str(self.suits[suit][card]))
                text_list.append(' ')
            text_list.append('\n')
        print(''.join(text_list))
    
    def count_cards(self):
        total_card = 0
        for suit in self.suits:
            total_card += len(self.suits[suit])
        return total_card
    
    def get_random_card(self):
        card_cnt = self.count_cards()
        if card_cnt == 0:
            return None
        
        rand = randint(0, card_cnt-1)
        for suit in self.suits:
            if len(self.suits[suit]) < rand:
                rand -= len(self.suits[suit])
            else:
                for card in self.suits[suit]:
                    if rand == 0:
                        return self.suits[suit][card]
                    else:
                        rand -= 1
    
    def pop_card(self, card):
        if card.suit not in self.suits:
            raise Exception("Inappropriate suit : {}".format(card.suit))
        elif card.number not in self.suits[card.suit]:
            return None
        else:
            result = self.suits[card.suit][card.number]
            del self.suits[card.suit][card.number]
            return result
    
    def push_card(self, card):
        if card.suit not in self.suits:
            raise Exception("Inappropriate suit : {}".format(card.suit))
        elif card.number in self.suits[card.suit]:
            raise Exception("Already has {}{}".format(card.suit, card.number))
        else:
            self.suits[card.suit][card.number] = card


class Game:
    def __init__(self, player_num):
        self.dealer = Deck()
        self.dealer.initial_fill()
        self.players = [None] * player_num
        for i in range(player_num):
            self.players[i] = Deck()
    
    def show_game(self):
        print('<< Dealer >>')
        self.dealer.show_deck()
        for i in range(len(self.players)):
            print('<< Player {} >>'.format(i+1))
            self.players[i].show_deck()
    
    def give_away_cards(self, card_nums):
        for j in range(card_nums):
            for player in self.players:
                random_card = self.dealer.get_random_card()
                player.push_card(self.dealer.pop_card(random_card))


if __name__ == '__main__':
    G = Game(4)
    G.show_game()

    G.give_away_cards(5)
    G.show_game()