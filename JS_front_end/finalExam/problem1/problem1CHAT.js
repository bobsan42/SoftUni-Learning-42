function runSprint(commands) {
    const board = {};
    const n = Number(commands.shift());
    // Initialize board with initial state
    for (let i = 1; i <= n; i++) {
        const [assignee, taskId, title, status, estimatedPoints] = commands[i].split(':');
        if (!board[assignee]) {
            board[assignee] = [];
        }
        board[assignee].push({
            taskId,
            title,
            status,
            estimatedPoints: parseInt(estimatedPoints),
        });
    }

    // Process commands to update board state
    for (let i = n + 1; i < commands.length; i++) {
        const [command, assignee, taskIdOrIndex, newStatus] = commands[i].split(':');
        if (command === 'Add New') {
            if (!board[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
                continue;
            }
            const [taskId, title, estimatedPoints] = [taskIdOrIndex, newStatus, parseInt(arguments[4])];
            board[assignee].push({ taskId, title, status: 'ToDo', estimatedPoints });
        } else if (command === 'Change Status') {
            if (!board[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
                continue;
            }
            const taskIndex = board[assignee].findIndex(task => task.taskId === taskIdOrIndex);
            if (taskIndex === -1) {
                console.log(`Task with ID ${taskIdOrIndex} does not exist for ${assignee}!`);
                continue;
            }
            board[assignee][taskIndex].status = newStatus;
        } else if (command === 'Remove Task') {
            if (!board[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
                continue;
            }
            const taskIndex = parseInt(taskIdOrIndex);
            if (taskIndex < 0 || taskIndex >= board[assignee].length) {
                console.log('Index is out of range!');
                continue;
            }
            board[assignee].splice(taskIndex, 1);
        }
    }

    // Calculate total points for each status and determine Sprint success
    let toDoPoints = 0;
    let inProgressPoints = 0;
    let codeReviewPoints = 0;
    let donePoints = 0;

    Object.values(board).forEach(tasks => {
        tasks.forEach(task => {
            switch (task.status) {
                case 'ToDo':
                    toDoPoints += task.estimatedPoints;
                    break;
                case 'In Progress':
                    inProgressPoints += task.estimatedPoints;
                    break;
                case 'Code Review':
                    codeReviewPoints += task.estimatedPoints;
                    break;
                case 'Done':
                    donePoints += task.estimatedPoints;
                    break;
                default:
                    console.log(`Invalid status ${task.status} for task ${task.taskId}!`);
            }
        });
    });

    const otherPoints = toDoPoints + inProgressPoints + codeReviewPoints;
    const success = donePoints >= otherPoints;
    console.log(`ToDo: ${toDoPoints}pts`);
    console.log(`In Progress: ${inProgressPoints}pts`);
    console.log(`Code Review: ${codeReviewPoints}pts`);
    console.log(`Done Points: ${donePoints}pts`);
    console.log(success ? 'Sprint was successful!' : 'Sprint was unsuccessful...');
}
runSprint(
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