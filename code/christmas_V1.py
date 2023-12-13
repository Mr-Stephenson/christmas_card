import pygame
import random
import sys
import os

pygame.init()

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
imgAndFontPath = os.path.join(os.path.dirname(script_dir), "images_fonts_music/")

clock = pygame.time.Clock()

pygame.display.set_caption("Christmas card")
info_object = pygame.display.Info()
screen_width = round(info_object.current_h / 1.3)
screen_height = round(info_object.current_h / 1.5)
screen = pygame.display.set_mode((screen_width, screen_height))

christmasTree = pygame.image.load(imgAndFontPath + "christmas_tree.png")
christmasTreeScale = 300
christmasTree = pygame.transform.scale(christmasTree, (round(screen_height / christmasTree.get_height()) * christmasTreeScale, round(screen_width / christmasTree.get_width()) * christmasTreeScale))

ground = pygame.image.load(imgAndFontPath + "ground.png")
groundScale = screen_width / ground.get_width()
ground = pygame.transform.scale(ground, (round(ground.get_width() * groundScale)+15, round(ground.get_height() * groundScale)))

my_font = pygame.font.Font(imgAndFontPath + "FugazOne-Regular.ttf", 45)
textBuffer = screen_width / 20

backgroundMusic = pygame.mixer.music.load(imgAndFontPath + "background_music.wav")
pygame.mixer.music.play(-1)

white = (255, 255, 255)
backgroundColour = (3, 169, 252)
snowflakes = 25
snowflakeInfo = []

for i in range(snowflakes):
  snowflakeInfo.append([random.randint(0, screen_width), random.randint(-screen_height, -20), random.uniform(5,10)])

playing = True

def drawSnowflake(posX, posY, radius):
  snowflakeCoords = (posX, posY)
  pygame.draw.circle(screen, white, snowflakeCoords, radius)

def drawBackground():
  screen.fill(backgroundColour)
  screen.blit(ground, (-5, screen_height - ground.get_height()))
  screen.blit(christmasTree, (screen_width - christmasTree.get_width(), screen_height - christmasTree.get_height() - 50))

  label = my_font.render("Merry Christmas", 1, white)
  label_rect = label.get_rect()
  label_rect.center = (0 + label.get_width() / 2 + textBuffer, screen_height/2)
  screen.blit(label, label_rect)

while playing:
  drawBackground()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

  for i in range(snowflakes):
    drawSnowflake(snowflakeInfo[i][0],snowflakeInfo[i][1],snowflakeInfo[i][2])
  for snowflake in snowflakeInfo:
    if snowflake[2] <= 7:
      snowflake[1] += random.uniform(1.5, 4)
    elif snowflake[2] <=9:
      snowflake[1] += random.uniform(2.5, 5)
    else:
      snowflake[1] += random.uniform(3.5, 5.5)
    if snowflake[1] > screen_height + 20:
      snowflake[1] = -20
      snowflake[0] = random.randint(0, screen_width)
      snowflake[2] = random.uniform(5, 10)
  
  pygame.display.flip()
  clock.tick(60)