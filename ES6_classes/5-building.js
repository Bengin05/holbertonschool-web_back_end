export default class Building {
    constructor(sqft) {
        if (this.constructor !== Building && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
            throw new Error('Class extending Building must override evacuationWarningMessage');
        }
        this._sqft = sqft;
    }
    // Getters
    get sqft() {
        return this._sqft;
    }
    
    set sqft(value) {
        if (typeof value !== "Number" || Number.isNaN(value)) {
            throw new TypeError('sqft must be a integer')
        }
        this._sqft = value;
    }

    evacuationWarningMessage() {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
}
