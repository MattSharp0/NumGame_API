import json
from random import randint


class Game():

    def __init__(self, save: dict = {}, player: str = '', max: int = 100) -> None:
        if save:
            print(save)
            self.player = save.get("player")
            self.correct = save.get("correct")
            self.guesses = save.get("guesses")
            self.number = save.get("number")
        else:
            self.player = player
            self.correct = False
            self.guesses = []
            self.number = randint(1, max)

    def check_guess(self, guess: int):
        self.guesses.append(guess)
        if self.number == guess:
            self.correct = True
            return 'Correct!'
        elif self.number > guess:
            return 'Too low'
        elif self.number < guess:
            return 'Too high'

    def save_game(self):
        new_data = {'player': self.player, 'correct': self.correct,
                    'total_guesses': len(self.guesses), 'guesses': self.guesses, 'number': self.number}
        with open('scores.json', 'r+') as jf:
            file_data = json.load(jf)
            saves = file_data["in_progress"]
            for i in range(1, len(saves)):
                if saves[i]["player"] == self.player:
                    del saves[i]
            if self.correct:
                file_data["completed"].append(new_data)
            else:
                file_data["in_progress"].append(new_data)

            jf.seek(0)
            json.dump(file_data, jf, indent=4)


def load_game(player):
    with open('scores.json', 'r+') as jf:
        file_data = json.load(jf)
        saves = file_data["in_progress"]
        for i in range(1, len(saves)):
            if saves[i]["player"] == player:
                return saves[i]


def get_game_data(completed: bool = True):
    with open('scores.json') as jf:
        scores = json.load(jf)
        if completed:
            return scores["completed"]
        else:
            return scores["in_progress"]
