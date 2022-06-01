import pygame

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong Game Title')

white = (255, 255, 255)
black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 75])
    self.image.fill(white)
    self.rect = self.img.get_rect()
    self.points = 0

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 10])
    self.image.fill(white)
    self.rect = self.image.get_rect()





run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()