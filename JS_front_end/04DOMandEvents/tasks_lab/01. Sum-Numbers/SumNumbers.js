function calc() {
    // TODO: sum = num1 + num2
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    let sumNums = Number(num1) + Number(num2);
    document.getElementById('sum').value = sumNums;
}