import machine
from machine import Pin

import led


class Scoreboard:
    def __init__(self):
        self.scores = {}
        self.current_game = None

        self.ones_led = led.score_ones
        self.twos_led = led.score_twos
        self.fours_led = led.score_fours
        self.eights_led = led.score_eights
        self.score_leds = [self.ones_led, self.twos_led,
                           self.fours_led, self.eights_led]

    def show_score(self, game):
        self.current_game = game
        print(f"Showing score for game: {self.current_game}")
        self.display_score(self.scores.get(game, 0))

    def display_score(self, score):
        print(f"Converting score {score} to binary.")
        if not (0 <= score <= 15):
            print("Score out of range.")
            return
        ones = score & 0b0001
        twos = (score & 0b0010) >> 1
        fours = (score & 0b0100) >> 2
        eights = (score & 0b1000) >> 3
        if ones:
            self.ones_led.on()
        else:
            self.ones_led.off()
        if twos:
            self.twos_led.on()
        else:
            self.twos_led.off()
        if fours:
            self.fours_led.on()
        else:
            self.fours_led.off()
        if eights:
            self.eights_led.on()
        else:
            self.eights_led.off()

    def add_score(self, game):
        print(f"Adding score for game: {game}")
        if game in self.scores:
            self.scores[game] += 1
        else:
            self.scores[game] = 1
        print(f"Score for {game} is now {self.scores.get([game], 0)}")

        print(f"Score for {game} is now {self.scores.get(game, 0)}")
        print(f"Score for {game}: {self.scores.get(game, 0)}")
        return self.scores.get(game, 0)

    def remove_score(self, game):
        if game in self.scores:
            if self.scores[game] > 0:
                self.scores[game] -= 1
            print(f"Score for {game} is now {self.scores.get(game, 0)}")
        else:
            print(f"No score found for game: {game}")


scoreboard = Scoreboard()
