class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player_name):
        # return player in self.players:
        return self.players.count(player_name)
    
    def play_game(self, has_won):
        if has_won:
            self.points += 3