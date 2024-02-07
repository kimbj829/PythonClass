'''
pip install pygame
'''
import pygame

pygame.init();  #pygame 초기화
screen = pygame.display.set_mode((700, 800)); #화면 디스플레이 설정

'''
게임 fps 설정
- 초당 프레임을 의미함
* 프레임에 따라서 게임에서 캐릭터가 움직이는 속도가 다름
'''

clock = pygame.time.Clock();
while True:
    screen.fill((0,0,0));
    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        break;
    #화면 그리기
    pygame.display.update();
    clock.tick(30); #초당 30프레임(30fps)

pygame.quit();