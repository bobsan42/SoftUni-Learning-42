function racing(input) {
    inputsCount = Number(input.shift());
    let sprintBoard = [];
    let commands = {
        'Add New': addNew,
        'Change Status': changeStatus,
        'Remove Task': removeTask
    }

    for (let i = 0; i < inputsCount; i++) {
        let line = input.shift();
        // console.log(line);
        // print(line);
        let [assignee, taskId, title, status, estPoints] = line.split(':');
        sprintBoard.push({ assignee, taskId, title, status, estPoints });
        // print(taskId);
        // print(sprintBoard[taskId]);
    }
    for (let line of input) {
        let arr = line.split(':');
        const cmd = arr.shift();
        // print(cmd);
        commands[cmd](arr);
    }

    // for (const [k, v] of Object.entries(sprintBoard)) {
    //     print(k);
    //     print(v);
    // }
    // printBoard();
    printResults();

    function addNew(params) {
        let [assignee, taskId, title, status, estPoints] = params;
        if (isOnTheBoard(assignee)) {
            sprintBoard.push({ assignee, taskId, title, status, estPoints });
        } else {
            print(`Assignee ${assignee} does not exist on the board!`)
        }

    }

    function changeStatus(params) {
        let [assignee, taskId, newStatus] = params;
        if (isOnTheBoard(assignee)) {
            let idx = sprintBoard.findIndex((x) => (x.assignee === assignee && x.taskId === taskId));
            // print(assignee);
            // print(taskId);
            // print(idx);
            if (idx >= 0) {
                // sprintBoard[idx]['status'] = newStatus;
                sprintBoard[idx].status = newStatus;
            } else {
                print(`Task with ID ${taskId} does not exist for ${assignee}!`);
            }
        } else {
            print(`Assignee ${assignee} does not exist on the board!`);
        }

    }

    function removeTask(params) {
        let [assignee, index] = params;
        if (isOnTheBoard(assignee)) {
            let tasks = sprintBoard.filter((x) => (x.assignee === assignee));
            // print(tasks);
            let task = tasks[index];
            if (task) {
                // print(task);
                let idx = sprintBoard.findIndex((x) => (x.taskId === task.taskId));
                if (idx >= 0) {
                    sprintBoard.splice(idx, 1);
                }
            } else {
                print('Index is out of range!');
            }
        } else {
            print(`Assignee ${assignee} does not exist on the board!`);
        }

    }

    function isOnTheBoard(assignee) {
        // for (const [k, v] of Object.entries(sprintBoard)) {
        for (const x of sprintBoard) {
            if (x.assignee === assignee) {
                return true;
            }
        }
        return false;

    }

    function print(x) {
        console.log(x);
    }
    function printBoard() {

        for (const x of sprintBoard) {
            print(x);
        }

    }


    function printResults() {
        const summary = ['ToDo', 'In Progress', 'Code Review', 'Done'];
        let sumDone = 0;
        let sumOthers = 0;

        for (const type of summary) {
            let ssum = 0;
            let res = sprintBoard.filter((x) => x.status === type)
            for (const y of res) {
                ssum +=Number(y.estPoints);
                if (type === 'Done') {
                    sumDone += ssum
                } else {
                    sumOthers +=ssum;

                }
            }
            if(type==='Done') {
                print(`Done Points: ${ssum}pts`)
            } else {
                print(`${type}: ${ssum}pts`)

            }
        }
        if (sumDone >= sumOthers ) {
            print('Sprint was successful!');
        } else {
            print('Sprint was unsuccessful...');
        }
    }

}

// testing 
racing(
       [
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]

)


console.log('# '.repeat(25));

// sprint(
//     [
//         '4',
//         'Kiril:BOP-1213:Fix Typo:Done:1',
//         'Peter:BOP-1214:New Products Page:In Progress:2',
//         'Mariya:BOP-1215:Setup Routing:ToDo:8',
//         'Georgi:BOP-1216:Add Business Card:Code Review:3',
//         'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
//         'Change Status:Georgi:BOP-1216:Done',
//         'Change Status:Will:BOP-1212:In Progress',
//         'Remove Task:Georgi:3',
//         'Change Status:Mariya:BOP-1215:Done',
//     ]

// )

