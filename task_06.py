class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


class Player:
    def __init__(self, p):
        self.name, self.choice = p

    def __str__(self):
        return f'{self.name} {self.choice}'


def rps_game_winner(choices):
    if len(choices) != 2:
        raise WrongNumberOfPlayersError

    for i in choices:
        if i[1] not in ['R', 'P', 'S']:
            raise NoSuchStrategyError

    player1, player2 = Player(choices[0]), Player(choices[1])

    # if there is a draw and/or first player wins
    if player1.choice == player2.choice or \
            (player1.choice == 'R' and player2.choice == 'S') or \
            (player1.choice == 'P' and player2.choice == 'R') or \
            (player1.choice == 'S' and player2.choice == 'P'):
        return player1
    else:
        return player2
