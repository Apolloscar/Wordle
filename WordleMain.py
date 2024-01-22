import pygame as p


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
        drawBoard(screen)
        #display the screen as it is now
        p.display.flip()


def drawBoard(screen):
    #colors of backgound for squares: white for initial color, grey for letter not in word, yellow for wrong place, green for correct letter and position
    global colors
    colors = ["white", "grey", "yellow", "green"]
    for x in range(SQ_NUM):
        for y in range(ROW_NUM):
            screen.blit(p.transform.scale(p.image.load("images/blankSquare.png"), (SQ_SIZE, SQ_SIZE)),p.Rect(x*SQ_SIZE,y*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    
if __name__ == "__main__":
    main()