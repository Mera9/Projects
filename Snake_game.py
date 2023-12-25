import pygame
import time
import random

pygame.init()

# Function to generate a random color
def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Define random colors
Background_Color = generate_random_color()
Snake_Color = generate_random_color()
Food_Color = generate_random_color()

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")


def draw_snake(snake_block, snake_list):
    for element in snake_list:
        pygame.draw.rect(dis, Snake_Color, [element[0], element[1], snake_block, snake_block])


def game_loop():
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_block = 10
    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        for coord in snake_list[:-1]:
            if coord[0] == x1 and coord[1] == y1:
                game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(Background_Color)
        pygame.draw.rect(dis, Food_Color, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        draw_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        time.sleep(0.1)

    pygame.quit()
    quit()

game_loop()

# Press "run" in the PyCharm, to play the Snake game.
