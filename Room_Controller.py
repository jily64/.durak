import random
cards = 8
card_marks = ["Бубен", "Червей", "Крестей", "Пик"]

class Room:
    def __init__(self, creator_id=None, max_users=1, deck=None, room_id=None):
        self.creator = creator_id
        self.max_users = max_users
        self.wait = True
        self.users = [creator_id, "sdsds"]
        self.deck = []
        self.user_data = {}
        self.koz = None
        self.cards_on_board = []

        for i in card_marks:
            for j in range(cards):
                self.deck.append([i, 6 + j, False])
                #print(str([6 + j, i]) + ",")
        random.shuffle(self.deck)


        self.id = room_id

    def start_game(self):
        if len(self.users) >=self.max_users:
            for i in self.users:
                user_hand = []
                for j in range(7):
                    rand = random.randint(0, len(self.deck)-1)
                    user_hand.append(self.deck[rand])
                    self.deck.pop(rand)
                self.user_data[i] = {
                    "in_hand": user_hand
                }
                print(user_hand)
            rand = random.randint(0, len(self.deck)-1)
            self.deck[rand][2] = True
            self.koz = self.deck[rand]
            self.deck.pop(rand)
            self.deck.append(self.koz)
            self.curr_user_send = random.randint(0, len(self.users)-1)
            if self.curr_user_send == len(self.users)-1:
                self.curr_user_get = 0
            else:
                self.curr_user_get = self.curr_user_send+1


        else:
            return False


    def on_user_connect(self, user_id):
        if len(self.users) < self.max_users:
            self.users.append(user_id)
            return True
        else:
            return "Room Is Full"

    def on_user_remove(self, user_id):
        self.users.pop(user_id)
        if len(self.users) == 0:
            return "Delete"
        else:
            return True

    def send_card(self, user, card):
        if len(self.cards_on_board) < 5:
            self.cards_on_board.append(card)

