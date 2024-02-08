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

# organize words in file source to have appropriate words
WordleEngine.getWords(SQ_NUM)


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
            elif e.type == p.KEYDOWN:
                # ` is preesed to make a new game
                if e.key == p.K_BACKQUOTE:
                    return
                # backspace key is pressed, delete character
                elif e.key == p.K_BACKSPACE and not gs.game_over:
                    gs.deleteLetter()
                # enter key is pressed, submit word
                elif e.key == p.K_RETURN and not gs.game_over:
                    gs.enterWord()
                elif not gs.game_over:
                    gs.enterLetter(e.unicode)
        # Set max FPS
        clock.tick(MAX_FPS)
        drawBoard(screen, gs)

        if gs.game_over:
            gameOverScreen(screen, gs)
        #display the screen as it is now
        p.display.flip()


# display current board state
def drawBoard(screen, gs):
    #colors of backgound for squares: white for initial color, grey for letter not in word, yellow for wrong place, green for correct letter and position
    global colors
    colors = {"_": "white", "w": "gray", "p": "yellow", "c": "springgreen4"}
    
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
            
            # move to next square if no text entry
            if gs.board[row][sq][1] == '_':
                continue
            # set font for text
            font = p.font.SysFont("Helvitca",SQ_SIZE, True, False)
            # create text that will be displayed
            text_object = font.render(gs.board[row][sq][1].upper(),0, p.Color("Black"))
            # create rect on appropriate square and center it in that square
            text_location = p.Rect(sq*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE).move(SQ_SIZE/2 - text_object.get_width()/2, SQ_SIZE/2 - text_object.get_height()/2)
            screen.blit(text_object,text_location)

def gameOverScreen(screen,gs):
    
    font = p.font.SysFont("Helvitca",SQ_SIZE//2, True, False)
    # create text that will be displayed
    if gs.isCorrectWord():
        text_object = font.render("You Win",0, p.Color("Green"))
        text_location = p.Rect(0,0,SQ_SIZE*SQ_NUM,SQ_SIZE*ROW_NUM).move(SQ_SIZE*SQ_NUM/2 - text_object.get_width()/2, SQ_SIZE*ROW_NUM/2 - text_object.get_height()/2)
        p.draw.rect(screen,p.Color("Blue"),[SQ_SIZE*SQ_NUM/2 - text_object.get_width()/2, SQ_SIZE*ROW_NUM/2 - text_object.get_height()/2,text_object.get_width(), text_object.get_height()])
        screen.blit(text_object,text_location)
    else:
        text_object_1 = font.render("You Lose",0, p.Color("Green"))
        text_location_1 = p.Rect(0,0,SQ_SIZE*SQ_NUM,SQ_SIZE*ROW_NUM).move(SQ_SIZE*SQ_NUM/2 - text_object_1.get_width()/2, SQ_SIZE*ROW_NUM/2 - text_object_1.get_height()/2)
        text_object_2 = font.render("Word is " + gs.secret_word.upper(),0, p.Color("Green"))
        text_location_2 = p.Rect(0,0,SQ_SIZE*SQ_NUM,SQ_SIZE*ROW_NUM).move(SQ_SIZE*SQ_NUM/2 - text_object_2.get_width()/2, SQ_SIZE*ROW_NUM/2 - text_object_2.get_height()/2 + text_object_1.get_height())
        
        p.draw.rect(screen,p.Color("Blue"),[min(SQ_SIZE*SQ_NUM/2 - text_object_1.get_width()/2, SQ_SIZE*SQ_NUM/2 - text_object_2.get_width()/2),SQ_SIZE*ROW_NUM/2 - text_object_1.get_height()/2, max(text_object_1.get_width(), text_object_2.get_width()), text_object_1.get_height()+text_object_2.get_height()])
        
        screen.blit(text_object_1,text_location_1)
        screen.blit(text_object_2,text_location_2)

    # create rect on appropriate square and center it in that square
    


    
if __name__ == "__main__":
    main()