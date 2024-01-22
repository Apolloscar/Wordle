import pygame as p
import WordleEngine


p.init()

# number of squares in each row, i.e how many letters for each word
SQ_NUM = 5
# number of rows, i.e number of tries
ROW_NUM = 6
SQ_SIZE = 100
WIDTH, HEIGHT = SQ_NUM*SQ_SIZE, ROW_NUM*SQ_SIZE

MAX_FPS = 15

def main():
    #set the size of the display window
    screen = p.display.set_mode((WIDTH,HEIGHT))
    #receive clock to heelp with time elements in game
    clock = p.time.Clock()
    #initialize with just a white screen
    screen.fill(p.Color("white"))

    #holds gamestate of the game at any given point
    gs = WordleEngine.GameState(SQ_NUM, ROW_NUM)

    #continue running game until it is quitted
    running = True
    while running:
        #check for possible events player makes
        for e in p.event.get():
            #check if player has quit wuith the close button
            if e.type == p.QUIT:
                running = False
        # Set max FPS
        clock.tick(MAX_FPS)
        drawBoard(screen, gs)
        #display the screen as it is now
        p.display.flip()


def drawBoard(screen, gs):
    #colors of backgound for squares: white for initial color, grey for letter not in word, yellow for wrong place, green for correct letter and position
    global colors
    colors = {"_": "white", "a": "gray", "y": "yellow", "e": "springgreen4"}

    # loads in image of entry square
    square_surface = p.transform.scale(p.image.load("images/blankSquare.png"), (SQ_SIZE, SQ_SIZE))
    for row in range(ROW_NUM):
        for sq in range(SQ_NUM):
            #create surface with appropriate color for square background
            square_color_surface = p.Surface((SQ_SIZE, SQ_SIZE))
            square_color_surface.fill(p.Color(colors[gs.board[row][sq][0]]))

            # surface of outline of square
            screen.blit(square_color_surface,p.Rect(sq*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            screen.blit(square_surface,p.Rect(sq*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    
if __name__ == "__main__":
    main()