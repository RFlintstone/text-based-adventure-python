import json

class World:
    def __init__(self):
        self.current_room = None
        with open("rooms.json") as f:
            self.rooms = json.load(f)

    def set_room(self, new_room):
        self.current_room = new_room

    def get_room(self):
        return self.current_room

    def load_room(self):
        # Print current room description
        if self.current_room is not None:
            res = self.rooms[self.current_room]["description"]
        else:
            res = None

        return res

    def get_exits(self):
        res = self.rooms[self.current_room]["exits"]
        return res


class Player(World):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.inv = list()

    def add_inv(self, new_item):
        self.inv.append(new_item)

    def command(self, action):
        res = None
        action = action.lower()
        act_splt = action.split(" ")

        if len(act_splt) < 2:
            print("Please provide more arguments")
        else:
            commands = ["go", "use", "inspect", "talk"]
            if act_splt[0] in commands:
                print(f"Executing command: {action}")
                res = act_splt[0], act_splt[1]
            else:
                print("That's not a valid command")
                res = act_splt[0], None
        return res

    def move(self, direction):
        directions = ["north", "east", "south", "west"]
        if direction in directions:
            if direction in w.get_exits():
                print(f"Moving {self.name} to the {direction}")
                w.set_room(w.get_exits()[direction])
                print(f"You're now in the {w.get_room()}")
                print(f"Description: {w.load_room()}")
            else:
                print(f"There is no exit in the {direction}")
        else:
            print("Please provide a valid direct (ex: North)")

    def use(self, arg):
        print("USE " + arg)

        if arg in self.inv:
            print(f"You used {arg}")
            self.inv.remove(arg)
        else:
            print("You're trying to use an item you don't have")

    def inspect(self, arg):
        res = None
        print("INSPECT " + arg)

        if arg == ("inv" or "inventory"):
            res = self.inv

        return res

    def talk(self, arg):
        print("TALK " + arg)

class Console:
    def __init__(self):
        self.SCREEN_WIDTH = 75

    def get_screen(self):
        return self.SCREEN_WIDTH

    def set_screen(self, new_width):
        self.SCREEN_WIDTH = new_width


"""
Room names:
- Bathroom
- Study
- Dining Room  
- Game Room
- Bedroom
"""

c = Console()
w = World()

print("=" * c.get_screen())
p = Player(input("What's your name? "))
p.add_inv("key")

w.set_room("game room")
print("=" * c.get_screen())
print(f"You start in the {w.get_room()}.")
print(f"Description: {w.load_room()}")

while True:
    print("=" * c.get_screen())
    cmd, arg = p.command(input("What do you want to do? "))
    if cmd == "go":
        p.move(arg)
    elif cmd == "use":
        p.use(arg)
    elif cmd == "inspect":
        res = p.inspect(arg)
        print(res)
    elif cmd == "talk":
        p.talk(arg)