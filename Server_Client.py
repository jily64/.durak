import asyncio
import random

rooms = []
deck = []
cards = 8
card_marks = ["Бубен", "Червей", "Крестей", "Пик"]


class Room_Controller:

    def catch_command(self, message):
        a = message.split(" ")
        if a[0] == "create_room":
            for i in card_marks:
                for j in range(cards):
                    deck.append([i, 6 + j])
                    #print(str([6 + j, i]) + ",")
            random.shuffle(deck)
            room = {
                "creator": a[1],
                "users": [],
                "wait": True,
                "deck": deck,
                "id": len(rooms),
                "max_users": 0
            }
            rooms.append(room)
            return str(room)

        elif a[0] == "connect_room":

            rooms[int(a[2])]["users"].append(int(a[1]))
            return str(rooms[int(a[2])])

        elif a[0] == "get_room":
            # if a[1] in rooms[int(a[2])]:
            return str(rooms[int(a[2])])

        elif a[0] == "echo":
            # if a[1] in rooms[int(a[2])]:
            return a[1]
        print(a)

    def _check_if_can_start(self, room_id, user):
        rooms[int(room_id)]


