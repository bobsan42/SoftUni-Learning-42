function addItem() {
    // console.log('TODO:...');
    const uList = document.getElementById('items');
    const input = document.getElementById('newItemText');
    let text = input.value;
    if (text.length>0) {
        const newLi = document.createElement('li');
        newLi.textContent=text;
        uList.appendChild(newLi);
    }
    input.value = '';
}