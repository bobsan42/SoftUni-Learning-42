function shoppingLst(input) {
    let groceries = [];
    groceries = input.shift().split('!');
    // console.log(groceries);
    keyWord = 'Go Shopping!';
    const commands = {
        'Urgent': urgent,
        'Unnecessary': unnecessary,
        'Correct': correct,
        'Rearrange': rearrange
    };

    for (const line of input) {
        if (line === keyWord) {
            break;
        }
        let tokens = line.split(' ');
        let cmd = tokens.shift();
        commands[cmd](...tokens);
    }

    console.log(groceries.join(', '))

    function urgent(item) {
        if (!groceries.includes(item)) {
            groceries.unshift(item);
        }
    }

    function unnecessary(item) {
        if(groceries.includes(item)) {
            let i = groceries.indexOf(item);
            let removed = groceries.splice(i,1)[0];
        }

    }

    function correct(oldItem, newItem) {
        if(groceries.includes(oldItem)) {
            let i = groceries.indexOf(oldItem);
            groceries[i] = newItem;
        }
    }

    function rearrange(item) {
        if(groceries.includes(item)) {
            let i = groceries.indexOf(item);
            let removed = groceries.splice(i,1)[0];
            // console.log(removed);
            groceries.push(removed);
        }

    }

};

shoppingLst(
    ([
        "Tomatoes!Potatoes!Bread!Milk",
        "Unnecessary Milk",
        "Urgent Tomatoes",
        "Urgent Peppers",
        "Rearrange Peppers",
        "Go Shopping!"
    ])
);
console.log();
console.log('# '.repeat(30));
console.log();

shoppingLst(
    ([
        "Milk!Pepper!Salt!Water!Banana",
        "Urgent Salt",
        "Unnecessary Grapes",
        "Correct Pepper Onion",
        "Rearrange Grapes",
        "Correct Tomatoes Potatoes",
        "Go Shopping!"
    ])

)