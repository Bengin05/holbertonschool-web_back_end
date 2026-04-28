export class ClassRoom {
    constructor(maxStudentsSize) {
        this._maxStudentsSize = maxStudentsSize;
    }
}

function initializeRooms() {
    const sizes = [19,20,34];
    const newArr = sizes.map(size => new ClassRoom(size));
    return newArr
}

export default initializeRooms
