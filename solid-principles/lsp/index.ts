/*
If you use a base class/interface and you put a derived class then 
everything should work
*/

class Rectangle {
  height: number;
  width: number;

  constructor(height: number, width: number) {
    this.height = height;
    this.width = width;
  }

  area(): number {
    return this.height * this.width;
  }
}

function printAreaOfRectange(r: Rectangle) {
  console.log(r.area());
}

const r = new Rectangle(2, 5);

printAreaOfRectange(r);
/*
If we substitute with a derived class Square it should work
*/

class Square extends Rectangle {
  constructor(side: number) {
    super(side, side);
  }
}

const s = new Square(5);

printAreaOfRectange(s);
