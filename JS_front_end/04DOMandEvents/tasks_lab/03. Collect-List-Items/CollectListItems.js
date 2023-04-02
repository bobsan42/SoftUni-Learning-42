function extractText() {
    // TODO
    let uList = document.querySelector('ul#items');
    let items = document.querySelectorAll('ul#items li');
    let textArea = document.querySelector('#result');
    // let text = ''
    // for (let item of items){
    //     text += item.textContent +'\n';
    // } 

    const text = uList.innerText;

    // let itemsArr = Array.from(items);
    // console.log(itemsArr);
    // let arr2 = itemsArr.map((x) => x=x.outerText);
    // console.log(arr2);
    
    // text = arr2.join('\n');

    // textArea.value = text;
    textArea.textContent = text;
}