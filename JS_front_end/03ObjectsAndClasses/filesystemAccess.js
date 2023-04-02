const fs = require('fs'); //FileSystem
// console.log(fs);

const file = fs.readFileSync('./03ObjectsAndClasses/people.json', 'utf-8');
// console.log(file);

const dataObj = JSON.parse(file);
console.log(dataObj.client_id);
console.log(dataObj.device_time);
console.log(dataObj['sdk_version']);
