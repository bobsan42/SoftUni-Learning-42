function racing(input) {
    let raceOrder = [];
    raceOrder = input.shift().split('|').reverse();
    // print(raceOrder);
    // print(raceOrder.length);

    // printBoard();
    let commandsPool = {
        'Retake': retake,
        'Trouble': trouble,
        'Rage': rage,
        'Miracle': miracle
    }

    for (let line of input) {
        let arr = line.split(' ');
        const cmd = arr.shift();
        if (cmd !== 'Finish') {
            commandsPool[cmd](arr);
        } else {
            break
        }
        // print(cmd);
    }

    printBoard();

    function retake(args) {
        let overtakingHorse = args[0];
        let idx1 = raceOrder.indexOf(overtakingHorse);
        let horseOvertaken = args[1];
        let idx2 = raceOrder.indexOf(horseOvertaken);
        if (idx2 < idx1) {
            raceOrder[idx2] = overtakingHorse;
            raceOrder[idx1] = horseOvertaken;
            print(`${overtakingHorse} retakes ${horseOvertaken}.`);
        }

    }

    function trouble(args) {
        let horse = args[0];
        let idx = raceOrder.indexOf(horse);
        if (idx + 1 < raceOrder.length) {
            raceOrder.splice(idx, 1);
            idx += 1;
            if (idx === raceOrder.length) {
                raceOrder.push(horse);
            } else {
                raceOrder.splice(idx, 0, horse);
            }
            print(`Trouble for ${horse} - drops one position.`)
        }

    }

    function rage(args) {
        let horse = args[0];
        let idx = raceOrder.indexOf(horse);
        raceOrder.splice(idx, 1);
        idx -= 2;
        if (idx < 0) {
            idx = 0;
            raceOrder.unshift(horse);
        } else {
            raceOrder.splice(idx, 0, horse);
        }
        print(`${horse} rages 2 positions ahead.`);

    }

    function miracle() {
        let horse = raceOrder.pop();
        raceOrder.unshift(horse);
        print(`What a miracle - ${horse} becomes first.`)
    }


    function print(x) {
        console.log(x);
    }
    function printBoard() {
        let winner = raceOrder[0]
        result = raceOrder.reverse().join('->');
        // for (const x of raceOrder) {
        //     print(x);
        // }
        print(result);
        print(`The winner is: ${winner}`)

    }


}


// testing
// racing(
//     ['Bella|Alexia|Sugar',
//         'Retake Alexia Sugar',
//         'Rage Bella',
//         'Trouble Bella',
//         'Finish']
// )
// console.log('# '.repeat(25));
// racing(
//     ['Onyx|Domino|Sugar|Fiona',
//         'Trouble Onyx',
//         'Retake Onyx Sugar',
//         'Rage Domino',
//         'Miracle',
//         'Finish']
// )


// console.log('# '.repeat(25));
// racing(
//     ['Fancy|Lilly',
//         'Retake Lilly Fancy',
//         'Trouble Lilly',
//         'Trouble Lilly',
//         'Finish',
//         'Rage Lilly']
// )