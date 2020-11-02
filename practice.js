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

// console.log(notDoublesArr)


// Enter your code here
let myArray = []
myArray.push('Jess Bonanno', 'Red')

const cutName = (name) => {
  return name.split(' ');
}

let myInfo = {}
myInfo.fullName = cutName(myArray[0])
myInfo.favoriteColor = myArray[1]
myInfo.github = 'https://github.com/JessBonanno'

function countAllCharacters(str) {
  // your code here
  let obj = {}
  for (const letter in str) {
    if (!obj[str[letter]]) {
      obj[str[letter]] = 1
    } else {
      obj[str[letter]] += 1
    }
  }
  return obj
}

// console.log(countAllCharacters('banana'))

function transformEmployeeData(employeeData) {
  // your code here
  result = []
  let count = 0
  employeeData.map(employee => {
    result.push({})
    employee.map(data => {
      let key = data[0]
      console.log(key)
      let val = data[1]
      result[count][key] = val
    })
    count += 1
  })
  return result
}

//
// console.log(transformEmployeeData([
//   [
//     ['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']
//   ],
//   [
//     ['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']
//   ]
// ]))


function convertObjectToArray(obj) {
  // your code here
  let result = []
  for (const pair in obj) {
    result.push([pair, obj[pair]])
  }
  return result
}

// console.log(convertObjectToArray({
//   name: 'Holly',
//   age: 35,
//   role: 'producer'
// }))


var customerData = {
  'Joe': {
    visits: 1
  },
  'Carol': {
    visits: 2
  },
  'Howard': {
    visits: 3,
  },
  'Carrie': {
    visits: 4
  }
};

function greetCustomer(firstName) {
  // your code here
  let output = ''
  if (!customerData.hasOwnProperty(firstName)) {
    output = `Welcome! Is this your first time?`
  } else if (customerData[firstName].visits === 1) {
    output = `Welcome back,  ${firstName}! We're glad you liked us the first time!`
  } else {
    output = `Welcome back,  ${firstName}! So glad to see you again!`
  }
  console.log(output)
}

// console.log(greetCustomer('Terance'))

var users = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  }
];

const generateSampleView = (usersArray) => {
  let output = []
  usersArray.map(user => {
    if (user.id % 2 != 0) {
      output.push(user.email)
    } else {
      const userString = `${user.address.street}, ${user.address.suite}, ${user.address.city}, ${user.address.zipcode}`
      output.push(userString)
    }
  })
  return output
}

// const assertArraysEqual = (actual, expected, testName) => {
//   if (actual === expected) {
//     return `passed ${testName}`
//   } else {
//     return `failed ${testName}`
//   }
// }

const assertArraysEqual = (actual, expected, testName) => {
  if (actual.length === expected.length) {
    for (let i = 0; i < actual.length; i++) {
      if (!expected.includes(actual[i])) {
        console.log(`failed ${testName}`)
        return
      }
    }
    console.log(`passed ${testName}`)
  }
}

// console.log(assertArraysEqual([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 'arr test'))


function average(numbers) {
  // uses sum function
  const sumOfNums = sum(numbers)
  // returns the average of an array of numbers
  return sumOfNums / numbers.length
}

function sum(numbers) {
  // returns the sum of an array of numbers
  let sumOfNums = 0
  numbers.map(num => {
    sumOfNums += num
  })
  return sumOfNums
}

// console.log(sum([1,2,3,4,5]))
// console.log(average([1,2,3,4,5]))


var classList = ["Joe", "Jack", "John", "Fred", "Frank", "Barry", "Larry", "Mary",
  "Harry", "Farrell", "Susan", "Monica", "Keira", "Caroline", "Harriet", "Erica",
  "Luann", "Cheryl", "Beth", "Rupa", "Linda", "Allison", "Nancy", "Dora"];

// FUNCTION DEFINITION(S)

// USE THIS FUNCTION TO GENERATE A RANDOM NUMBER
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


function decorateClassListWithAges(classList) {
  let result = []
  // creates an object for each string in the input array, with an age of 10 or 11
  // returns an array of these objects
  classList.map(item => {
    result.push({
      name: item,
      age: getRandomIntInclusive(10, 11)
    })
  })
  return result
}

// console.log(decorateClassListWithAges(classList))
// ASSERTION FUNCTION(S) TO BE USED

// TESTS CASES


// Skeleton

// FUNCTION DEFINITION(S)
function isIsogram(text) {
  // add each char to a set
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
  // note: a set drops dup values
  // thus, to see if all the chars were unique,
  // check length of text and the size of the set
  let singles = new Set(text.toLowerCase())
  console.log(singles)
  console.log(singles.size)
  console.log(text.length)
  if (singles.size === text.length || text === '') {
    return true
  } else {
    return false
  }
}

// console.log(isIsogram('cat'))


// Skeleton

// FUNCTION DEFINITION(S)
function findMaxRepeatCountInWord(word) {
  // Break up individual word into individual letters.
  // Count the instances of each letter
  // Iterate all the counts and find the highest
  // Return this word's max repeat count
  const repeats = {}
  for (const char in word) {
    if (!repeats[word[char]]) {
      repeats[word[char]] = 1
    } else {
      repeats[word[char]] += 1
    }
  }
  let letter = ''
  let highest = 0
  for (let repeat in repeats) {
    if (repeats[repeat] > highest) {
      highest = repeats[repeat]
      letter = repeat
    }
  }
  const result = {}
  result[letter] = highest
  return highest
}

// console.log(findMaxRepeatCountInWord('hellooo'))

function findFirstWordWithMostRepeatedChars(text) {
  var maxRepeatCountOverall = 0;
  var wordWithMaxRepeatCount = '';

  // Break up input text into words (space-delimited).
  const wordsList = text.split(' ')
  // For each word...
  for (word in wordsList) {
    // If that max repeat count is higher than the overall max repeat count, then
    // update maxRepeatCountOverall
    // update wordWithMaxRepeatCount
    var repeatCountForWord = findMaxRepeatCountInWord(wordsList[word])
    if (maxRepeatCountOverall < repeatCountForWord) {
      maxRepeatCountOverall = repeatCountForWord
      wordWithMaxRepeatCount = wordsList[word]
    }
  }

  return wordWithMaxRepeatCount;
}

// console.log(findFirstWordWithMostRepeatedChars('this sentence is a tester' +
//   ' for repeated characters'))


// Skeleton

// FUNCTION DEFINITION(S)
function PhoneNumberFormatter(numbers) {
  this.numbers = numbers;
}

PhoneNumberFormatter.prototype.render = function () {
  console.log('test')
  var string = '';
  // your code here
  string = `${this.parenthesize(this.getAreaCode())} ${this.getExchangeCode()}-${this.getLineNumber()}`
  return string;
};

PhoneNumberFormatter.prototype.getAreaCode = function () {
  // your code here
  return this.numbers.slice(0, 3).join('')

};

PhoneNumberFormatter.prototype.getExchangeCode = function () {
  // your code here
  return this.slice(3, 6)
};

PhoneNumberFormatter.prototype.getLineNumber = function () {
  // your code here
  return this.slice(6, this.numbers.length)
};

PhoneNumberFormatter.prototype.parenthesize = function (string) {
  return '(' + string + ')';
};

PhoneNumberFormatter.prototype.slice = function (start, end) {
  return this.numbers.slice(start, end).join('');
};

// ASSERTION FUNCTION(S) TO BE USED

// TESTS CASES

// let numbers = [6, 5, 0, 8, 3, 5, 9, 1, 7, 2]
//
// let myNumber = new PhoneNumberFormatter(numbers)
// console.log(myNumber.render())


// Skeleton

// FUNCTION DEFINITION(S)
function findLongestPalindrome(sentence) {
  // split sentence into words
  const words = sentence.split(' ')
  // iterate words and collect the palindromes
  const pal = words.filter(word => {
    if (isPalindrome(word.toLowerCase())) {
      return word
    }
  })
  // sort the list of palindromes by word length
  pal.sort(sortAscendingByLength)
  // return the largest item in the sorted list
  return pal[pal.length - 1]
}


function reverseString(string) {
  return string.split('').reverse().join('').toLowerCase()
}

function isPalindrome(word) {
  // hint: you can detect palindromes by comparing a string to its reverse
  if (word.toLowerCase() === reverseString(word)) {
    return true
  } else {
    return false
  }
}

function sortAscendingByLength(a, b) {
  if (a.length > b.length) {
    return 1;
  } else if (a.length < b.length) {
    return -1;
  }
  return 0;
}


const sentence = 'Mom makes lunch at noon on racecar plates wow'
// ASSERTION FUNCTION(S) TO BE USED
// console.log(findLongestPalindrome(sentence))
// TESTS CASES


/*
* Fashion Inventory Part-A
Write a function that will take in this currentInventory array as its argument. Your function should access all the shoes across each designer and return them out in a flat list: {designer name} - {shoe name} - {price}{designer name} - {shoe name} - {price}

//...console output:
Brunello Cucinelli, tasselled black low-top lace-up, 1000
Brunello Cucinelli, tasselled green low-top lace-up, 1100
// and so on...
Here is an example of a flat list in code:

var flatList = "First line\nSecond Line\nThird Line\n";
console.log(flatList);
Observe that a "flat list" refers to a string where each new line is separated by the newline symbol. Also note that the "flat list" ends with a newline symbol. There are, like all of the challenges in this course, tests attached to these exercises. However, in order to get the most effective practice, please continue to write your own unit tests.

Hint: the return value is a string. */

var currentInventory = [
  {
    name: 'Brunello Cucinelli',
    shoes: [
      {name: 'tasselled black low-top lace-up', price: 1000},
      {name: 'tasselled green low-top lace-up', price: 1100},
      {name: 'plain beige suede moccasin', price: 950},
      {name: 'plain olive suede moccasin', price: 1050}
    ]
  },
  {
    name: 'Gucci',
    shoes: [
      {name: 'red leather laced sneakers', price: 800},
      {name: 'black leather laced sneakers', price: 900}
    ]
  }
];

function renderInventory(inventory) {
  let flatList = ''
  inventory.map(designer => {
    designer.shoes.map(shoe => {
      flatList += `${designer.name}, ${shoe.name}, ${shoe.price}\n`
    })
  })
  return flatList
}

//Create helper functions if needed
// console.log(renderInventory(currentInventory))


/*
* Fashion Inventory Part-B
Your function should return the average cost of all shoes per designer in this format:

var expected = {
  'designers': [
    {
      'name': 'Brunello Cucinelli',
      'averagePrice': 1025
    },
    {
      'name': 'Gucci',
      'averagePrice': 850
    }
  ]
};
There are, like all of the challenges in this course, tests attached to these exercises. However, in order to get the most effective practice, please continue to write your own unit tests. */


function calculateAveragePricePerDesigner(inventory) {
  let averagePrices = {
    'designers': []
  }
  inventory.map(designer => {
    let priceTotals = 0
    designer.shoes.map(shoe => {
      priceTotals += shoe.price
    })
    averagePrices.designers.push({
      'name': designer.name,
      'averagePrice': priceTotals / designer.shoes.length
    })
  })
  return averagePrices
}

// Create helper functions if needed


// console.log(calculateAveragePricePerDesigner(currentInventory))


/*

You have a fashion catalog, an inventory of items from various high-fashion designers. Each designer has a lineup of shoes. Each shoe has a name and a price.

It looks like this:

var currentInventory = [
  {
    name: 'Brunello Cucinelli',
    shoes: [
      {name: 'tasselled black low-top lace-up', price: 1000},
      {name: 'tasselled green low-top lace-up', price: 1100},
      {name: 'plain beige suede moccasin', price: 950},
      {name: 'plain olive suede moccasin', price: 1050}
    ]
  },
  {
    name: 'Gucci',
    shoes: [
      {name: 'red leather laced sneakers', price: 800},
      {name: 'black leather laced sneakers', price: 900}
    ]
  }
];
1
Fashion Inventory Part-C
Your task is to find all of the shoes with "black" in the name. Your function should filter these shoes, and return them in a "flat list" similarly to Part A. Here is an example of the console output:

Brunello Cucinelli, tasselled black low-top lace-up, 1000
Gucci, black leather laced sneakers, 900
Here is an example of a flat list in code:

var flatList = "First line\nSecond Line\nThird Line\n";
console.log(flatList);
Observe that a "flat list" refers to a string where each new line is separated by the newline symbol. Also note that the "flat list" ends with a newline symbol. There are, like all of the challenges in this course, tests attached to these exercises. However, in order to get the most effective practice, please continue to write your own unit tests.*/

function listAllBlackShoes(inventory) {
  let flatBlackList = ''
  inventory.map(designer => {
    designer.shoes.map(shoe => {
      if (shoe.name.includes('black')) {

        flatBlackList += `${designer.name}, ${shoe.name}, ${shoe.price}\n`
      }
    })
  })
  return flatBlackList
}

// console.log(listAllBlackShoes(currentInventory))


/*
*  The task now is to find all the laced shoes, but we are going to render them in a somewhat complex format. Your function should return shoe names that contain "lace" in them, and indicate which word contains "lace". The return value's format should be structured like this:

var expectedResult = [
  {
    "nameWords": [
      "tasselled",
      "black",
      "low-top",
      "lace-up"
    ],
    "targetWordIndex": 3
  },
  {
    "nameWords": [
      "tasselled",
      "green",
      "low-top",
      "lace-up"
    ],
    "targetWordIndex": 3
  },
  {
    "nameWords": [
      "red",
      "leather",
      "laced",
      "sneakers"
    ],
    "targetWordIndex": 2
  },
  {
    "nameWords": [
      "black",
      "leather",
      "laced",
      "sneakers"
    ],
    "targetWordIndex": 2
  }
];
There are no tests attached to this exercise. In order to get the most effective practice, please continue to write your own unit tests.*/

// create everything for this problem, functions, assertion function, and test cases
// call your function "generateLaceDetails", and let it take the inventory as its parameter


function listLacedShoes(inventory) {
  let lacedShoes = []
  inventory.map(designer => {
    designer.shoes.map(shoe => {
      if (shoe.name.includes('lace')) {
        let shoes = shoe.name.trim().split(' ')
        let laceIndex
        shoes.map(str => {
          if (str.includes('lace')) {
            console.log(str)
            laceIndex = shoes.indexOf(str)
          }
        })
        lacedShoes.push({
          'nameWords': shoes,
          'targetWordIndex': laceIndex
        })
      }
    })
  })
  return lacedShoes
}

console.log(listLacedShoes(currentInventory))
