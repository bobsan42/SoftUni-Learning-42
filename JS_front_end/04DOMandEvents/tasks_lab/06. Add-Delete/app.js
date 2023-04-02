function addItem() {
    //TODO...
    // console.log (Event);
    const uList = document.getElementById('items');
    const input = document.getElementById('newItemText');
    let text = input.value;
    const aDelete = document.createElement('a');
    aDelete.textContent = '[Delete]';
    aDelete.href='#';
    aDelete.addEventListener('click', handler, false);
    if (text.length > 0) {
        const newLi = document.createElement('li');
        newLi.textContent = text;
        uList.appendChild(newLi);
        newLi.appendChild(aDelete);
    }
    input.value = '';

    function handler (e) {
        const caller = e.currentTarget;
        console.log(this === caller); // always TRUE
        // console.log(e.currentTarget.parentElement);
        caller.parentElement.remove();

    }

    // function deleteItem() {
    //     console.log(this)

    // }
}