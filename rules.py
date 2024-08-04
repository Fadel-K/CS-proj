from random import randint

class player():
    def __init__(self, no, wallet=1500, places=None, cards=None, jailed=0, position=0):
        self.no=no
        self.wallet=wallet
        self.places=places
        self.cards=cards
        self.jailed=jailed
        self.position=position

class place():
    def __init__(self, name, no, color, rent, cost,houses=0, owner=None):
        self.name = name
        self.no = no
        self.houses = houses
        self.cost = cost
        self.owner = owner
        self.rent = rent
        self.color = color
        
class station():
    def __init__(self, name, no, rent, cost, owner=None):
        self.name=name
        self.no=no
        self.owner=owner
        self.rent=rent
        self.cost=cost

class utility():
    def __init__(self, name, no, cost, owner=None):
        self.name=name
        self.no=no
        self.owner=owner
        self.cost = cost
        

#Income tax, Community Chest, Chance, Water, Electricity, Free parking, Jail visit, go to jail

# Brown properties
old_kent_road = place("Old Kent Road", 1, "Brown", 2, 60)
whitechapel_road = place("Whitechapel Road", 3, "Brown", 4, 60)

# Light Blue properties
the_angel_islington = place("The Angel Islington", 6, "Light Blue", 6, 100)
euston_road = place("Euston Road", 8, "Light Blue", 6, 100)
pentonville_road = place("Pentonville Road", 9, "Light Blue", 8, 120)

# Pink properties
pall_mall = place("Pall Mall", 11, "Pink", 10, 140)
whitehall = place("Whitehall", 13, "Pink", 10, 140)
northumberland_avenue = place("Northumberland Avenue", 14, "Pink", 12, 160)

# Orange properties
bow_street = place("Bow Street", 16, "Orange", 14, 180)
marlborough_street = place("Marlborough Street", 18, "Orange", 14, 180)
vine_street = place("Vine Street", 19, "Orange", 16, 200)

# Red properties
strand = place("Strand", 21, "Red", 18, 220)
fleet_street = place("Fleet Street", 23, "Red", 18, 220)
trafalgar_square = place("Trafalgar Square", 24, "Red", 20, 240)

# Yellow properties
leicester_square = place("Leicester Square", 26, "Yellow", 22, 260)
coventry_street = place("Coventry Street", 27, "Yellow", 22, 260)
piccadilly = place("Piccadilly", 29, "Yellow", 24, 280)

# Green properties
regent_street = place("Regent Street", 31, "Green", 26, 300)
oxford_street = place("Oxford Street", 32, "Green", 26, 300)
bond_street = place("Bond Street", 34, "Green", 28, 320)

# Dark Blue properties
park_lane = place("Park Lane", 37, "Dark Blue", 35, 350)
mayfair = place("Mayfair", 39, "Dark Blue", 50, 400)

# Stations
kings_cross_station = station("King's Cross Station", 5, 25, 200)
marylebone_station = station("Marylebone Station", 15, 25, 200)
fenchurch_st_station = station("Fenchurch St. Station", 25, 25, 200)
liverpool_street_station = station("Liverpool Street Station", 35, 25, 200)

# Utilities
electric_company = utility("Electric Company", 12, 150)
water_works = utility("Water Works", 28, 150)

map = {
    1: old_kent_road,
    2: "community",
    3: whitechapel_road,
    4: "income tax",
    5: kings_cross_station,
    6: the_angel_islington,
    7: "chance",
    8: euston_road,
    9: pentonville_road,
    10: "Visiting Jail",
    11: pall_mall,
    12: electric_company,
    13: whitehall,
    14: northumberland_avenue,
    15: marylebone_station,
    16: bow_street,
    17: "community",
    18: marlborough_street,
    19: vine_street,
    20: "Free Parking",
    21: strand,
    22: "chance",
    23: fleet_street,
    24: trafalgar_square,
    25: fenchurch_st_station,
    26: leicester_square,
    27: coventry_street,
    28: water_works,
    29: piccadilly,
    30: "Go to Jail",
    31: regent_street,
    32: oxford_street,
    33: "community",
    34: bond_street,
    35: liverpool_street_station,
    36: "chance",
    37: park_lane,
    39: mayfair
}


num_pl=0

while not (6>=num_pl>=2):
    try:
        num_pl=int(input("Number of players (2-6):"))
    except:
        print("Only whole numbers")
print(num_pl, "Playing! Have fun")
def main(player):
    die1=randint(1,6)
    die2=randint(1,6)
    roll = die1+die2
    pos = player.position
    pos+=roll
    # position 37, u roll a 12 now ur position = 49
    if pos>39:
        pos-=40
        player.wallet=player.wallet+200

    place_v = map[pos]
    
    if place_v=="community":
        