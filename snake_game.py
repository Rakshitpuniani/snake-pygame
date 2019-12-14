import pygame
import random
import sys
pygame.init()

def button_pressed():
    global change_direction,run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            change_direction = 'RIGHT'
        if keys[pygame.K_LEFT]:
            change_direction = 'LEFT'
        if keys[pygame.K_UP]:
            change_direction = 'UP'
        if keys[pygame.K_DOWN]:
            change_direction = 'DOWN'

def redraw_window(win):
    global snake_body,food_location

    win.fill((0, 0, 0))
    # Drawing Box
    pygame.draw.line(win, (255, 255, 255), (50, 50), (50, 450))
    pygame.draw.line(win, (255, 255, 255), (50, 50), (450, 50))
    pygame.draw.line(win, (255, 255, 255), (450, 50), (450, 450))
    pygame.draw.line(win, (255, 255, 255), (50, 450), (450, 450))
    # Drawing snake
    for i in snake_body:
        pygame.draw.rect(win, (255, 255, 0), (i[0], i[1], 10, 10))
    # Drawing food
    pygame.draw.rect(win, (255, 255, 255), (food_location[0], food_location[1], 10, 10))


def food():
    #food respawning
    global food_spawn,food_location
    if not food_spawn:
        food_location = [random.randrange(5,45)*10,random.randrange(5,45)*10]
    food_spawn = True

def movement():
    # checking for opposite direction
    global current_direction, change_direction, snake_position,width
    if change_direction == 'LEFT' and current_direction !='RIGHT':
        current_direction = 'LEFT'
    if change_direction == 'RIGHT' and current_direction != 'LEFT':
        current_direction = 'RIGHT'
    if change_direction == 'UP' and current_direction != 'DOWN':
        current_direction = 'UP'
    if change_direction == 'DOWN' and current_direction != 'UP':
        current_direction = 'DOWN'
    # Actual movement
    if current_direction == 'RIGHT':
        snake_position[0] += 10
    if current_direction == 'LEFT':
        snake_position[0] -= 10
    if current_direction == 'DOWN':
        snake_position[1] += 10
    if current_direction == 'UP':
        snake_position[1] -= 10

def collisions():
    global snake_position, width, snake_body, run, food_location, food_spawn,score,win
    #collision with food/ Size increase mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_location[0] and snake_position[1] == food_location[1]:
        food_spawn = False
        score +=1
    else:
        snake_body.pop()
    # If snake collides with the box
    if snake_position[0] < 50 or snake_position[0] > 440:
        run = False
    if snake_position[1] < 50 or snake_position[1] > 440:
        run = False
    # If snake collides with its own body
    for end in snake_body[1:]:
        if end[0] == snake_position[0] and end[1] == snake_position[1]:
            run = False


def show_score(win):
    global score
    score_font = pygame.font.SysFont('times new roman', 20)
    score_surface = score_font.render('score: ' + str(score),True,(255,255,255))
    score_rect = score_surface.get_rect()
    score_rect.center = (78,30)
    win.blit(score_surface,score_rect)


def main():

    global snake_position,snake_body,width,run,food_spawn,food_location,change_direction,current_direction,score
    width = 500
    score = 0
    win = pygame.display.set_mode((width,width))
    pygame.display.set_caption('Snake')
    snake_position = [100,100]
    snake_body = [[100,100],[90,100]]
    current_direction = 'RIGHT'
    change_direction  = current_direction
    food_spawn = True
    food_location = [random.randrange(5,45)*10,random.randrange(5,45)*10]
    run = True
    while run:
        pygame.time.delay(100)
        button_pressed()
        movement()
        food()
        redraw_window(win)
        collisions()
        show_score(win)
        pygame.display.update()



main()




