function focused() {
    // console.log('TODO:...');
    const inputs = document.getElementsByTagName('input');
    for (let i of inputs) {
        i.addEventListener('focus', handler);
        i.addEventListener('blur', handler);
    }

    function handler(e) {
        // console.log(e.type);
        const inputParent = e.target.parentElement;
        // console.log(inputParent);
        if (e.type === 'focus') {
            inputParent.setAttribute('class','focused'); 
        } else if (e.type === 'blur' ) {
            inputParent.setAttribute('class',''); 
        }
    }

}