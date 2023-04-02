function sumTable() {
    // body > table > tbody > tr:nth-child(2) > td:nth-child(2);
    // body > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)
    // body > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)
    const costColumn = document.querySelectorAll('table:nth-child(1)  td:nth-child(2)');
    const result = document.getElementById('sum');
    let totalCost = 0;
    console.log(costColumn);
    for (let c of costColumn) {
        // console.log(c.textContent);
        // console.log(c.id);
        if (c.id !== 'sum') {
            totalCost += Number(c.textContent);
        }
    }
    result.textContent = totalCost;
    

}