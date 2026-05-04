export default function cleanset(set, startString) {
    if (!startString || typeof startString !== 'string') {
        return '';
    }
    if (!(set instanceof Set)) {
        return '';
    }
    const result = [];
    for (const value of set) {
        if (typeof value === 'string' && value.startsWith(startString)) {
            result.push(value.slice(startString.length));
        }
    }
    return result.join('-');
}
