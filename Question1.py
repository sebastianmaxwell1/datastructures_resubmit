import random


class PiDay:
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    print(months[2])
    print("Happy pi-day!")


# question 1B


class BirthdayLocations:
    birthdayLocations = ["Miami", "Qatar", "Ft Pierce", "Wichita"]
    birthdayLocations.add("Tampa")
    birthdayLocations.add("Palm Beach")
    birthdayLocations.add("Vegas")
    for locations in birthdayLocations:
        print(locations)


# Problem 1C:


class Sweepstakes:
    def __init__(self):
        self.name = ''

    def sweepstakes_winner(self):
        winner = random.choice(list(contestants.values()))
        print(f'The winner is: {winner}')


contestants = {
    "ticket1": "Joyner Lucas",
    "ticket2": "Kendrick Lamar",
    "ticket3": "Eminem",
    "ticket4": "Hopsin",
    "ticket5": "NF"
}
