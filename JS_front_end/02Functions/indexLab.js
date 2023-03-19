function formatGrade(grade) {
    let result = '';
    if (grade < 3) {
        result = 'Fail (2)';
    } else if (grade < 3.50) {
        result = `Poor (${grade.toFixed(2)})`
    } else if (grade < 4.50) {
        result = `Good (${grade.toFixed(2)})`
    } else if (grade < 5.50) {
        result = `Very good (${grade.toFixed(2)})`
    } else {
        result = `Excellent (${grade.toFixed(2)})`
    }
    return result
}

// console.log(formatGrade(5.68))

function mathPower(num, power) {
    let result = 1
    for (let i = 0; i < power; i++) {
        result *= num
    }
    return result;
}
function mathPower2(num, power) {
    return Math.pow(num, power)
}
// console.log(mathPower(2,8))
// console.log(mathPower2(2,8))

function repeatString(text, count) {
    let result = ''
    for (let i = 0; i < count; i++) {
        result += text;
    }
    return result;
}
function repeatText(text, count) {
    return text.repeat(count)
}

// console.log (repeatString("abc", 3))
// console.log(repeatText("abc", 3))

function orders(product, qty) {
    const priceList = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }
    let cost = priceList[product] * qty
    console.log(cost.toFixed(2))
}
// orders("water", 5);
// orders("coffee", 2);

function simpleCalculator(a, b, operation) {
    let calculations = {
        'multiply': (a, b) => a * b,
        'divide': (a, b) => a / b,
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b
    }
    console.log(calculations[operation](a, b))
}

// simpleCalculator(
//     5,
//     5,
//     'multiply'
// )
// simpleCalculator (
//     40,
//     8,
//     'divide'
// )
// simpleCalculator (
//     12,
//     19,
//     'add'    
// )
// simpleCalculator (
//     50,
//     13,
//     'subtract'    
// )

function signCheck(a, b, c) {
    let sign = 1;
    sign *= Math.sign(a);
    sign *= Math.sign(b);
    sign *= Math.sign(c);
    // console.log(Math.sign(a));
    // console.log(Math.sign(b));
    // console.log(Math.sign(c));
    if (sign < 0) {
        console.log('Negative')
    } else {
        console.log('Positive')
    }
}

// signCheck(10,0,-5);
signCheck(5, 12, -15);
signCheck(-6, -12 - 14);
signCheck(-1, -2, -3);
signCheck(-5, 1, 1);