import Currency from './3-currency.js';

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount
        this._currency = currency
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
    //Getter
    get amount() {
        return this._amount;
    }

    get currency() {
        return this._currency;
    }
    //Setter with type verification
    set amount(value) {
        if (typeof value !== "number" || Number.isNaN(value)) {
            throw new TypeError("Amount must be an integer")
        }
        this._amount = value;
    }

    set currency(value) {
        if (typeof value !== "object") {
            throw new TypeError("Currency must be an object")
        }
        this._currency = value;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.displayFullCurrency()}`
    } 
}
