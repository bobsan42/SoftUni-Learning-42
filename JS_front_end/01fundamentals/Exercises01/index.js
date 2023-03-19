// 1.	Ages
// Write a function that determines whether based on the given age a person is: baby, child, teenager, adult, elder.
// The input comes as a single number parameter. The bounders are:
// ·	0-2 (age) – is a baby;   
// ·	3-13 (age) – is a child; 
// ·	14-19 (age) – is a teenager;
// ·	20-65 (age) – is an adult;
// ·	>=66 (age) – is an elder; 
// ·	In all other cases print – "out of bounds";
// The output should be printed to the console.

function ages(age) {
    let result;
    if (0 <= age && age <= 2) {
        result = 'baby';
    } else if (3 <= age && age <= 13) {
        result = 'child';
    } else if (14 <= age && age <= 19) {
        result = 'teenager';
    } else if (20 <= age && age <= 65) {
        result = 'adult';
    } else if (66 <= age) {
        result = 'elder';
    } else {
        result = 'out of bounds'
    }
    console.log(result);
}

// ages (29)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 2.	Vacation
// You are given a group of people, the type of the group, and the day of the week they are going to stay. 
// Based on that information calculate how much they have to pay and print that price on the console. 
// Use the table below. In each cell is the price for a single person. 
// The output should look like that: `Total price: {price}`. The price should be formatted to the second decimal point.

function vacation(guestsCount, groupType, dayOfTheWeek) {
    let unitPrice = 0;
    let discount = 0;
    let totalPirce = 0;
    if (dayOfTheWeek == 'Friday') {
        if (groupType == 'Students') {
            unitPrice = 8.45
        } else if (groupType == 'Business') {
            unitPrice = 10.90
        } else if (groupType == 'Regular') {
            unitPrice = 15
        }
    } else if (dayOfTheWeek == 'Saturday') {
        if (groupType == 'Students') {
            unitPrice = 9.80
        } else if (groupType == 'Business') {
            unitPrice = 15.60
        } else if (groupType == 'Regular') {
            unitPrice = 20
        }
    } else if (dayOfTheWeek == 'Sunday') {
        if (groupType == 'Students') {
            unitPrice = 10.46
        } else if (groupType == 'Business') {
            unitPrice = 16
        } else if (groupType == 'Regular') {
            unitPrice = 22.50
        }
    }

    totalPirce = guestsCount * unitPrice;
    //discounts
    if (groupType == 'Students' && guestsCount >= 30) {
        totalPirce = .85 * guestsCount * unitPrice;
    } else if (groupType == 'Business' && guestsCount >= 100) {
        totalPirce = (guestsCount - 10) * unitPrice;
    } else if (groupType == 'Regular' && 10 <= guestsCount && guestsCount <= 20) {
        totalPirce = .95 * guestsCount * unitPrice;
    }
    console.log(`Total price: ${totalPirce.toFixed(2)}`)

}

// vacation(30,
//     "Regular",
//     "Saturday"
// )

// vacation(40,
//     "Regular",
//     "Saturday"
// )
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 3.	Leap Year
// Write a JS function to check whether a year is a leap. Leap years are either divisible by 4 but not by 100 or are divisible by 400. The output should be following:
// •	If the year is a leap, print: "yes"
// •	Otherwise, print: "no"

function leapYear(year) {
    let result = 'no'
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
        result = 'yes'
    }
    console.log(result)
}
// leapYear(1984);
// leapYear(2003);
// leapYear(2300);

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 4.	Print and Sum
// Write a function that displays numbers from given start to given end and their sum. 
// The input comes as two number parameters. Print the result like the examples below:
// 5 6 7 8 9 10
// Sum: 45
function printAndSum(start, end) {
    let totalSum = 0;
    let numbers = [];
    for (let i = start; i <= end; i++) {
        numbers.push(i);
        totalSum += i;
    }
    console.log(numbers.join(' '));
    console.log(`Sum: ${totalSum}`);
}

// printAndSum(5,10);
// printAndSum(0,26);
// printAndSum(50,60);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 5.	Multiplication Table
// You will receive a number as a parameter. Print the 10 times table for this number. See the examples below for more information.
// Output
// Print every row of the table in the following format:
// {number} X {times} = {product}
// Constraints
// ·	The number will be an integer will be in the interval [1…100]

function multiplicationTable(num) {
    for (let i = 1; i <= 10; i++) (
        console.log(`${num} X ${i} = ${i * num}`)
    )
}

// multiplicationTable (5);

// 6.	Sum Digits
// Write a function, which will be given a single number. Your task is to find the sum of its digits.
function sumDigits(num) {
    let digitsSum = 0;
    let numberToText = String(num);
    for (let dig of numberToText) {
        digitsSum += Number(dig);
    }
    console.log(digitsSum);

}

// sumDigits (245678);

// 7.	Chars to String
// Write a function, which receives 3 parameters. Each parameter is a single character. 
// Combine all the characters into one string and print it on the console.

function charsToString(...chars) {
    console.log(chars.join(''))
}

// charsToString('B','4','2')

// 8.	Reversed Chars
// Write a program that takes 3 parameters (characters) and prints them 
// in reversed order with a space between them.

function reversedJoin(...chars) {
    console.log(chars
        .reverse()
        .join(' '))
}
// reversedJoin('B','4','2')
// 9.	Fruit
// Write a function that calculates how much money you need to buy fruit. 
// You will receive a string for the type of fruit you want to buy, 
// a number for weight in grams, and another number for the price per kilogram. 
// Print the following text on the console:  
// `I need ${money} to buy {weight} kilograms {fruit}.`
// Print the weight and the money rounded to two decimal places.
// The input comes as three arguments passed to your function.
// The output should be printed on the console.

function moneyForFruits(fruit, weightInGrams, pricePerKilo) {
    let weight = weightInGrams / 1000;
    let money = weight * pricePerKilo;
    console.log(`I need $${money.toFixed(2)} to buy ${weight.toFixed(2)} kilograms ${fruit}.`)
}
// moneyForFruits('orange', 2500, 1.80)

// 10.	Same Numbers
// Write a function that takes an integer number as an input 
// and check if all the digits in a given number are the same or not.
// Print on the console true if all numbers are the same and false if not. 
// On the next line print the sum of all digits.
// The input comes as an integer number.
// The output should be printed on the console.

function checkSameDigits(num) {
    let numberToText = String(num);
    let digitsSum = 0;
    let firstDigit = numberToText[0];
    let sameDigits = true;
    for (let dig of numberToText) {
        if (dig !== firstDigit) {
            sameDigits = false;
        }
        digitsSum += Number(dig);
    }
    console.log(sameDigits);
    console.log(digitsSum);
}

// checkSameDigits (2222222);
// checkSameDigits(121111);

// 11.	Road Radar
// Write a function that determines whether a driver is within the speed limit. 
// You will receive the speed and the area. Each area has a different limit: 
// •	On the motorway, the limit is 130 km/h
// •	On the interstate, the limit is 90 km/h
// •	In the city, the limit is 50 km/h 
// •	Within a residential area, the limit is 20 km/h
// If the driver is within the limits, there should be a printed speed and the speed limit. 
//                 `Driving {speed} km/h in a {speed limit} zone`
// If the driver is over the limit, however, 
// your function should print the severity of the infraction and the difference in speeds. 
// `The speed is {difference} km/h faster than the allowed speed of {speed limit} - {status}`
// For speeding up to 20 km/h over the limit, the status should be speeding.
// For speeding up to 40 km/h over the limit, the status should be excessive speeding.
// For anything else, status should be reckless driving.
// The input comes as 2 string parameters. 
// The first element is the current speed (number), the second element is the area.
// The output should be printed on the console.

function roadRadar(speed, area) {
    let speedLimits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    }
    if (speed <= speedLimits[area]) {
        console.log(`Driving ${speed} km/h in a ${speedLimits[area]} zone`)
    } else {
        let diff = speed - speedLimits[area];
        let status = 'speeding';
        if (diff > 20 && diff <= 40) {
            status = 'excessive speeding';
        } else if (diff > 40) {
            status = 'reckless driving'
        }
        console.log(`The speed is ${diff} km/h faster than the allowed speed of ${speedLimits[area]} - ${status}`)
    }
}

// roadRadar(40, 'city');
// roadRadar(21, 'residential');
// roadRadar(120, 'interstate');
// roadRadar(200, 'motorway');

// 12.	Cooking by Numbers
// Write a program that receives 6 parameters which are a number and a list of five operations. 
// Perform the operations sequentially by starting with the input number 
// and using the result of every operation as a starting point for the next one. 
// Print the result of every operation in order. The operations can be one of the following:
// •	chop - divide the number by two
// •	dice - square root of a number
// •	spice - add 1 to the number
// •	bake - multiply number by 3
// •	fillet - subtract 20% from the number
// The input comes as 6 string elements. 
// The first element is the starting point and must be parsed to a number. 
// The remaining 5 elements are the names of the operations to be performed.
// The output should be printed on the console.

function cookingByNumbers(numString, ...operations) {
    let result = 0;
    result = Number(numString);

    for (let op of operations) {
        switch (op) {
            case 'chop': result /= 2; break;
            case 'dice': result = Math.sqrt(result); break;
            case 'spice': result++; break;
            case 'bake': result *= 3; break;
            case 'fillet': result *= 0.8; break;
        }
        console.log(parseFloat(result.toFixed(6)));
    }

}
// cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop');
// cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');

// 13.	Array Rotation
// Write a function that receives an array and the number of rotations you have to perform. 
// Note: Depending on the number of rotations, the first element goes to the end.
// Output
// Print the resulting array elements separated by a single space.

function arrayRotations(arr, rotations) {
    let el = null;
    for (let i = 0; i < rotations; i++) {
        el = arr.shift();
        arr.push(el)
    }
    console.log(arr.join(' '))
}
// arrayRotations([32, 21, 61, 1], 4);
// arrayRotations([2, 4, 15, 31], 5);

function testBreak() {
    for (let i = 0; i < 10; i++) {
        if (i > 5) { break };
        console.log(i);
    }
}

// testBreak();

// 14.	Print Every N-th Element from an Array 
// The input comes as two parameters – an array of strings and a number. 
// The second parameter is N – the step.
// The output is every element on the N-th step starting from the first one. 
// If the step is 3, you need to return the 1-st, the 4-th, the 7-th … and so on, 
// until you reach the end of the array. 
// The output is the return value of your function and must be an array.
// Hints
// •	Return all the elements with for loop, incrementing the loop variable 
// with the value of the step variable.


function printNthElements(arr, step) {
    let result = [];
    let elem = null;
    for (let i = 0; i < arr.length; i += step) {
        result.push(arr[i]);
    }
    return result
}

// console.log (printNthElements(['5', 
//                 '20', 
//                 '31', 
//                 '4', 
//                 '20'], 
//                 2
//                 ));
// printNthElements(['dsa',
//                 'asd', 
//                 'test', 
//                 'tset'], 
//                 2
//                 );
// printNthElements(['1', 
//                 '2',
//                 '3', 
//                 '4', 
//                 '5'], 
//                 6
//                 );

// 15.	List of Names
// You will receive an array of names. 
// Sort them alphabetically in ascending order and print a numbered list of all the names, each on a new line.
// Hints
// •	The sort function rearranges the array in ascending order

function listOfNames(arr) {
    arr.sort();
    let i = 0;
    for (let name of arr) {
        i++
        console.log(`${i}.${name}`)
    }
}

// listOfNames (["John", "Bob", "Christina", "Ema"]);

// zada4a 16
function compareNumbers(a, b) { return a - b };

function sortingNumbers(arr) {
    let sortedArr = [];
    let result = [];
    let el = undefined;
    sortedArr = arr.sort(function (a, b) { return a - b; });

    while (true) {
        el = sortedArr.shift();
        if (el) {
            result.push(el);
        } else { break; }
        el = sortedArr.pop();
        if (el) {
            result.push(el);
        } else { break; }
    }
    return result;
}

// console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));

// 17.	Reveal Words
// Write a function, which receives two parameters. 
// The first parameter will be a string with some words separated by ', '.
// The second parameter will be a string that contains templates containing '*'.
// Find the word with the same length as the template and replace it.

function revealWords(wordsString, sentence) {
    let words = wordsString.split(', ');
    let result = '';
    const char = '*';
    result = sentence;
    for (let word of words) {
        result = result.replace(char.repeat(word.length), word)
    };
    console.log(result)

}

// revealWords('great, learning',
// 'softuni is ***** place for ******** new programming languages'
// )


// 18.	Modern Times of #(HashTag)
// The input will be a single string.
// Find all special words starting with #. If the found special word does not consist only of letters, then it is invalid and should not be printed. 
// Finally, print out all the special words you found without the label (#) on a new line.

function hashTags(text) {
    const char = '#';
    let words = [];
    words = text.split(' ');
    let found = [];
    const regex = new RegExp('^#[a-zA-Z]+$');
    for (let word of words) {
        // if (word.includes(char)) {
        if (regex.test(word)) {
            found.push(word.replace(char, ''));
        };
        // };
    }
    // console.log(found);
    for (let word of found) {
        console.log(word);
    }
}

// hashTags('Nowadays everyone uses # to tag a #special word in #socialMedia')

function textRegEx() {
    const regEx = new RegExp('^#[a-z]+$');
    const word = '#alabalanica';
    console.log(regEx.test(word))
}

// textRegEx();


// 19.	String Substring
// The input will be given as two separated strings (a word as a first parameter and a text as a second).
// Write a function that checks given text for containing a given word. The comparison should be case insensitive. Once you find a match, print the word and stop the program. 
// If you don't find the word print: "{word} not found!"

function stringSubstring(word, text) {
    // if (text.toLowerCase().includes(word.toLowerCase())) {
    //     console.log(word);
    // } else {
    //     console.log (`${word} not found!`)
    // }
    let allWords = text.split(' ');
    let isFound = false;
    for (let sub of allWords) {
        if (sub.toLowerCase() === word.toLowerCase()) {
            isFound=true;
            // word = sub;
            break;
        }
    }
    if (isFound) {
        console.log(word);
    } else {
        console.log (`${word} not found!`)
    }
}

// stringSubstring ('javascript',
//                 'JavaScript is the best programming language'
//                 );
// stringSubstring ('python',
//                 'JavaScript is the best programming language'
//                 );

function textRegEx2() {
    // const regEx = new RegExp('[A-Z][a-z]+');
    const regEx = /[A-Z][a-z]+/g;
    const word = 'aAlabaLanica';
    // let result = word.match (regEx)
    // console.log (result)
    // console.log (result['index'])
    for (let found of word.matchAll(regEx)) {
        console.log(found)
    }
    // console.log(regEx.test(word))
}

// textRegEx2();

function splitterPascalCase(text) {
    const regex = /[A-Z][a-z]*/g;
    let results = [];
    for (let found of text.matchAll(regex)) {
        results.push(found[0])
    }
    console.log(results.join(', '))
}

splitterPascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan');
splitterPascalCase('HoldTheDoor');
splitterPascalCase('ThisIsSoAnnoyingToDoAAA');