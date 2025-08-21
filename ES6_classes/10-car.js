export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Method to clone the current car instance
  cloneCar() {
    // Use the constructor of the current object to create a new instance
    return new this.constructor(this._brand, this._motor, this._color);
  }
}

