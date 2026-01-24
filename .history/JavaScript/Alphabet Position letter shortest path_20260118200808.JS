// Alphabet Position letter shortest path
// TERNARY OPERATOR
// IF ELSE
// SWICH CASE 
// FOR LOOP
// RETURN 
// to work on the website


// PHYTON WERSION      Alphabet Position letter shortest path

// def position(letter):
//     Letter = 'abcdefghijklmnopqrstuvwxyz'
//     count = 0
//     for i in Letter:
//         if i == letter:
//             return f'Position of Letter: {count + 1}'
//         count += 1
//     return 'Invalid letter'


// letter = input("Enter a letter: ").lower()
// print(position(letter))


// TERNARY OPERATOR

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter);
    return index !== -1 ? `Position of Letter: ${index + 1}` : 'Invalid letter';
}

let letter = prompt("Enter a letter:").toLowerCase();
console.log(position(letter));


// IF ELSE

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter);

    if (index !== -1){
        return `Position of Letter: ${index + 1}`
    }
}