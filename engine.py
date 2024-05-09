import random
class Ship:
    def __init__(self, size):
        self.row = random.randrange(0,9)
        self.col = random.randrange(0,9)
        self.size = size
        self.orientation = random.choice (["h","v"])
        self.indexes = self.compute_indexes()
    def compute_indexes(self):
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i*10 for i in range(self.size)]

class Player:
    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100)]
        self.place_ships (sizes = [5,4,3,3,2])
    
    def place_ships (self, sizes):
        for size in sizes:
            placed = False
            while not placed:

                ship = Ship(size)
                possible = True
                for i in ship.indexes:
                    if i >= 100:
                        possible = False
                        break
                    new_row = i // 10
                    new_col = i % 10
                    if new_row != ship. row and new_col != ship.col:
                        possible = False
                        break

                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible = False
                            break

                if possible:
                    self.ships.append(ship)
                    placed = True
p = Player()
for ship in p.ships:
    print(ship.indexes)