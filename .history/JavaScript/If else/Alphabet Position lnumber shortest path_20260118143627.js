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

let number = prompt("Enter a number (1-26): ");
console.log(position(number));



