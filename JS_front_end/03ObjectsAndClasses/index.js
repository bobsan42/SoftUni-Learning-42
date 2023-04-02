function personInfo(firstName, lastName, age) {
    let person = {};
    person.firstName = firstName;
    person.lastName = lastName;
    person.age = age;
    person.grades = [5, 6, 4.5]
    console.log(person);
    return person;

}
function personInfo2(firstName, lastName, age) {
    age = Number(age);
    let person = { firstName: firstName, lastName: lastName, age: age };

    return person;

}

function personInfo3(firstName, lastName, age) {
    age = Number(age);
    let person = { firstName, lastName, age };

    return person;

}
// console.log(personInfo3("Peter",
//     "Pan",
//     20
// ));

function cityInfo(city) {
    let entries = Object.entries(city);
    for (let [key, value] of entries) {
        console.log(`${key} -> ${value}`);
    }
}

function personInfo4(firstName, lastName, age) {
    age = Number(age);
    let person = {
        firstName,
        lastName,
        age,
        sayHello: function () {
            return `Hello ${this.firstName} ${this.lastName}`
        }
    };
    // console.log(person.sayHello())
    return person;

};


console.log(personInfo4("Peter",
    "Pan",
    20).sayHello()

)
let person = {
    firstName: 'Jack',
    lastName: 'Sparrow',
    age: 42,
    sayHello: function () {
        return `Hello ${this.firstName} ${this.lastName}`
    }
};
// console.log(Object.keys(person));

// const keys = Object.keys(person);
// for (const key of keys) {
//     console.log(`Key: ${key}`)
//     console.log(`Value: ${person[key]}`)
// };

// const tuples = Object.entries(person); //
// for (const [key, value] of tuples) {
//     console.log(`Key: ${key}`)
//     console.log(`Value: ${value}`)
// };

const tuples = Object.entries(person)
    .forEach(([key, value]) => console.log(key, value));


let person2 = {
    firstName: "John",
    lastName: "Doe",
    age: function (myAge) {
        return `My age is ${myAge}!`
    }
};
console.log(person2.age(21)); // My age is 21!


// sorting helper
const compareNumbers = {
    ascending: (a, b) => a - b,
    descending: (a, b) => b - a,
  };
  
// Objects as switch replacement
// You will almost never see switch used in JS code
// Named methods are used instead

// let count = 5;
// switch (command) {
//   case 'increment':
//     count++;
//     break;
//   case 'decrement':
//     count--;
//     break;
//   case 'reset':
//     count = 0;
//     break;
// }

let count = 5;
const parser =  {
  increment() { count++; },
  decrement() { count--; },
  reset() { count = 0; }
}
console.log(parser.increment());







