let num = 2;
let name = 'Kiril';
let output = name / num;
console.log(output);
console.log(typeof output)
let num2 = '2'
/* let output = name - num;
console.log(output);
console.log(typeof output);

let output = name * num;
console.log(output);
console.log(typeof output);

let output = name / num;
console.log(output);
console.log(typeof output)
 */
console.log(num == num2);
console.log(num === num2);
console.log(num >= num2);
console.log(num <= num2);
console.log(num !== num2);

//Ternary operator (instead of if else)
let result = (0 <= num && num <= 20)
    ? 'in Between'
    : 'not in Between';
console.log(result)


// ARRAYS & Methods

let others = [4, 5, 6]
let more = [1, 2, 3, ...others]
console.log(more)

let numbers = [1, 4, 9];
let roots = numbers.map(function (num, i, arr) {
    return Math.sqrt(num)
});
console.log(roots)
console.table(roots)

let array1 = [5, 12, 8, 130, 44];
let found = array1.find(function (element) {
    return element > 10;
});
console.log(found); // 12

let fruits = ['apple', 'banana', 'grapes', 'mango', 'orange'];
// Filter array items based on search criteria (query)
function filterItems(arr, query) {
    return arr.filter(function (el) {
        return el.toLowerCase().indexOf(query.toLowerCase()) !== -1;
    });
};
console.log(filterItems(fruits, 'ap')); // ['apple', 'grapes']


let matrix = [[1, 2, 3], [4, 5], [6, , 7, 8], [, , , 9]];
console.table(matrix)


const beasts = ['ant', 'bison', 'camel', 'duck', 'bison'];
console.log(beasts.indexOf('bison')); // 1
// start from index 2
console.log(beasts.indexOf('bison', 2)); // 4
console.log(beasts.indexOf('giraffe')); // -1


// array length is 3
// fromIndex is -100
// computed index is 3 + (-100) = -97
let arr = ['a', 'b', 'c'];
arr.includes('a', -100); // true
arr.includes('b', -100); // true
arr.includes('c', -100); // true
arr.includes('a', -2); // false

let fruits2 = ['Banana', 'Orange', 'Lemon', 'Apple'];
let citrus = fruits2.slice(1, 3);
let fruitsCopy = fruits2.slice();
// fruits contains ['Banana', 'Orange', 'Lemon', 'Apple']
// citrus contains ['Orange', 'Lemon']

let elements = ['Fire', 'Air', 'Water'];
console.log(elements.join()); // "Fire,Air,Water"
console.log(elements.join('')); // "FireAirWater"
console.log(elements.join('-')); // "Fire-Air-Water"
console.log(['Fire'].join(".")); // Fire




let nums = [1, 3, 4, 5, 6];
nums.splice(1, 0, 2); // inserts at index 1
console.log(nums); // [ 1, 2, 3, 4, 5, 6 ]
nums.splice(4, 1, 19); // replaces 1 element at index 4
console.log(nums); // [ 1, 2, 3, 4, 19, 6 ]
let el = nums.splice(2, 1); // removes 1 element at index 2
console.log(nums); // [ 1, 2, 4, 19, 6 ]
console.log(el); // [ 3 ]


const items = ['item1', 'item2', 'item3'];
const copy = [];
// For loop
for (let i = 0; i < items.length; i++) {
    copy.push(items[i]);
}
// ForEach
items.forEach(item => { copy.push(item); });


console.clear()
//////////////////////////////////////////////////
let xx = [1, 2, 3, 4, 5, 6, 7, 8, 20];
let yy = [];
xx
    .forEach((num) => {
        // console.log(num)
        yy.unshift(num)
    });
let transformed = xx
    .map((num) => num * 2);
    let even = xx
        .filter((num) => num % 2 === 0);

console.log(xx);
console.log(yy);
console.log(transformed);
console.log(even);

// Mutator methods - ones that change the array: 
// - splice, sort, reverse, push, pop ...

// Access data only methods (don't change the array or create a copy)
// - slice, includes, indexOf ...

//Iteration methods (receive a callback function and go through all elements)
// - forEach, map, filter ...


let text = "010";
console.log(text.padStart(8, '0'));
// Expected output: 00000010

let sentence = "He passed away";
console.log(sentence.padEnd(20, '.'));
// Expected output: He passed away......
