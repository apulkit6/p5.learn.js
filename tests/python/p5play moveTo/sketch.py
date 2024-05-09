from p5 import *


def setup():
  global player
  createCanvas(windowWidth, windowHeight)

  player = Sprite()
  player.diameter = 70

def draw():
  global player

  clear()
  player.moveTo(mouse.x, mouse.y)