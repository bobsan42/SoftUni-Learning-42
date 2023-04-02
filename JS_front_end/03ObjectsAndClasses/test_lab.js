let count = 5;
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

const comamndParser = {
    increment: (count) => ++count,
    decrement: (count) => --count,
    reset: () => 0
}
// count = comamndParser.increment(count);
// console.log(count)
// count = comamndParser.decrement(count);
// console.log(count)
// count = comamndParser.reset();
// console.log(count)


// Sort Address Book

function solve(input) {
    let addressbook = {};
    for (let line of input) {
        let [name, address] =
            line.split(':'); addressbook[name] = address;
    }
    let sorted = Object.entries(addressbook);
    sorted.sort((a, b) => a[0].localeCompare(b[0]));
    // console.log(sorted[0])
    // console.log(sorted[1])
    // console.log(sorted[2])

    // TODO: Print result
}

solve(['Tim:Doe Crossing',
    'Bill:Nelson Place',
    'Peter:Carlyle Ave',
    'Bill:Ornery Rd']
)

// Find in array
// let person = { name: 'Kiril' };
// let arr = [person, { name: 'Peter' }, { name: 'Georgi' }];
// let indexOfFound = arr.findIndex((p) => p.name === person.name);
// console.log(arr[indexOfFound]);
// let found = arr.find((p) => p.name === person.name);
// console.log(found);

// Sorting objects
let people = {
    ZKiril: { age: 25, email: 'kiro@gmail.com' },
    Peter: { age: 3, email: 'pesho@gmail.com' },
    Georgi: { age: 21, email: 'zgosho@gmail.com' },
}
const entries = Object.entries(people);
// for (const [name, info] of entries) {
//     console.log(name);
//     console.log(info);
// }
// console.log(entries);
let sortedByName = entries.sort((personA, personB) => {
    // let namePersonA = personA[0];
    // let namePersonB = personB[0];
    let namePersonA = personA[1].email;
    let namePersonB = personB[1].email;
    return namePersonA.localeCompare(namePersonB);
    // console.log()
}).reverse();
for (const [name, info] of sortedByName) {
    console.log(name);
    console.log(info);
}
console.log('#'.repeat(30))
let sortedByAge = entries.sort((personA, personB) => {
    // let namePersonA = personA[0];
    // let namePersonB = personB[0];
    let agePersonA = personA[1].age;
    let agePersonB = personB[1].age;
    return agePersonA - agePersonB;
    // console.log()
});
for (const [name, info] of sortedByName) {
    console.log(name);
    console.log(info);
}

// Destructuring arrays and objects
// Thedestructuring assignmentsyntax makes it possible to unpack
// values from arrays, or properties from objects, 
// into distinct variables.
// Оn the left - hand side of the assignment to define what 
// values to unpack from the sourced variable.
const x = [1, 2, 3, 4, 5];
const [y, z] = x;
console.log(y); // 1
console.log(z); // 2


obj = { a: 1, b: 2 };
const { a, b } = obj;
// is equivalent to:
// const a = obj.a;
// const b = obj.b;

// To sort by value, use the second element of each entry
entries.sort((a, b) => {
    valueA = a[1];
    valueB = b[1];
    // Perform comparison and return negative, 0 or positive
  });
//   You can also destructure the entries
entries.sort(([keyA, valueA],[keyB, valueB]) => {
    // Perform comparison and return negative, 0 or positive
  });


