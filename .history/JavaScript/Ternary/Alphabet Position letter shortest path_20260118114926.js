function position(letter) {
    const letters = 'abcdefghijklmnopqrstuvwxyz';
    const index = letters.indexOf(letter.toLowerCase());
    return index !== -1 
        ? `Position of Letter: ${index + 1}` 
        : 'Invalid letter';
}
