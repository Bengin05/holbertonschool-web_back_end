export default class HolbertonCourse {
    constructor(name, length, students) {
        this._name = name
        this._length = length
        this._students = students
    }
    //Getters
    get name() {
        return this._name;
    }

    get length() {
        return this._length;
    }

    get students() {
        return this._students;
    }
    //Setters with type verification
    set name(value) {
        if (typeof value !== "string") {
            throw new TypeError("Name must be a string");
        }
        this._name = value
    }

    set length(value) {
        if (typeof value !== "number" || Number.isNaN(value)) {
            throw new TypeError("Length must be an integer")
        }
        this._length = value
    }

    set students(value) {
        if (!Array.isArray(value)) {
            throw new TypeError("Students need to be an array");
        }
        for (const student of value) {
            if (typeof student !== "string") {
                throw new TypeError("Student need to be a string");
            }
        }
        this._students = value
    }
}
