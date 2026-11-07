import pygame
import sys
import random
import math

pygame.init()
screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Tàu Lái Vũ Trụ")
ship_img = pygame.image.load("resources/rocketship.png")
pygame.display.set_icon(ship_img)
bg_img = pygame.image.load("resources/bg_galaxy.png")
ship_img_x = 220
ship_img_y = 280
ship_img_sound = pygame.mixer.Sound("resources/explosion.wav")

meteor_img = pygame.image.load("resources/meteoroid.png")
meteor_img_x = 220
meteor_img_y = 0
x_change = 0
score = 0
game_over = False
score_text = pygame.font.SysFont("Arial", 24)

while True:
    screen.blit(bg_img, (0,0))
    screen.blit(ship_img, (ship_img_x, ship_img_y))
    screen.blit(meteor_img, (meteor_img_x, meteor_img_y))
    score_render = score_text.render(str(score), True, (255, 255, 255))
    screen.blit(score_render, (10, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            x_change = 0
    if not game_over:
        ship_img_x += x_change
        meteor_img_y += 2
        distance = math.sqrt((ship_img_x - meteor_img_x)**2 + (ship_img_y - meteor_img_y)**2)

        if distance < 60:
            game_over = True
            ship_img_sound.play()
        if meteor_img_y < 360:
            meteor_img_y = 0
            meteor_img_x = random.randint (0, 480)
            score += 1