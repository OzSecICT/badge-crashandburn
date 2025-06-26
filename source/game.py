import button
import led

class Game:
    """
    Base game class
    """
    def __init__(self):
        print("Initializing base Game class")
        self.__running = False

    def set_running(self, running):
        print(f"Setting game running state to {running}")
        self.__running = running

    def register_callbacks(self):
        """
        Register button callbacks
        Overload with your own logic.
        """
        print("Registering default button callbacks to do_nothing")
        button.up.callback = self.do_nothing  # type: ignore
        button.down.callback = self.do_nothing  # type: ignore
        button.left.callback = self.do_nothing  # type: ignore
        button.right.callback = self.do_nothing  # type: ignore
        button.a.callback = self.do_nothing  # type: ignore
        button.b.callback = self.do_nothing  # type: ignore
        button.start.callback = self.do_nothing  # type: ignore
        button.select.callback = self.clicked_select  # type: ignore

    def do_nothing(self):
        """
        Does nothing
        Useful for buttons that are not used in the game.
        """
        print("Button pressed, doing nothing.")
        pass

    def clicked_select(self, pin, pressed, duration):
        """
        Handle the select button being pressed
        """
        if pressed:
            self.exit()

    @property
    def is_running(self):
        return self.__running
    
    def run(self):
        """
        Set up the board for the game
        Overload with your own logic.
        """
        self.set_running(True)
        led.clear()
        button.clear()
        self.register_callbacks()

    def exit(self):
        """
        Exit the game and set running state to False
        """
        led.clear()
        button.clear()
        self.set_running(False)