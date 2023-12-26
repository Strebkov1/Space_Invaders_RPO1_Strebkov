import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        '''инициалиция главного героя - космического корабля'''
        self.image = pygame.image.load("image/enemy.png")
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def output_enemy(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.4
        self.rect.y = self.y