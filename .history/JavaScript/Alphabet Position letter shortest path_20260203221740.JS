// Alphabet Position letter shortest path
// ubdate later
// 9  ARR
// 10 Arrow function  
// helper functions

// May 2026, 2020, New update Arrow function in JavaScript New projects version with arrow function and arrays and also arrow function and array together

// 8  TERNARY OPERATOR
// 7  IF ELSE
// 6  SWICH CASE 
// 5  FOR LOOP
// 4  RETURN 
// 3  to work on the website
// 2  Object
// 1  Object IF ELSE



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


// 1 TERNARY OPERATOR

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter);
    return index !== -1 ? `Position of Letter: ${index + 1}` : 'Invalid letter';
}

// 2 IF ELSE

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter);

    if (index !== -1){
        return `Position of Letter: ${index + 1}`
    } else {
        return 'invalid letter'
    }
}

// 3 SWICH CASE 

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter);

    switch (index !== -1) {
        case true:
            return `Position of Letter: ${index + 1}`
        case false:
            return 'Invalid letter'
    }
}

// 4 FOR LOOP

function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    
    for (let i = 0; i < letters.length; i++) {
        if (letters[i] === letter) {
            return `Position of Letter: ${i + 1}`;
        }
    }
    
    return 'Invalid letter';
}

// 5 ნTERNARY OPERATOR Object   

const lettersMap = {
    a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7,
    h: 8, i: 9, j: 10, k: 11, l: 12, m: 13, n: 14,
    o: 15, p: 16, q: 17, r: 18, s: 19, t: 20,
    u: 21, v: 22, w: 23, x: 24, y: 25, z: 26
};

function position(letter) {
    return lettersMap[letter] 
        ? `Position of Letter: ${lettersMap[letter]}` 
        : 'Invalid letter';
}

// 6 Object IF ELSE

{
const lettersMap = {
    a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7,
    h: 8, i: 9, j: 10, k: 11, l: 12, m: 13, n: 14,
    o: 15, p: 16, q: 17, r: 18, s: 19, t: 20,
    u: 21, v: 22, w: 23, x: 24, y: 25, z: 26
};

function position(letter) {
    if (lettersMap[letter]) {
        return `Position of Letter: ${lettersMap[letter]}`;
    } else {
        return 'Invalid letter';
    }
}
}

აკლია

12) ternary opoerator Object /
11) ARR
10) Arrow function  
9)  helper functions
8)  TERNARY OPERATOR /
7)  IF ELSE
6)  SWICH CASE 
5)  FOR LOOP /
4)  RETURN 
3)  to work on the website
2)  Object

