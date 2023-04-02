function colorize() {
    // TODO
    // const tbl = document.getElementsByClassName('table');
    // console.log (tbl[0]);
    // const rows = document.querySelectorAll('table tr:nth-child(even)');
    const rows = document.querySelectorAll('table tr');
    // console.log(rows);
    // console.log(rows[0].style);
    let index = 0;
    for (let r of rows) {
        index++;
        if (index %2 ==0) {
            r.style.backgroundColor='Teal';
            // r.style.color = 'teal';
            // r.color='Teal';
            // console.log(r.style.backgoundColor);
        }
        
    };
}