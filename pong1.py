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
    self.rect = self.image.get_rect()
    self.points = 0

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 10])
    self.image.fill(white)
    self.rect = self.image.get_rect()
    self.speed = 10
    self.dx = 1
    self.dy = 1

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

paddle_speed = 50

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

def redraw():
  window.fill(black)
  all_sprites.draw(window)
  pygame.display.update()






run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  key = pygame.key.get_pressed()
  # Handles verticle movement of left paddle
  if key[pygame.K_w]:
    paddle1.rect.y += -paddle_speed
  if key[pygame.K_s]:
    paddle1.rect.y += +paddle_speed

  # Handles verticle movement of right paddle
  if key[pygame.K_UP]:
    paddle2.rect.y += -paddle_speed
  if key[pygame.K_DOWN]:
    paddle2.rect.y += +paddle_speed

  ball.rect.x += ball.speed 
  ball.rect.y += ball.speed

  redraw()

pygame.quit()