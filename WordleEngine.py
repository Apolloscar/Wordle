import random
# will hold all the words in the file
setOfAllWords = set()


class GameState():
    def __init__(self, SQ_NUM = 5, ROW_NUM = 6):
        self.board = [[['_', '_'] for _ in range(SQ_NUM)] for _ in range(ROW_NUM)]
        self.secret_word = self.chooseWord()
        self.current_row = 0
        self.current_sq = 0

    # when a character outside of backspace is pressed
    def enterLetter(self, key_pressed):
        key_pressed = key_pressed.lower()
        # if all squares in row used then cant add another letter or if not a 
        if self.current_sq >= len(self.board[0]) or not ('a'<= key_pressed <= 'z'):
            return
       
        # add letter to board and update the current square we can write on
        self.board[self.current_row][self.current_sq][1] = key_pressed
        self.current_sq += 1
    
    # when backspace is pressed
    def deleteLetter(self):
        # if no letters in cureent row then do nothing
        if self.current_sq == 0:
            return
        # go back a square and make it blank
        self.current_sq -=1
        self.board[self.current_row][self.current_sq][1] = '_'
    
    # when enter is pressed
    def enterWord(self):
        # if word is not correct amount of letters theb cannot submit word
        if self.current_sq< len(self.board[0]):
        
            return True
        if not self.isValidWord():
            return False
        # will contain letters from secret words that are not correct in submitted word to check if submitted word has correct letters but wrong position later
        unused_letters = {}
        for sq in range(len(self.board[0])):
            # is coreect so change background to color that represents that
            if self.board[self.current_row][sq][1] == self.secret_word[sq]:
                self.board[self.current_row][sq][0] = 'c'
            else:
                # submitted letter does not match letter in secret word at same position
                unused_letters[self.secret_word[sq]] = unused_letters.get(self.secret_word[sq], 0) + 1
        
        # check if letter in submiteed word is in secret word but wrong position or not at all in word
        for sq in range(len(self.board[0])):
            # if letter has correct color background then skip
            if self.board[self.current_row][sq][0] != '_':
                continue

            if unused_letters.get(self.board[self.current_row][sq][1], 0) > 0:
                # correct letter but wrong position so give that background color and mark that letter is used from that secret word
                self.board[self.current_row][sq][0] = 'p'
                unused_letters[self.board[self.current_row][sq][1]] -= 1
            else:
                # letter not in secret word or has already been accounted for
                self.board[self.current_row][sq][0] = 'w'
        
        # start at next row and first square
        self.current_row += 1
        self.current_sq = 0

        return True
    # check if word is in list
    def isValidWord(self):
        word = ""
        for sq in self.board[self.current_row]:
            word += sq[1]
        return word in setOfAllWords
    # randomly select the secret word for player to guess
    def chooseWord(self):

        return random.choice(tuple(setOfAllWords))
        
        
    

def getWords(SQ_NUM):
    
    global setOfAllWords
    setOfAllWords = set()
    f = open("words.txt", 'r')
    # read entire file and then split it by \n into a list
    for word in f.read().splitlines():
        # if word is correct length then add it to the set
        if len(word) == SQ_NUM:
            setOfAllWords.add(word)
    f.close()
    
        
