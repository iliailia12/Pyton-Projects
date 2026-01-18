function position(number) {
    let Letter = 'abcdefghijklmnopqrstuvwxyz';
    let count = 1;
    for (let i of Letter) {
        if (String(count) === number) {
            return `Letter at position ${number}: ${i}`;
        }
        count += 1;
    }
    return 'Invalid number';
}


// იფ ელსით