let display = document.getElementById('result');

function addToDisplay(value) {
  if (display.innerHTML == '0') {
    display.innerHTML = value;
  } else {
    display.innerHTML += value;
  }
}

function clearDisplay() {
  display.innerHTML = '0';
}

function backspace() {
  let currentValue = display.innerHTML;
  display.innerHTML = currentValue.substring(0, currentValue.length - 1);
}

function calculate() {
  let expression = display.innerHTML;
  let result = eval(expression);
  display.innerHTML = result;
}