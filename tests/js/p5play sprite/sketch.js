function setup() {
  createCanvas(windowWidth, windowHeight);

  const a = new Sprite(200, 200, 100, 100);
  a.image = "./ada.jpg";
  a.debug = true;
}

function draw() {
  background("black");
  drawTickAxes();
}
