import button
import led

class Game:
    """ Base game class."""
    def __init__(self):
        self.__running = False

    def set_running(self, running):
        self.__running = running

    def register_callbacks(self):
        """ Register button callbacks. Requires overriding"""
        pass

    @property
    def is_running(self):
        return self.__running
    
    def run(self):
        """ Set up the board for the game. Requires overriding"""
        self.set_running(True)
        led.clear()
        button.clear()
        self.register_callbacks()

    def exit(self):
        """ Exit the game. """
        led.clear()
        button.clear()
        self.set_running(False)