function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter.toLowerCase());
    return index !== -1 
        ? `Position of Letter: ${index + 1}` 
        : 'Invalid letter';
}


function position(letter) {
    letter = letter.toLowerCase();
    console.log(
        letter === 'a' ? 1 :
        letter === 'b' ? 2 :
        letter === 'c' ? 3 :
        letter === 'd' ? 4 :
        letter === 'e' ? 5 :
        letter === 'f' ? 6 :
        letter === 'g' ? 7 :
        letter === 'h' ? 8 :
        letter === 'i' ? 9 :
        letter === 'j' ? 10 :
        letter === 'k' ? 11 :
        letter === 'l' ? 12 :
        letter === 'm' ? 13 :
        letter === 'n' ? 14 :
        letter === 'o' ? 15 :
        letter === 'p' ? 16 :
        letter === 'q' ? 17 :
        letter === 'r' ? 18 :
        letter === 's' ? 19 :
        letter === 't' ? 20 :
        letter === 'u' ? 21 :
        letter === 'v' ? 22 :
        letter === 'w' ? 23 :
        letter === 'x' ? 24 :
        letter === 'y' ? 25 :
        letter === 'z' ? 26 :
        "არასწორი ასო"
    );
}
 