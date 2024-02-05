/*
Some classes require a lot of steps to create/initialize a object
and can be initialized in a lot of ways.
One solution is to create a huge constructor and initialize everything.
But sometimes we don't need all the parts of the initializaton for all the objects,

Suppose we are creating a house object, some houses may have a pool, some have a lawn,
but all houses will not have that. So we use builder pattern for this situation.

Builder patterns gives apis to initialize the objects in steps by calling the apis.
*/

class Car {
  seats: number;
  gears: number = 0;
  clutch: boolean = false;
  gpsDevice: string | null;
  carType: string;

  constructor(
    seats: number,
    gears: number,
    gpsDevice: string,
    isAutomatic: boolean = false
  ) {
    this.seats = seats;
    if (seats > 5) {
      this.carType = "SUV";
    } else {
      this.carType = "Sedan";
    }
    if (isAutomatic) {
      this.clutch = true;
      this.gears = gears;
    }
    if (gpsDevice) {
      this.gpsDevice = gpsDevice;
    }
  }
}

/*
In the above class there are so many steps in the constructor.
Let's use builder patter to do this.
*/

class CarNew {
  seats: number;
  gears: number = 0;
  clutch: boolean = false;
  gpsDevice: string | null;
  carType: string;
}

interface ICarBuilder {
  buildSeats(seats: number): void;
  buildGps(gpsDevice: string): void;
  buildGears(gears: number): void;
  getCar(): CarNew;
}

class CarBuilder implements ICarBuilder {
  car: CarNew;
  constructor() {
    this.car = new CarNew();
  }

  buildSeats(seats: number): void {
    this.car.seats = seats;
    if (seats > 5) {
      this.car.carType = "SUV";
    } else {
      this.car.carType = "Sedan";
    }
  }

  buildGears(gears: number): void {
    this.car.gears = gears;
  }

  buildGps(gpsDevice: string): void {
    this.car.gpsDevice = gpsDevice;
  }

  getCar(): CarNew {
    return this.car;
  }
}

class Director {
  builder: ICarBuilder;

  constructor(builder: ICarBuilder) {
    this.builder = builder;
  }

  buildAutoSuvWithGps(): CarNew {
    this.builder.buildSeats(7);
    this.builder.buildGps("gps device");
    return this.builder.getCar();
  }

  buildManualSedan(): CarNew {
    this.builder.buildGears(5);
    this.builder.buildSeats(5);
    return this.builder.getCar();
  }
}
