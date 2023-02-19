import pygame
import random
import os
import sys




pygame.init()


# Create Window
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lost on Bit Mountain")

# Create Rectangle
def create_rect(width, height, border, color, border_color):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 2)
    return surf

# Load images
bg_img = pygame.image.load("Image2.png")
bg_img = pygame.transform.scale(bg_img,(WIDTH, HEIGHT))
rect_surf1 = create_rect(510, 60, 5, (255, 255, 255), (255, 255, 255))
rect_surf2 = create_rect(1000, 1000, 7, (255, 255, 255), (255, 255, 255))

#define fonts
font = pygame.font.SysFont("arialblack", 30)
font2 = pygame.font.SysFont("arialblack", 20)
font3 = pygame.font.SysFont("arialblack", 45)

#define colors
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

# Setup game loop
clock = pygame.time.Clock()
FPS = 60


# Main Menu
def main():
    main = True
    pygame.display.set_caption("Main Menu")
    while main:
        clock.tick(FPS)
        window.fill((240, 0, 0))
        window.blit(bg_img, (0,0))
        window.blit(rect_surf1, (134,50))
        draw_text("Welcome! Press return to play", font, TEXT_COL, 140, 175)
        draw_text("Instructions:", font2, TEXT_COL, 150, 285)
        draw_text("Convert the unsigned binary # into decimal", font2, TEXT_COL, 150, 310)
        draw_text("before it passes the white line! Be careful,", font2, TEXT_COL, 150, 335)
        draw_text("time will go faster as your score increases.", font2, TEXT_COL, 150, 360)
        draw_text("Lost in Bit Mountain", font3, TEXT_COL, 147, 50)

        #window.blit(bg_img,(140,140))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main = False
                    play()
        pygame.display.update()




def play():
    play = True
    pygame.display.set_caption("Playing Game")
    while play:
        clock.tick(FPS)

        window.blit(bg_img,(0,0))


        for event in pygame.event.get():
            name()
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                play = False
                main()
        pygame.display.update()

def name():
    score = 0
    number = randomBinary()
    y = 1
    i = 0
    var = 1
    x = random.randint(30, 500)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(300, 750, 140, 32)
    color_inactive = pygame.Color('darkgreen')
    color_active = pygame.Color('lightgreen')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:

                    if event.key == pygame.K_RETURN:
                        if text == '':
                            text = 1000
                        print(text)
                        entered = int(text)
                        bits = bin(entered)[2:]
                        if(len(bits) < 8):

                            for a in range(len(bits), 8, 1):
                                bits = '0'+bits

                        print(bits)


                        text = ''
                        if(bits == number):
                            x = random.randint(30, 750)
                            y = 0
                            number = randomBinary() # change
                            score += 1
                            i += 1



                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if(event.unicode.isdigit()): # accepts if int
                          text += event.unicode

        window.blit(bg_img,(0,0))
        window.blit(rect_surf2, (-100,730))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        window.blit(txt_surface, (305, 756))
        # Blit the input_box rect.
        pygame.draw.rect(window, color, input_box, 4)
        draw_text(number, font2, TEXT_COL, x, y) # needed after rescreen
        draw_text("Score: "+str(score), font2, TEXT_COL, 650, 750) # prints score
        y += var

        if i > 2:
            var += 1
            i = 0
        if y > 725:
            ### return score
            main()


        pygame.display.flip()
        clock.tick(30)

def randomBinary():
    sequence = ''

    for i in range(0,8):
      bit = str(random.randint(0,1))
      sequence += bit

    return sequence





main()

'''for event in pygame.event.get():
    if event.type ==pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON
'''



