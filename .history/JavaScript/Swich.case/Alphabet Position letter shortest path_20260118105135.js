

// უფრო მოკლე ფორმა  ეს სხვა პროექტია მარა მეორეზეც შეგხვდებათ ეს სოლუშენი

function position(letter){
    const letter = 'abcdefghijklmnopqrstuvwxyz'
    for (let i = 0; i < letters.length; i++){
        if (letters[i] === letter.toLowerCase()){
            return `Position of Letter: ${i + 1}`
        }
        else{ return 'invalid letter'}
    } 
}