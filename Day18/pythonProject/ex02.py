import pygame

pygame.init();  #pygame 초기화
screen = pygame.display.set_mode((800, 800)); #화면 디스플레이 설정
#이미지 불러오기
character_img = pygame.image.load('Attack(10).png');
character_img = pygame.transform.scale(character_img, (100,100));

clock = pygame.time.Clock();
#캐릭터 변수 선언 및 화면에 이미지 이동
character = character_img.get_rect();
character.left = 300 - character_img.get_width() // 2;
character.top = 800 - character_img.get_height();

while True:
    screen.fill((0,0,0));
    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        break;
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character.left = character.left - 50;
        elif event.key == pygame.K_RIGHT:
            character.right = character.right + 50;
    # 캐릭터가 화면 왼쪽을 벗어나는 것을 방지
    if character.left < 0:
        character.left = 0;
    # 캐릭터가 화면 오른쪽으로 벗어나는 것을 방지
    if character.right > 800:
        character.right = 800;
    screen.blit(character_img, character);
    pygame.display.update();
    clock.tick(30);
pygame.quit();