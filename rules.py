from random import randint
import csv
from time import sleep

class player():
    list=[]
    def __init__(self, no, wallet=1500, places=[], card=None, bankruptcy=False, jailed=0, position=0):
        self.no=no
        self.wallet=wallet
        self.places=places
        self.cards=card
        self.jailed=jailed
        self.position=position
        self.bankruptcy=bankruptcy
        player.list.append(self)

class place():
    list=[]
    def __init__(self, name, no, color, rent, cost, house_cost, houses=0, owner=None):
        self.name = name
        self.no = no
        self.houses = houses
        self.cost = cost
        self.house_cost=house_cost
        self.owner = owner
        self.rent = rent
        self.color = color
        place.list.append(self)

        
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
old_kent_road = place("Old Kent Road", 1, "Brown", [2, 10, 30, 90, 160, 250], 60, 50)
whitechapel_road = place("Whitechapel Road", 3, "Brown", [4, 20, 60, 180, 320, 450], 60, 50)

# Light Blue properties
the_angel_islington = place("The Angel Islington", 6, "Light Blue", [6, 30, 90, 270, 400, 550], 100, 50)
euston_road = place("Euston Road", 8, "Light Blue", [6, 30, 90, 270, 400, 550], 100, 50)
pentonville_road = place("Pentonville Road", 9, "Light Blue", [8, 40, 100, 300, 450, 600], 120, 50)

# Pink properties
pall_mall = place("Pall Mall", 11, "Pink", [10, 50, 150, 450, 625, 750], 140, 100)
whitehall = place("Whitehall", 13, "Pink", [10, 50, 150, 450, 625, 750], 140, 100)
northumberland_avenue = place("Northumberland Avenue", 14, "Pink", [12, 60, 180, 500, 700, 900], 160, 100)

# Orange properties
bow_street = place("Bow Street", 16, "Orange", [14, 70, 200, 550, 750, 950], 180, 100)
marlborough_street = place("Marlborough Street", 18, "Orange", [14, 70, 200, 550, 750, 950], 180, 100)
vine_street = place("Vine Street", 19, "Orange", [16, 80, 220, 600, 800, 1000], 200, 100)

# Red properties
strand = place("Strand", 21, "Red", [18, 90, 250, 700, 875, 1050], 220, 150)
fleet_street = place("Fleet Street", 23, "Red", [18, 90, 250, 700, 875, 1050], 220, 150)
trafalgar_square = place("Trafalgar Square", 24, "Red", [20, 100, 300, 750, 925, 1100], 240, 150)

# Yellow properties
leicester_square = place("Leicester Square", 26, "Yellow", [22, 110, 330, 800, 975, 1150], 260, 150)
coventry_street = place("Coventry Street", 27, "Yellow", [22, 110, 330, 800, 975, 1150], 260, 150)
piccadilly = place("Piccadilly", 29, "Yellow", [24, 120, 360, 850, 1025, 1200], 280, 150)

# Green properties
regent_street = place("Regent Street", 31, "Green", [26, 130, 390, 900, 1100, 1275], 300, 200)
oxford_street = place("Oxford Street", 32, "Green", [26, 130, 390, 900, 1100, 1275], 300, 200)
bond_street = place("Bond Street", 34, "Green", [28, 150, 450, 1000, 1200, 1400], 320, 200)

# Dark Blue properties
park_lane = place("Park Lane", 37, "Dark Blue", [35, 175, 500, 1100, 1300, 1500], 350, 200)
mayfair = place("Mayfair", 39, "Dark Blue", [50, 200, 600, 1400, 1700, 2000], 400, 200)

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
    38: "super tax",
    39: mayfair
}

def main(per, rolling = True):
    doubles=True
    d=0
    while doubles:
        if d==3:
            print("Go To Jail for moving too fast")
            per.position=10
            per.jailed=3
            return
        doubles=False
        if rolling:
            die1=randint(1,6)
            die2=randint(1,6)
            print(f"Die 1: {die1}, Die 2: {die2}")
            sleep(1)
            if die1==die2:
                print("DOUBLES!!!")
                doubles=True
                d+=1
            roll = die1+die2
            print(f"Total: {roll}")
            pos = per.position
            pos+=roll
            # position 37, u roll a 12 now ur position = 49
            if pos>39:
                pos-=40
                per.wallet=per.wallet+200
            print(f'Rolled a {roll}')
            sleep(2)
        place_v = map[pos]
        if not isinstance(place_v, str):
            print(place_v.name)
            
        if per.jailed>0:
            if per.jailed>1:
                inp=input("Would you like to pay or roll dice: ")
                if inp=="pay":
                    per.wallet=per.wallet-50
                    per.jailed=0
                else:
                    print("Rolling")
                    d1=randint(1,6)
                    d2=randint(1,6)
                    if d1==d2:
                        print("Success")
                    else:
                        print("Unsuccessful")
            else:
                print("Your last chance, payment is compulsory")
                per.wallet=per.wallet-50
                per.jailed=0
                
        elif place_v=="community":
            no=randint(1,16)
            comm_log(no,per)
            
        elif place_v=="chance":
            no=randint(1,16)
            chance_log(no,per)
            
        elif place_v=="income tax":
            print("Pay 200")
            per.wallet=per.wallet-200
            
        elif place_v=="super tax":
            print("Pay 100")
            per.wallet=per.wallet-100
            
        elif place_v=="Visiting Jail":
            print("Visiting Jail")
            
        elif place_v=="Free Parking":
            print("Free Parking")
            
        elif place_v=="Go to Jail":
            print("Go to Jail")
            per.position=10
            per.jailed=3
            
        elif isinstance(place_v, place):
            if place_v.owner==None:
                inp = input(f'Do you want to buy this property for £ {place_v.cost} \n Input yes/no: ')
                if inp=='yes':
                    if per.wallet>place_v.cost:
                        per.wallet=per.wallet-place_v.cost
                        per.places.append(place_v)
                        place_v.owner=per
                        print("Purchase successful")
                    else:
                        print("Dont have enough to buy")
                    
                elif inp=='no':
                    print("Sorry to see you go!")
            elif place_v.owner==per:
                print("Your own property")
            else:
                print("you have to pay £", place_v.rent[place_v.houses],"to player", place_v.owner.no)
                per.wallet=per.wallet-place_v.rent
                place_v.owner.wallet=place_v.owner.wallet+place_v.rent
                
        elif isinstance(place_v, station):
            if place_v.owner==None:
                inp = input(f"Do you want to buy this property for £ {place_v.cost} \n Input yes/no: ")
                if inp=='yes':
                    if per.wallet>place_v.cost:
                        per.wallet=per.wallet-place_v.cost
                        per.places.append(place_v)
                        place_v.owner=per
                        print("Purchase successful")
                        st=0
                        sts=[]
                        if kings_cross_station.owner==per:
                            st+=1
                            sts.append(kings_cross_station)
                        if marylebone_station.owner==per:
                            st+=1
                            sts.append(marylebone_station)
                        if fenchurch_st_station.owner==per:
                            st+=1
                            sts.append(fenchurch_st_station)
                        if liverpool_street_station.owner==per:
                            st+=1
                            sts.append(liverpool_street_station)
                        rent=25*2**(st-1)
                        for stat in sts:
                            stat.rent=rent
                    else:
                        print("Dont have enough to buy")

                elif inp=='no':
                    print("Sorry to see you go!")
            elif place_v.owner==per:
                print("Your own property")
            else:
                print("you have to pay £", place_v.rent,"to player", place_v.owner.no)
                per.wallet=per.wallet-place_v.rent
                place_v.owner.wallet=place_v.owner.wallet+place_v.rent
                
        elif isinstance(place_v, utility):
            if place_v.owner==None:
                inp = input(f"Do you want to buy this property for £ {place_v.cost}\n Input yes/no: ")
                if inp=='yes':
                    if per.wallet>place_v.cost:
                        per.wallet=per.wallet-place_v.cost
                        per.places.append(place_v)
                        place_v.owner=per
                        print("Purchase successful")
                    else:
                        print("Dont have enough to buy")
                    
                elif inp=='no':
                    print("Sorry to see you go!")
            elif place_v.owner==per:
                print("Your own property")
            else:
                ut=0
                uts=[]
                if electric_company.owner==place_v.owner:
                    ut+=1
                    uts.append(electric_company)
                if water_works.owner==place_v.owner:
                    ut+=1
                    uts.append(water_works)
                if len(uts)==1:
                    rent=roll*4
                else:
                    rent=roll*10
                print("you have to pay £", rent,"to player", place_v.owner.no)
                per.wallet=per.wallet-rent
                place_v.owner.wallet=place_v.owner.wallet+rent
        sleep(2)
        
def comm_log(no,per):
    with open ('comm.csv','r') as comm:
        cr=list(csv.reader(comm))
        if no==1:
            print(cr[0])
            per.position=0
            per.wallet=per.wallet+200
            main(per,False)
        elif no==2:
            print(cr[1])
            per.wallet=per.wallet+200
        elif no==3:
            print(cr[2])
            per.wallet=per.wallet-50
        elif no==4:
            print(cr[3])
            per.wallet=per.wallet+50
        elif no==5:
            print(cr[4])
            per.card=True
        elif no==6:
            print(cr[5])
            per.position=10
            per.jail=True
            main(per,False)
        elif no==7:
            print(cr[6])
            per.wallet=per.wallet+100
        elif no==8:
            print(cr[7])
            per.wallet=per.waller+50
        elif no==9:
            print(cr[8])
            per.wallet=per.wallet+10*num_pl
            for i in player.list:
                i.wallet=i.wallet-10
        elif no==10:
            print(cr[9])
            per.wallet=per.wallet+100
        elif no==11:
            print(cr[10])
            per.wallet=per.wallet-100
        elif no==12:
            print(cr[11])
            per.wallet=per.wallet-50
        elif no==13:
            print(cr[12])
            per.wallet=per.wallet+25
        elif no==14:
            print(cr[13])
            st = (per.position//10) + 1
            hs=ht=0
            for i in range((st-1)*10,st*10):
                place_v=map[i]
                if isinstance(place_v,place):
                    if place_v.houses<=4:
                        hs+=place_v.houses
                    else:
                        ht+=1
            amount=40*hs+115*ht
            print("Amount to pay:", amount)
        elif no==15:
            print(cr[14])
            per.wallet=per.wallet+10
        elif no==16:
            print(cr[15])
            per.wallet=per.wallet+100

def chance_log(no,per):
    with open ('chance.csv','r') as comm:
        cr=list(csv.reader(comm))
        if no==1:
            print(cr[0])
            per.position=0
            per.wallet=per.wallet+200
            main(per,False)
        elif no==2:
            print(cr[1])
            if per.position<24:
                per.position=24
            elif per.position>24:
                per.position=24
                per.wallet=per.wallet+200
            main(per, False)
        elif no==3:
            print(cr[2])
            per.position=39
            main(per,False)
        elif no==4:
            print(cr[3])
            if per.position<11:
                per.position=11
            elif per.position>11:
                per.position=11
                per.wallet=per.wallet+200
                main(per,False)
        elif no==5:
            print(cr[4])
            if per.position<10:
                per.position=5
            elif per.position<20:
                per.poition=15
            elif per.position<30:
                per.position=25
            elif per.position<40:
                per.position=35
                main(per,False)
        elif no==6:
            print(cr[5])
            if per.positon<10:
                per.position=12
            elif per.position>20 and per.positon<30:
                per.position=28
                main(per,False)
        elif no==7:
            print(cr[6])
            per.wallet=per.wallet+50
        elif no==8:
            print(cr[7])
            per.card=True
        elif no==9:
            print(cr[8])
            per.position=per.position-3
            main(per,False)
        elif no==10:
            print(cr[9])
            per.position=10
            per.jailed=3
            main(per,False)
        elif no==11:
            print(cr[10])
            for places in per.places:
                h=t=0
                if h<5:
                    h+=places.houses
                else:
                    t+=1
            per.wallet=per.wallet-h*25 - t*100
        elif no==12:
            print(cr[11])
            per.wallet=per.wallet-15
        elif no==13:
            print(cr[12])
            if per.position<5:
                per.position=5
            elif per.poition>5:
                per.poition=5
                per.wallet=per.wallet+200
                main(per,False)
        elif no==14:
            print(cr[13])
            if num_pl>1:
                per.wallet=per.wallet-50*num_pl
        elif no==15:
            print(cr[14])
            per.wallet=per.wallet+150       

def start(per):
    houses=[]
    col={'Brown':0, 'Light Blue':0, 'Pink':0, 'Orange':0, 'Red':0, 'Yellow':0, 'Green':0, 'Dark Blue':0}
    
    for pla in per.places:
        col[pla.color]=col[pla.color]+1
    
    for k,v in col:
        if k in ['Brown', 'Dark Blue']:
            if v==2:
                houses.append(v)
        else:
            if v==3:
                houses.append(v)
    inp='dice'
    if len(houses)>0:
        inp=input(f'Would you like to place houses or roll dice? (input "houses" for houses and "dice" for rolling dice): ')
        sleep(2)
    if inp=='dice':
        main(per)
    else:
        inp=input(f'Choose which color you want to add houses to {houses}: ')
        places=[]
        for i in place.list:
            if i.color==inp:
                places.append(i)
        print(f'Choose which place do you want to add houses to: ')
        for i in places:
            print(i.name, end=', ')
            sleep(1)
        inp = input('Enter: ')
        for i in places:
            if i.name.lower()==inp:
                i.houses=i.houses+1
        sleep(1)     
        
        

num_pl=0

while not (6>=num_pl>=2):
    try:
        num_pl=int(input("Number of players (2-6):"))
    except:
        print("Only whole numbers")
print(num_pl, "Playing! Have fun")

player1=player(1)
player2=player(2)
player3=player(3)
player4=player(4)
player5=player(5)
player6=player(6)

if num_pl<6:
    del player6
    if num_pl<5:
        del player5
        if num_pl<4:
            del player4
            if num_pl<3:
                del player3
while True:
    sleep(2)
    for i in range(num_pl):
        if i==0:
            if not player1.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player1)
                if player1.wallet<0:
                    print("Player 1 Has Gone Bankrupt!!!")
                    player1.bankruptcy=True
        elif i==1:
            if not player2.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player2)
                if player2.wallet<0:
                    print("Player 2 Has Gone Bankrupt!!!")
                    player2.bankruptcy=True
        elif i==2:
            if not player3.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player3)
                if player3.wallet<0:
                    print("Player 3 Has Gone Bankrupt!!!")
                    player3.bankruptcy=True
        elif i==3:
            if not player4.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player4)
                if player4.wallet<0:
                    print("Player 4 Has Gone Bankrupt!!!")
                    player4.bankruptcy=True
        elif i==4:
            if not player5.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player5)
                if player5.wallet<0:
                    print("Player 5 Has Gone Bankrupt!!!")
                    player5.bankruptcy=True
        elif i==5:
            if not player6.bankruptcy: 
                print(f"Player {i+1}'s turn") 
                start(player6)
                if player6.wallet<0:
                    print("Player 6 Has Gone Bankrupt!!!")
                    player6.bankruptcy=True