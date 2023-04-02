function deleteByEmail() {
    // console.log(document.querySelectorAll('*'));
    // console.log('TODO:...');
    // let input = document.getElementsByName('email');
    // const email = input[0].value;
    let input = document.querySelector('input[name="email"]');
    const email = input.value;
    // console.log (input[0].value);
    let table = document.getElementsByTagName('table')[0];
    // table.parentNode.removeChild(table);
    // table.remove();
    let isFound = false;
    const result = document.getElementById('result');
    console.log(table);
    // let secondColumn = document.querySelectorAll(
    //     '#customers tbody tr td:nth-child(even)');
    let secondColumn = document.querySelectorAll(
        '#customers tbody tr td:nth-child(2)');
    // console.log(secondColumn);

    // for (const cell of secondColumn) {
    //     if (cell.textContent === email) {
    //         let row = cell.parentElement;
    //         row.remove();
    //         isFound = true;
    //         // return;
    //     }
    // }
    // if (isFound) {
    //     result.textContent = 'Deleted.';
    // } else {
    //     result.textContent = 'Not found.'
    // }

    // console.log(email);
    let foundElement = Array.from(secondColumn).find((item) => item.textContent === email);
    if (foundElement) {
        foundElement.parentElement.remove();
        result.textContent = 'Deleted.';
    } else {
        result.textContent = 'Not found.' 
    }
}