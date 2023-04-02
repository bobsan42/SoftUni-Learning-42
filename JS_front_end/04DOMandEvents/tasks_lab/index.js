const  liItems = Array.from(document.getElementsByTagName('li'));

let p = document.createElement('p');
p.textContent = 'This is a new Paragraph.';
let h1 = document.createElement('h1');
h1.textContent = 'This is a Heading.';
let li = document.createElement("li");
li.textContent = 'FOURTH';
const firstLi = liItems[0];
firstLi.appendChild(p);
firstLi.parentElement.appendChild(li);
p.textContent += ' - MORE';
li.appendChild(p);
li.replaceChild(h1, p);
