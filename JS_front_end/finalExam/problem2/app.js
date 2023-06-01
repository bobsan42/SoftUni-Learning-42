window.addEventListener('load', solve);

function solve() {
    const inputDOMSelectors = {
        id: document.getElementById('task-id'),
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        points: document.getElementById('points'),
        assignee: document.getElementById('assignee'),
        // deleteBtn : document.getElementById(''),

    }

    const otherDOMSelectors = {
        createBtn: document.getElementById('create-task-btn'),
        deleteBtn: document.getElementById('delete-task-btn'),
        tasksList: document.getElementById('tasks-section'),
        totalPoints: document.getElementById('total-sprint-points'),
        // deleteBtn = document.getElementById(''),
    }

    const labelIcons = {
        'Feature': String.fromCharCode(8865), // '&#8865;',
        'Low Priority Bug': String.fromCharCode(9737), //'&#9737;',
        'High Priority Bug': String.fromCharCode(9888) //'&#9888;'

    }

    const labelClasses = {
        'Feature': 'feature',
        'Low Priority Bug': 'low-priority',
        'High Priority Bug': 'high-priority'

    }

    const data = [];
    const record = {
        id: null,
        title: null,
        description: null,
        label: null,
        points: null,
        assignee: null
    };
    totalPoints = 0;

    otherDOMSelectors.createBtn.addEventListener('click', createTaskHandler);
    otherDOMSelectors.deleteBtn.addEventListener('click', deleteConfirmationHandler);


    function createTaskHandler(event) {
        print('hello');
        // validate - check is all input fields are filled
        if (inputDOMSelectors.id.value === '') {
            print(inputDOMSelectors.id.value);
            inputDOMSelectors.id.value = `task-${data.length + 1}`;
            print(inputDOMSelectors.id.value);
        }
        const allFieldsHaveValue = Object.values(inputDOMSelectors)
            .every((input) => input.value !== '');
        if (!allFieldsHaveValue) {
            // print ('NOPE')
            return;
        }

        const { id, title, description, label, points, assignee } = inputDOMSelectors;
        const art = createElement('article', otherDOMSelectors.tasksList, null, ['task-card'], id.value);
        const div1 = createElement('div', art, null, ['task-card-label', labelClasses[label.value]], null, null);
        div1.textContent = label.value + ' ' + labelIcons[label.value];
        print(div1.textContent);
        print(label.value);
        print(labelIcons[label.value]);
        const h3 = createElement('h3', art, id.value + title.value, ['task-card-title']);
        const p1 = createElement('p', art, description.value, ['task-card-description']);
        const div2 = createElement('div', art, `Estimated at ${points.value} pts`, ['task-card-points']);
        const div3 = createElement('div', art, `Assigned to: ${assignee.value}`, ['task-card-assignee']);
        const divActions = createElement('div', art, null, ['task-card-actions']);
        const eraseBtn = createElement('button', divActions, 'Delete', ['task-card-assignee']);
        eraseBtn.addEventListener('click', deleteTaskHandler);

        totalPoints += Number(points.value);
        otherDOMSelectors.totalPoints.textContent = `Total Points ${totalPoints}pts`

        for (const key in inputDOMSelectors) {
            record[key] = inputDOMSelectors[key].value;
        }
        data.push(record);
        clearAllInputs();
    }

    function deleteTaskHandler(event) {
        let task = event.currentTarget.parentNode.parentNode;
        let tid = task.id;
        let i = data.findIndex((x) => x.id === tid);
        let record = data[i];
        for (const key in record) {
            inputDOMSelectors[key].value = record[key]
            inputDOMSelectors[key].disabled = true;
        }
        otherDOMSelectors.createBtn.disabled = true;
        otherDOMSelectors.deleteBtn.disabled = false;
    }

    function deleteConfirmationHandler(event) {
        const tid = inputDOMSelectors.id.value
        let i = data.findIndex((x) => x.id === tid);
        let record = data[i];
        data[i].id = null;
        totalPoints -= Number(record.points);
        if ( tid !== '') {
            document.getElementById(tid).remove();
            Object.values(inputDOMSelectors)
                .forEach(element => {
                    element.value = '';
                    element.disabled= false;
                })
        }
        otherDOMSelectors.createBtn.disabled=false;
        otherDOMSelectors.deleteBtn.disabled=true;
        otherDOMSelectors.totalPoints.textContent = `Total Points ${totalPoints}pts`

    }

    function createElement(type, parentNode, content, classesArray, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);

        if (useInnerHtml) {
            htmlElement.innerHtml = content;
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content;
            }
            if (content && type === 'input') {
                htmlElement.value = content;
            }
        }

        if (classesArray && classesArray.length > 0) {
            htmlElement.classList.add(...classesArray);
        }

        if (id) {
            htmlElement.id = id;
        }

        // {src: 'link', href: 'http'}
        if (attributes) {
            for (const key in attributes) {
                // htmlElement[key] = attributes [key];
                htmlElement.setAttribute(key, attributes[key]);
            }
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;

    }

    function print(x) {
        console.log(x);
    }

    function clearAllInputs() {
        Object.values(inputDOMSelectors)
            .forEach(element => {
                element.value = '';
            });
    }


}