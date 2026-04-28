import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        super(sqft)
        this._floors = floors
    }
    // Getters
    get sqft() {
        return this._sqft;
    }

    get floors() {
        return this._floors;
    }
    // Setters with type verification
    set sqft(value) {
        if (typeof value !== "Number" || Number.isNaN(value)) {
            throw new TypeError('sqft must be an integer')
        }
        this._sqft = value;
    }

    set floors(value) {
        if (typeof value !== "Number" || Number.isNaN(value)) {
            throw new TypeError('floors must be an integer')
        }
        this._floors = value;
    }

    evacuationWarningMessage() {
        return `Evacuate slowly the ${this._floors} floors`
    }
}
