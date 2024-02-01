
class GameState():
    def __init__(self, SQ_NUM = 5, ROW_NUM = 6):
        self.board = [["__" for _ in range(SQ_NUM)] for _ in range(ROW_NUM)]
        self.secret_word = "paris"
        self.current_row = 0
        self.current_sq = 0

    def enterLetter(self, key_pressed):
        key_pressed = key_pressed.lower()
        # if all squares in row used then cant add another letter or if not a 
        if self.current_sq >= len(self.board[0]) or not ('a'<= key_pressed <= 'z'):
            return
       
        # add letter to board and update the current square we can write on
        self.board[self.current_row][self.current_sq] = "_"+key_pressed
        self.current_sq += 1