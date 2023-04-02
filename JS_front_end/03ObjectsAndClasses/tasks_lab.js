// 03. City Taxes 

function cityTaxes(name, population, treasury) {
    let city = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes: function () {
            this.treasury += Math.floor(this.population * this.taxRate);
        },
        applyGrowth: function (percentage) {
            this.population = Math.floor(this.population * (100 + percentage) / 100);
        },
        applyRecession: function (percentage) {
            this.treasury = Math.floor(this.treasury * (100 - percentage) / 100);
        }
    };
    return city;

}
// const city =
//     cityTaxes('Tortuga',
//         7000,
//         15000);
// console.log(city);
// const city =
//   cityTaxes('Tortuga',
//   7000,
//   15000);

// city.collectTaxes();
// console.log(city.treasury);
// city.applyGrowth(5);
// console.log(city.population);


// 04. Convert to Object 

function objConverter(json) {
    let person = JSON.parse(json);

    let entries = Object.entries(person);

    for (let [key, value] of entries) {
        console.log(`${key}: ${value}`);
    }
}

// 5.	Convert to JSON
function convertJSON(name, lastName, hairColor) {
    let person = {
        name,
        lastName,
        hairColor
    };
    console.log(JSON.stringify(person));
}


// convertJSON('George', 'Jones', 'Brown')

// 6.	Phone Book

function phonebook(arr) {
    let phonebbok = {};
    for (let entry of arr) {
        let x = entry.split(' ')
        phonebbok[x[0]] = x[1]
    }
    let contacts = Object.entries(phonebbok)
    for (let [key, value] of contacts) {
        console.log(`${key} -> ${value}`);
    }
}

// phonebook(['Tim 0834212554',
//     'Peter 0877547887',
//     'Bill 0896543112',
//     'Tim 0876566344']);

// 7.	Meetings
function meetings(input) {
    let meetings = {};
    for (let item of input) {
        let x = item.split(' ');
        let day = x[0];
        let name = x[1];
        // if (meetings[day]) {
        if (meetings.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`)
        } else {
            console.log(`Scheduled for ${day}`)
            meetings[day] = name
        }
    };
    let result = Object.entries(meetings);
    for (let [day, name] of result) {
        console.log(`${day} -> ${name}`);
    };

}

// meetings(['Monday Peter',
//     'Wednesday Bill',
//     'Monday Tim',
//     'Friday Tim']
// )

// 8.	Address Book

function addressBook(input) {
    let addresses = {};
    for (const item of input) {
        let [name, address] = item.split(':')
        addresses[name] = address
    };
    // console.log(addresses);
    const entries = Object.entries(addresses)
    let sortedByName = entries.sort((personA, personB) => {
        return personA[0].localeCompare(personB[0])
    })
    for (let [name, addr] of sortedByName) {
        console.log(`${name} -> ${addr}`);
    };

}

// addressBook(['Tim:Doe Crossing',
//     'Bill:Nelson Place',
//     'Peter:Carlyle Ave',
//     'Bill:Ornery Rd']
// )

// 9.	Cats - CLASSES
function catTask(input) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = Number(age);
        }
        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    let cats = [];
    for (const item of input) {
        let [name, age] = item.split(' ');
        cats.push(new Cat(name, age));
    };

    for (let kittie of cats) {
        kittie.meow();
    }
}

catTask(['Mellow 2', 'Tom 5'])
