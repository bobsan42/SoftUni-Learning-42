// recursion 

function printCountdown(num) {
    console.log(num)
    if (num > 0) {
        printCountdown(num - 1);
    }
}

// printCountdown(6 );

// Check if array index is valid:

function isValid(index, arr) {
    if (Number.isInteger(index) && index >= 0 && index < arr.length) {
        return true;
    } else {
        return false;
    }
}

// console.log(isValid(5,[1,2,3,4,5]))

// Nested Functions: Example

function swapElements(arr) {
    for (let i = 0; i < arr.length / 2; i++) {
        swap(arr, i, arr.length - 1 - i);
    }
    console.log(arr.join(' '));
    function swap(elements, i, j) {
        let temp = elements[i];
        elements[i] = elements[j];
        elements[j] = temp;
    }
}

//   console.log(swapElements([0,1,2,3]))
swapElements([0, 1, 2, 3])


function sumNumbers(...nums) {
    let sum = 0;
    // for (let idx = 0; idx <nums.length; idx++){
    //     sum += nums[idx]
    // }

    for (num of nums) {
        sum += Number(num)
    }
    return sum;
}

console.log(sumNumbers(1,5,8,11,+15,-152));