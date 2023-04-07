function thePianist(input) {
    //######################################
    function addPiece(piece, composer, key, init = false) {
        if (piecesCollection[piece] && !init) {
            console.log(`${piece} is already in the collection!`);
            return;
        }
        piecesCollection[piece] = { composer, key };
        console.log(`${piece} by ${composer} in ${key} added to the collection!`);
    };
    //######################################
    function removePiece(piece) {
        if (piecesCollection.hasOwnProperty(piece)) {
            delete piecesCollection[piece];
            console.log(`Successfully removed ${piece}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`)
        }
    };
    //######################################
    function changeKey(piece, newKey) {
        if (piecesCollection.hasOwnProperty(piece)) {
            piecesCollection[piece]['key'] = newKey;
            console.log(`Changed the key of ${piece} to ${newKey}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        }
    };
    //######################################
    function printCollection() {
        for (const [p, v] of Object.entries(piecesCollection)) {
            // console.log(p);
            // console.log(v);
            console.log(`${p} -> Composer: ${v['composer']}, Key: ${v['key']}`)
        };
    };

    //######################################
    let n = Number(input.shift());
    let piecesCollection = {};
    let commandFunctions = {
        'Add': addPiece,
        'Remove': removePiece,
        'ChangeKey': changeKey,
    };

    for (let idx = 0; idx < n; idx++) {
        let [piece, composer, key] = input.shift().split('|')
        piecesCollection[piece] = { composer, key }
    }
    // console.log(piecesCollection['Fur Elise']);
    for (let line of input) {
        // console.log(line);
        const tokens = line.split('|');
        const cmd = tokens.shift();
        // console.log(cmd);
        if (cmd === 'Stop') {
            break;
        }
        commandFunctions[cmd](...tokens);
    }
    printCollection();


}

thePianist(
    [
        '3',
        'Fur Elise|Beethoven|A Minor',
        'Moonlight Sonata|Beethoven|C# Minor',
        'Clair de Lune|Debussy|C# Minor',
        'Add|Sonata No.2|Chopin|B Minor',
        'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
        'Add|Fur Elise|Beethoven|C# Minor',
        'Remove|Clair de Lune',
        'ChangeKey|Moonlight Sonata|C# Major',
        'Stop'
    ]


);

console.log('#'.repeat(50));
thePianist(
    [
        '4',
        'Eine kleine Nachtmusik|Mozart|G Major',
        'La Campanella|Liszt|G# Minor',
        'The Marriage of Figaro|Mozart|G Major',
        'Hungarian Dance No.5|Brahms|G Minor',
        'Add|Spring|Vivaldi|E Major',
        'Remove|The Marriage of Figaro',
        'Remove|Turkish March',
        'ChangeKey|Spring|C Major',
        'Add|Nocturne|Chopin|C# Minor',
        'Stop'
    ]

);