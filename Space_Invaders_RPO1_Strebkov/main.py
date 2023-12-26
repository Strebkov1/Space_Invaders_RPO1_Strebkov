import pygame, controls
from hero import Hero
from pygame.sprite import Group
from stats import Stats


def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()
    stats = Stats()
    controls.create_army(screen, enemys)
    
    flag = True
    while flag:
        
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets, enemys)
        controls.moving_bullets(screen, bullets, enemys)

        controls.update_enemys(stats, screen, enemys, bullets, hero)
        screen.blit(pygame.transform.scale(pygame.image.load("image/background.jpg"), (1200,1000)), (0, 0))
        pygame.display.flip()


       
start_game()