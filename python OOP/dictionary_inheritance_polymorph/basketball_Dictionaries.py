class Player:
    #def __init__(self, name, age, position, team):
        #self.name=name
        #self.age=age
        #self.position=position
        #self.team=team
        #Player.players.append(self)

    #Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        
    def __repr__(self):
        return f"PLAYER: {self.name} has {self.age} years old and his position is: {self.position} in: {self.team} team"

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(repr(player_kevin)) 
print(repr(player_jason))
print(repr(player_kyrie))

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

new_team = []
for data in players:
    player = Player(data)
    new_team.append(player)
print(new_team) 
