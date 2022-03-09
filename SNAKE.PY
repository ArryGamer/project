from re import I
from turtle import color
import pygame
import random
import button

pygame.init()

red = (255, 0, 0)
lime = (0,255,0)
white = (255, 255 , 255)
black = (0 ,0 ,0)

screen_width = 900
screen_hieght = 600
gamewindow = pygame.display.set_mode((screen_width, screen_hieght))
pygame.display.set_caption("SnakesWithPhenox")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
bgm = pygame.mixer.music.load("theme.mp3")
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(701, 35, exit_img, 0.8)

pygame.mixer.music.play()


def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gamewindow.blit(screen_text, [x, y])
def plot_snake(gamewindow, colour, snk_list, size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, colour, [x, y, size, size])

def game_loop():
        
        game_exit = False
        game_over = False
        snake_x = 549
        snake_y = 233
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1
        food_x = random.randint(20, screen_width)
        food_y = random.randint(20, screen_hieght)
        score = 0
        vel = 5
        size = 20
        fps = 30
        r = 5
        w = 5
        while not game_exit:
            for event in pygame.event.get():
                print (event)
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = vel
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - vel
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - vel
                        velocity_x = 0
            
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 1
                food_x = random.randint(20, screen_width)
                food_y = random.randint(20, screen_hieght)
                snk_length += 5

            gamewindow.fill(black)
            text_screen("Score:"+ str(score * 10), red, 5, 5)
            pygame.draw.rect(gamewindow, red , (food_x, food_y,20,20))
            if exit_button.draw(gamewindow):
                exit()
            head = [] 
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_x>screen_hieght:
                game_over = True

            # pygame.draw.rect(gamewindow, lime, [snake_x, snake_y, size, size])
            plot_snake(gamewindow, white, snk_list, size)
            
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        quit()
game_loop()
    