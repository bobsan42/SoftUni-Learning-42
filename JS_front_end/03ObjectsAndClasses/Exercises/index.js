
// 1.	Employees
// You're tasked to create a list of employees and their personal numbers.
// You will receive an array of strings. Each string is an employee name and 
// to assign them a personal number you have to find the length of the name (whitespace included). 
// Try to use an object.
// At the end print all the list employees in the following format:
//  "Name: {employeeName} -- Personal Number: {personalNum}" 

function employees(input) {
    let employeesList = {};
    for (let name of input) {
        employeesList[name] = name.length;
    }
    // console.log(employeesList)
    let emp = Object.entries(employeesList)
    for (let [name, num] of emp) {
        console.log(`Name: ${name} -- Personal Number: ${num}`)
    }

}
// employees([
//     'Silas Butler',
//     'Adnaan Buckley',
//     'Juan Peterson',
//     'Brendan Villarreal'
//     ]);

// 2.	Towns
// You’re tasked to create and print objects from a text table. 
// You will receive the input as an array of strings, 
// where each string represents a table row, with values on the row separated by pipes " | " and spaces.
// The table will consist of exactly 3 columns "Town", "Latitude" and "Longitude". 
// The latitude and longitude columns will always contain valid numbers. 
// Check the examples to get a better understanding of your task.
// The output should be objects. 
// Latitude and longitude must be parsed to numbers and formatted to the second decimal point!

function towns(input) {
    let listOfTowns = [];
    let town = [];
    let x = {}
    for (let item of input) {
        town = item.split(' | ');
        x = {
            town: town[0],
            latitude: String(Number(town[1]).toFixed(2)),
            longitude: String(Number(town[2]).toFixed(2))
        };
        console.log(x);
        listOfTowns.push(x);
    };
}

// towns(['Sofia | 42.696552 | 23.32601',
// 'Beijing | 39.913818 | 116.363625']);

// 3.	Store Provision
// You will receive two arrays. 
// The first array represents the current stock of the local store. 
// The second array will contain products that the store has ordered for delivery.
// The following information applies to both arrays:
// Every even index will hold the name of the product and every odd index will hold the quantity of that product. 
// The second array could contain products that are already in the local store. 
// If that happens increase the quantity for the given product. 
// You should store them into an object, and print them in the following format: (product -> quantity)
// All of the arrays’ values will be strings.

function store(storeArr, productsArr) {
    let stock = {};
    for (let i = 0; i < storeArr.length; i += 2) {
        stock[storeArr[i]] = Number(storeArr[i + 1])
    };
    // console.log(stock);
    for (let i = 0; i < productsArr.length; i += 2) {
        // if (stock.hasOwnProperty(productsArr[i])){
        if (stock[productsArr[i]]) {
            stock[productsArr[i]] += Number(productsArr[i + 1])
        } else {
            stock[productsArr[i]] = Number(productsArr[i + 1])
        };
    }
    // console.log(stock);
    let result = Object.entries(stock);
    for (let [prod, qty] of result) {
        console.log(`${prod} -> ${qty}`);
    };
}

// store ([
//     'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
//     ],
//     [
//     'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
//     ]
//     );

// 4.	Movies
// Write a function that stores information about movies inside an array. 
// The movie's object info must be name, director, and date. You can receive several types of input:
// •	"addMovie {movie name}" – add the movie
// •	"{movie name} directedBy {director}" – check if the movie exists and then add the director
// •	"{movie name} onDate {date}" – check if the movie exists and then add the date
// At the end print all the movies that have all the info 
// (if the movie has no director, name, or date, don’t print it) in JSON format.

function movies(input) {
    let movies = [];
    for (let line of input) {
        if (line.split('addMovie ')[1]) {
            movies.push({ name: line.split('addMovie ')[1] });
        } else if (line.split(' directedBy ')[1]) {
            let movieIdx = movies.findIndex((m) => m.name === line.split(' directedBy ')[0])
            if (movieIdx>=0) {
                let mm = movies[movieIdx];
                // console.log(mm);
                movies[movieIdx]['director'] = line.split(' directedBy ')[1];
            }
        } else if (line.split(' onDate ')[1]) {
            let movieIdx = movies.findIndex((m) => m.name === line.split(' onDate ')[0])
            if (movieIdx>=0) {
                movies[movieIdx].date = line.split(' onDate ')[1];
            }
        }
    }
    movies
        .filter((m) => m.name && m.director && m.date)
        .forEach((m)=> console.log(JSON.stringify(m)))

    // console.log(movies)

};

    // movies([
    //     'addMovie Fast and Furious',
    //     'addMovie Godfather',
    //     'Inception directedBy Christopher Nolan',
    //     'Godfather directedBy Francis Ford Coppola',
    //     'Godfather onDate 29.07.2018',
    //     'Fast and Furious onDate 30.07.2018',
    //     'Batman onDate 01.08.2018',
    //     'Fast and Furious directedBy Rob Cohen'
    // ]
    // );
    // console.log ('#'.repeat(20));
    // movies ([
    //     'addMovie The Avengers',
    //     'addMovie Superman',
    //     'The Avengers directedBy Anthony Russo',
    //     'The Avengers onDate 30.07.2010',
    //     'Captain America onDate 30.07.2010',
    //     'Captain America directedBy Joe Russo'
    //     ]
    //     );

// 5.	Inventory
// Create a function, which creates a register for heroes, with their names, level, and items (if they have such). 
// The input comes as an array of strings. Each element holds data for a hero, in the following format:
// "{heroName} / {heroLevel} / {item1}, {item2}, {item3}..." 
// You must store the data about every hero. The name is a string, a level is a number and the items are all strings.
// The output is all of the data for all the heroes you’ve stored sorted ascending by level. 
// The data must be in the following format for each hero:
// Hero: {heroName}
// level => {heroLevel}
// Items => {item1}, {item2}, {item3

function inventory(input){
    let heroes = [];
    for (let line of input) {
        let [hero, level, items] = line.split(' / ');
        level = Number(level);
        heroes.push([hero, level, items]);
    };
    let sortedByLevel = heroes.sort((hero1, hero2) => (hero1[1]-hero2[1]));
    // console.table(sortedByLevel);
    for (let h of heroes) {
        console.log(`Hero: ${h[0]}`);
        console.log(`level => ${h[1]}`);
        console.log(`items => ${h[2]}`);
    }
};

// inventory([
//     'Isacc / 25 / Apple, GravityGun',
//     'Derek / 12 / BarrelVest, DestructionSword',
//     'Hes / 1 / Desolator, Sentinel, Antara'
//     ]);

// 6.	Words Tracker
// Write a function that receives an array of words and finds occurrences of given words in that sentence. 
// The input will come as an array of strings. 
// The first string will contain the words you will be looking for separated by a space. 
// All strings after that will be the words in which you will check for a match.
// Print for each word how many times it occurs. 
// The words should be sorted by count in descending.

function wordsTracker(input) {

}

wordsTracker([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
    ); 
    // this - 3
    // sentence - 2

    
    
// 7.	Odd Occurrences
// Write a function that extracts the elements of a sentence, 
// if it appears an odd number of times (case-insensitive).
// The input comes as a single string. The words will be separated by a single space.
    
function oddOccur(input) {

}

oddOccur('Java C# Php PHP Java PhP 3 C# 3 1 5 C#'); // c# php 1 5


// 8.	Piccolo
// Write a function that:
// •	Records a car number for every car that enters the parking lot
// •	Removes a car number when the car goes out
// •	Input will be an array of strings in format [direction, carNumber]
// Print the output with all car numbers which are in the parking lot sorted in ascending by number.
// If the parking lot is empty, print: "Parking Lot is Empty".

function picolo (input) {

}

picolo (['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);
// CA2822UU
// CA2844AA
// CA9876HH
// CA9999TT

// 9.	Make a Dictionary
// You will receive an array with strings in the form of JSON's. 
// You have to parse these strings and combine them into one object. 
// Every string from the array will hold terms and a description. 
// If you receive the same term twice, replace it with the new definition.
// Print every term and definition in that dictionary on new line in format:
// `Term: ${term} => Definition: ${definition}`
// Don't forget to sort the dictionary alphabetically by the terms as in real dictionaries.

function dictionary(input) {

};

dictionary ([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
    );

    // Term: Boiler => Definition: A fuel-burning apparatus or container for heating water.
    // Term: Bus => Definition: A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.
    // Term: Coffee => Definition: A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub.
    // Term: Microphone => Definition: An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded.
    // Term: Tape => Definition: A narrow strip of material, typically used to hold or fasten something.
    

    // 10.	Class Vehicle
    // Create a class with the name Vehicle that has the following properties:
    // •	type – a string
    // •	model – a string
    // •	parts – an object that contains:
    // o	engine – number (quality of the engine)
    // o	power – number
    // o	quality – engine * power
    // •	fuel – a number
    // •	drive – a method that receives fuel loss and decreases the fuel of the vehicle by that number
    // The constructor should receive the type, the model, the parts as an object, and the fuel
    // In judge post your class (Note: all names should be as described
    
// class testing code:
// --------------------------------------------------------------
// let parts = { engine: 6, power: 100 };
// let vehicle = new Vehicle('a', 'b', parts, 200);
// vehicle.drive(100);
// console.log(vehicle.fuel);
// console.log(vehicle.parts.quality);

// output: 
// 100
// 600

// class testing code:
// --------------------------------------------------------------
// let parts = {engine: 9, power: 500};
// let vehicle = new Vehicle('l', 'k', parts, 840);
// vehicle.drive(20);
// console.log(vehicle.fuel);

// output: 820

