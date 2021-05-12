import random


class SweepStakes:
    def __init__(self):
        pass

    def contestants(self):
        contestants = [
            {
                'id': 111,
                'first_name': 'John',
                'last_name': 'Doe'
            },
            {
                'id': 222,
                'first_name': 'Karen',
                'last_name': 'Nomask'
            },
            {
                'id': 444,
                'first_name': 'Marshall',
                'last_name': 'Mathers'
            },


        ]
        return contestants

    def choose_winner(self):
        rand_int = random.randint(0, len(food.contestants()) - 1)
        winner = food.contestants()[rand_int]
        print(f'Guess What?! {winner["first_name"]} {winner["last_name"]} you won!')


food = SweepStakes()
food.choose_winner()
