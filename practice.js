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

console.log(assertArraysEqual([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 'arr test'))
