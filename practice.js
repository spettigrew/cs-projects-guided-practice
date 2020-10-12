// get words into an array


const fs = require('fs');
const words = fs.readFileSync('./words.txt');
const wordsByline = words.toString().split('\r\n')


// print all words with double u

doubles = wordsByline.filter(w => w.includes('UU'))

// find a letter if never doubled

// create a list of doubles found
doubles = []

// iterate a each word
const getDoubleLetters = () => {

  for (let i = 0; i < wordsByline.length; i++) {
    let word = wordsByline[i]
//   check word for a double
    for (let i = 0; i < word.length - 1; i++) {
      if (word[i] === word[i + 1]) {
        if (!doubles.includes(word[i]))
// if a double is found add it to the list
          doubles.push(word[i])
      }
    }
  }
}

// checking to see what letters are not in the list of doubles
getDoubleLetters()

const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

const notDoublesArr = []

const notDoubles = () => {
  for (let i = 0; i < alphabet.length; i++) {
    if (!doubles.includes(alphabet[i])) {
      notDoublesArr.push(alphabet[i])
    }
  }
}

notDoubles()

console.log(notDoublesArr)
