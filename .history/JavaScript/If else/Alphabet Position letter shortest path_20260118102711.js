function position(letter) {
    const LETTERS = 'abcdefghijklmnopqrstuvwxyz';
    letter = letter.toLowerCase();

    if (LETTERS.includes(letter)) {
        return `Position of Letter: ${LETTERS.indexOf(letter) + 1}`;
    } else {
        return 'Invalid letter';
    }
}



// ფორ ლუპი ფორ ლოოპ


function position(letter) {
    const LETTERS = 'abcdefghijklmnopqrstuvwxyz';
    letter = letter.toLowerCase();

    for (let i = 0; i < LETTERS.length; i++) {
        if (LETTERS[i] === letter) {
            return `Position of Letter: ${i + 1}`;
        }
    }
    return 'Invalid letter';
}



function position(letter) {
    const LETTERS = 'abcdefghijklmnopqrstuvwxyz';
    letter = letter.toLowerCase();

    if (LETTERS.includes(letter)) {
        return `Position of Letter: ${LETTERS.indexOf(letter) + 1}`;
    }
    else {
        return 'Invalid letter';
    }
}


