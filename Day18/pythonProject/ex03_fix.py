
import pygame
import sys
import random

pygame.init();
SCREEN_WIDTH = 800;
SCREEN_HEIGHT = 800;
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
clock = pygame.time.Clock();
background_image = pygame.image.load('BackGround.png');
background_image = pygame.transform.scale(background_image, (800,800));

character_image = pygame.image.load('Attack(10).png');
character_image = pygame.transform.scale(character_image, (80,80));
character = character_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT);

rock_image = pygame.image.load('Rock.png');
rock_image = pygame.transform.scale(rock_image, (40,40));
rocks = [];
running = True;
for i in range(10):
    rock = rock_image.get_rect(left=random.uniform(10, SCREEN_WIDTH - rock_image.get_width()), top=-20);
    dy = random.uniform(200,500);
    rocks.append((rock, dy));

while True:
    screen.blit(background_image, (0,0));

    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        running = False;
    pressed = pygame.key.get_pressed();
    if pressed[pygame.K_LEFT]:
        character.left = character.left - 15;
    elif pressed[pygame.K_RIGHT]:
        character.left = character.left + 15;

    if character.left < 0:
        character.left = 0;

    if character.right > SCREEN_WIDTH:
        character.right = SCREEN_WIDTH;

    for rock, dy in rocks:
        rock.top += 20;
        if rock.top > SCREEN_HEIGHT:
            rocks.remove((rock, dy));
            rock = rock_image.get_rect(left=random.uniform(10, SCREEN_WIDTH - rock_image.get_width()), top=-20);
            dy = random.uniform(200,500);
            rocks.append((rock, dy));
        if character.colliderect(rock):
            running = False;
            pygame.quit();
        for rock, dy in rocks:
            screen.blit(rock_image, rock);

    screen.blit(character_image, character);
    pygame.display.update();
    clock.tick(30);
pygame.quit();