function smallestOfThreeNumbers(a, b, c) {
    // enter 3 numbers
    let result = a;
    if (result > b) {
        result = b;
    }
    if (result > c) {
        result = c;
    }
    return result;
}

function addAndSubtract(a, b, c) {
    let add = (x, y) => x + y;
    let subtract = (x, y) => x - y;
    let result = subtract(add(a, b), c)
    return result;
}

function charactersInRange(char1, char2) {
    let ascii1 = char1.charCodeAt(0)
    let ascii2 = char2.charCodeAt(0)

    let startCode = Math.min(ascii1, ascii2) + 1
    let endCode = Math.max(ascii1, ascii2)
    let result = []
    for (let ii = startCode; ii < endCode; ii++) {
        result.push(String.fromCharCode(ii))
    }
    // return result.join(' ')
    console.log(result.join(' '));
}

// charactersInRange('a','d');
// charactersInRange('#',':');
// charactersInRange('C','#');

function oddAndEvenDigitsSum(num) {
    let arr = String(num).split('');
    let sumOdd = 0;
    let sumEven = 0;
    for (let dig of arr) {
        if (dig % 2) {
            sumOdd += Number(dig)
        } else {
            sumEven += Number(dig)
        }
    }
    return (`Odd sum = ${sumOdd}, Even sum = ${sumEven}`)
}

// console.log(oddAndEvenDigitsSum(1000435));
// console.log(oddAndEvenDigitsSum(3495892137259234));

function palindromeIntegers(arr) {
    let str = ''
    for (let int of arr) {
        str = String(int)
        console.log(
            str ===
            str.split('').reverse().join('')
        )
    }
}

// palindromeIntegers([123,323,421,121]);
// console.log('='.repeat(20))
// palindromeIntegers([32,2,232,1010]);

function passwordValidator(password) {
    let isValid = true;
    let unfulfilledValidations = [];
    if (password.length > 10 || password.length < 6) {
        isValid = false;
        unfulfilledValidations.push(
            'Password must be between 6 and 10 characters'
        );
    }
    let regex = /[A-Za-z\d]+$/;
    let result = [];
    result = password.match(regex)
    if (result) {
        if (password !== result[0]) {
            isValid = false;
            unfulfilledValidations.push(
                'Password must consist only of letters and digits'
            )
        }

    } else {
        isValid = false;
        unfulfilledValidations.push(
            'Password must consist only of letters and digits'
        )
    }

    // regex = /[0-9]/g
    // result = password.matchAll(regex);
    let test3 = password.replace(/[\D]/g, ''); //.length;
    // console.log(test3)
    if (test3.length < 2) {
        isValid = false;
        unfulfilledValidations.push(
            'Password must have at least 2 digits'
        )
    }

    if (isValid) {
        console.log('Password is valid')
    } else {
        // console.log(unfulfilledValidations)
        for (let item of unfulfilledValidations) {
            console.log(item)
        }
    }

}

// passwordValidator('#^@$%^@#');
// passwordValidator('MyPass123');
// passwordValidator('Pa$s$s');


function matrixNxN(n) {
    let str = (n + ' ').repeat(n).trim()
    for (let i = 0; i < n; i++) {
        console.log(str)
    }
}

// matrixNxN(7)

function perfectNumber(num) {
    let sumDigits = 0
    for (let i = 1; i <= num / 2; i++) {
        if (num % i === 0) {
            sumDigits += i;
        }
    }
    if (sumDigits === num) {
        console.log('We have a perfect number!')
    } else {
        console.log('It\'s not so perfect.')
    }
}

// perfectNumber(6);
// perfectNumber(28);
// perfectNumber(1236498);

function loadingBar(num) {
    let progress = 0;
    progress = num / 10;
    const tot = 10;
    let str = '';
    if (num < 100) {
        str = String(num) + '% [' + '%'.repeat(progress) + '.'.repeat(tot - progress) + ']'
        console.log(str)
        console.log('Still loading...')
    } else {
        console.log('100% Complete!')
        console.log('[%%%%%%%%%%]')
    }
}

// loadingBar(30);
// loadingBar(70);
// loadingBar(100);

function factorialDivision(a, b) {
    let aFact = 1;
    let bFact = 1;
    function factorial(x) {
        let result = 1;
        for (let i = 1; i <= x; i++) {
            result *= i;
        }
        return result;
    }
    aFact = factorial(a);
    bFact = factorial(b);
    let result = aFact / bFact;
    console.log(result.toFixed(2));

}
factorialDivision(5,2);
factorialDivision(6,2);
factorialDivision (8,7);