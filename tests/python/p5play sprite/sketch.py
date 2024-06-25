from p5 import *


def setup():
  createCanvas(windowWidth,windowHeight)

  a = Sprite(200,200,100,100)
  a.image = "./ada.jpg"
  a.debug = True

def draw():
  background("black")
  drawTickAxes()