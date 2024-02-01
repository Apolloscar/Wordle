
class GameState():
    def __init__(self, SQ_NUM = 5, ROW_NUM = 6):
        self.board = [["__"]*SQ_NUM]*ROW_NUM
        self.secret_word = "paris"

    def enterLetter(self, key_pressed):
        key_pressed = key_pressed.lower()


