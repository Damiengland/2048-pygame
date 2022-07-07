import pygame
import numpy as np
from logic import Logic

# constants
FPS = 60
W = 400
H = 500
N = 4
GAP = 5
CELL_SIZE = 90
COLORS = {
    "bg": (186, 171, 159),
    0: (206, 192, 180),
    2: (243, 226, 222),
    4: (236, 223, 205),
    8: (241, 177, 121),
    16: (238, 140, 84),
    32: (248, 123, 96),
    64: (235, 88, 55),
    128: (245, 214, 111),
    256: (241, 208, 75),
    512: (227, 192, 41),
    1024: (237, 196, 62),
    2048: (231, 188, 45),
    4096: (96, 216, 148)
}

# initialize pygame font library
pygame.font.init()
# set font style
game_font = pygame.font.SysFont("cooperhewittbook", 24, bold=True)

# testing grid for visual setup
TEST_GRID = np.array([[2, 4, 8, 16],
                      [32, 64, 128, 256],
                      [512, 1024, 2048, 4096],
                      [0, 0, 0, 0]])


def draw_screen(win, grid):
    '''
    draws game elements onto the screen
    '''
    # set bg color to white
    win.fill(COLORS["bg"])

    # set box size
    box_size = CELL_SIZE + GAP * 2

    # for loop to build grid
    for r in range(N):
        rectX = box_size * r + GAP
        for c in range(N):
            rectY = box_size * c + GAP

            g = grid[c][r]

            pygame.draw.rect(
                win,
                COLORS[g],
                pygame.Rect(rectX, rectY, CELL_SIZE, CELL_SIZE),
                border_radius=10
            )

            # turn grid number into a string and if number is equal to zero make it empty string
            if g == 0:
                font_input = ""
            else:
                font_input = f"{g}"

            # draw text on each box
            box_text = game_font.render(font_input, True, (255, 255, 255))
            text_rect = box_text.get_rect(center=(rectX + CELL_SIZE / 2,
                                                  rectY + CELL_SIZE / 2))
            win.blit(box_text, text_rect)

            # draw score of the game
            score = sum(grid.flatten())
            score_input = f"Score: {score}"
            score_text = game_font.render(score_input, True, (255, 255, 255))
            score_text_rect = score_text.get_rect(center=(W / 2, H - 50))
            win.blit(score_text, score_text_rect)

    # updates screen based on clock fps
    pygame.display.update()


def main():
    '''
    Main game function
    '''

    # create an instance of the logic class
    game = Logic()
    # generate starting numbers
    game.generate_num(k=2)

    # initialize pygame module
    pygame.init()

    # load logo & set name
    logo = pygame.image.load("images/2048_logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("2048")

    # create screen with dims of 240 x 180
    window = pygame.display.set_mode((W, H))

    # create clock attribute to update display
    clock = pygame.time.Clock()

    # define variable to control main loop
    running = True

    # main loop
    while running:

        # set refresh rate per second
        clock.tick(FPS)

        # run game
        grid = game.grid

        # call draw screen function
        draw_screen(window, grid)

        # event handling, gets all events
        for event in pygame.event.get():
            # quit event function
            if event.type == pygame.QUIT:
                # exit main loop by setting control variable to false
                running = False
                pygame.quit()
            # listens for which keys are pressed
            if event.type == pygame.KEYDOWN:
                # triggers action based on key pressed
                if event.key == pygame.K_UP:
                    # print("Up")
                    game.play("u")
                if event.key == pygame.K_DOWN:
                    # print("Down")
                    game.play("d")
                if event.key == pygame.K_LEFT:
                    # print("Left")
                    game.play("l")
                if event.key == pygame.K_RIGHT:
                    # print("Right")
                    game.play("r")
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()


# run the main function only if this module is executed as the main script (if this module is imported then nothing is executed)
if __name__ == "__main__":
    # call main function
    main()
