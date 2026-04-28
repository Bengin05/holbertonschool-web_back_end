export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand
        this._motor = motor
        this._color = color
    }

    toString() {
        return this._brand;
    }

    cloneCar() {
        return new this.constructor();
    }
}
