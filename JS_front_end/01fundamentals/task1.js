//JUDGE input testing
function test(input) {
    console.log(input);
    console.log(typeof input);
}
test([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);
test(1,2,3);

// zada4a 1
function multi2(num) {
    console.log(num * 2)
}

//zada4a 2 
function studentData(name, age, grade) {
    console.log(`Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`)
}
// studentData('Ivan40', 16, 5.38158)

//zada4a # 3
function solve(num) {
    num = Number(num);
    if (num >= 5.50) {
        console.log('Excellent');
    } else {
        console.log('Not excellent');
    }
}

//zada4a # 4
function checkMonth(num) {
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'];
    let result = months[num - 1];
    if (result) {
        return result;
    } else {
        return 'Error!'
    }
}

//zada4a 5
function mathOperations(a, b, op) {
    let result;
    switch (op) {
        case '+': result = a + b; break;
        case '-': result = a - b; break;
        case '*': result = a * b; break;
        case '/': result = a / b; break;
        case '%': result = a % b; break;
        case '**': result = a ** b; break;

    }
    console.log(result);
}

// mathOperations(5, 3, '**')

// zada4a 6
function largestNumber(a, b, c) {
    let result;
    if (a > b) {
        result = a
    } else {
        result = b
    }
    if (result < c) {
        result = c
    }
    console.log(`The largest number is ${result}.`)
}
// largestNumber(5, -3, 16)
// largestNumber(-3, -5, -22.5)

//zada4a 7

function theatreTickets(dayType, age) {
    let price;
    let isError = false;
    if (age > 122 || age < 0) {
        price = "Error!";
        isError = true;
    } else {
        switch (dayType) {
            case 'Weekday':
                if (age <= 18 || age > 64) {
                    price = 12;
                } else {
                    price = 18;
                }
                break;
            case 'Weekend':
                if (age <= 18 || age > 64) {
                    price = 15;
                } else { price = 20; }
                break;
            case 'Holiday':
                if (age <= 18) { price = 5; }
                else if (age > 64) { price = 10; }
                else { price = 12; }
                break;
        }
    }
    if (isError) {
        console.log('Error!')
    } else {
        console.log(`${price}$`)
    }

}

// theatreTickets('Weekday', 42)

//zada4a 8
function circleArea(input) {
    let result;
    let inputType = typeof (input)

    if (inputType === 'number') {
        result = Math.pow(input, 2) * Math.PI;
        console.log(result.toFixed(2))
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`)
    }
}

// circleArea(6);
// circleArea ('asljdhaslk dsadasd')


// zada4a # 9 
function printNums() {
    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }
}
//printNums();

// zada4a # 10 
function printBetweenNums(m, n) {
    for (let i = m; i >= n; i--) {
        console.log(i);
    }
}
//printBetweenNums(5,2);

// зада4а 11

function sumArrayFirstLast(arr) {
    let result = arr[0] + arr[arr.length - 1]
    console.log(result)
}

// zada4a 12 

function reveresNElements(n, nums) {
    // let nums = [];
    let result = nums
        .slice(0, n)
        .reverse()
        .join(' ')
    console.log(result)
}
// reveresNElements(3, [10, 20, 30, 40, 50] )

//zada4a 13

function evenOddSubtraction(arr) {
    // let arr = [];
    let evens = arr
        .filter((num) => (num) % 2 === 0);
    let odds = arr
        .filter((num) => ((num) % 2) ** 2 === 1);
        // .filter((num) => ((num) % 2) !== 0);
    let sumOdd = 0;
    let sumEven = 0;
    // evens.forEach(e => {
    //     sumEven += e;
    //   });
    // odds.forEach(e => {
    //     sumOdd += e;
    //   });
    evens.map(e => sumEven += Number(e));
    odds.map(e => sumOdd += Number(e));
    // console.log(evens)
    // console.log(odds)
    let result = sumEven - sumOdd;
    console.log(result)
}

evenOddSubtraction([-2, -4, '6'])

//zada4a 14

function substring(text, idx, count) {
    console.log(text.slice(idx, idx + count));
}

// substring('ASentence', 1, 8)


//zada4a 15
function censoredWords(text, word) {
    while (text.includes(word)) {
        text = text.replace(word, "*".repeat(word.length))
    }
    console.log(text)
}
// censoredWords('A small sentence with some words small small','small')

//zada4a 16
function countStringOccurences(text, word) {
    let arr = [];
    arr = text
        .split(' ')
        .filter((item) => item === word);

    let result = arr.length
    console.log(result)
}

// countStringOccurences('This is a word and it also is a sentence','is')
// countStringOccurences('softuni is great place for learning new programming languages', 'softuni')
