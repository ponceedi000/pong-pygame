import pygame

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong Game!')
# Colors to be used in game
white = (255, 255, 255)
black = (0, 0, 0)
green = ( 87, 224, 87)
red = ( 216, 36, 71)
blue = ( 90, 208, 230)
class Paddle(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 75])
    self.rect = self.image.get_rect()
    self.points = 0

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 10])
    self.image.fill(white)
    self.rect = self.image.get_rect()
    self.speed = 3
    self.dx = 1
    self.dy = 1

paddle1 = Paddle()
paddle1.image.fill(blue)
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.image.fill(green)
paddle2.rect.x = 715
paddle2.rect.y = 225

paddle_speed = 10

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

def redraw():
  window.fill(black)
  #Title Font
  font = pygame.font.SysFont('Comic Sans MS', 30)
  text = font.render('PONG', False, white)
  textRect = text.get_rect()
  textRect.center = (750//2, 25)
  window.blit(text, textRect)

  #Player 1 score
  p1_score = font.render(str(paddle1.points), False, blue)
  p1Rect = p1_score.get_rect()
  p1Rect.center = (50, 50)
  window.blit(p1_score, p1Rect)

  #Player 2 score
  p2_score = font.render(str(paddle2.points), False, green)
  p2Rect = p2_score.get_rect()
  p2Rect.center = (700, 50)
  window.blit(p2_score, p2Rect)

  
  all_sprites.draw(window)
  pygame.display.update()

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Game Loop 
run = True
while run:
  # pygame.time.delay(100)
  clock.tick(60)
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

  ball.rect.x += ball.speed * ball.dx
  ball.rect.y += ball.speed * ball.dy


  if ball.rect.y > 490:
    ball.dy = -1

  # Resets ball to middle if it passes through x axis RIGHT wall
  if ball.rect.x > 740:
    ball.rect.x, ball.rect.y = 375, 250
    ball.dx = -1  
    paddle1.points += 1

  if ball.rect.y < 0:
    ball.dy = 1
  # Resets ball to middle if it passes through x axis LEFT wall
  if ball.rect.x < 10:
    ball.rect.x, ball.rect.y = 375, 250
    ball.dx = 1
    paddle2.points += 1


  if paddle1.rect.colliderect(ball.rect):
    ball.dx = 1

  if paddle2.rect.colliderect(ball.rect):
    ball.dx = -1


  redraw()

pygame.quit()