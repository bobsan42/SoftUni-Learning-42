// TODO
function attachEvents() {

    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    const titleInput = document.getElementById('title');
    const loadBtn = document.getElementById('load-button');
    const addBtn = document.getElementById('add-button');
    const todoListContainer = document.getElementById('todo-list');

    loadBtn.addEventListener('click', loadTaskHandler);
    addBtn.addEventListener('click', addTaskHandler);

    function loadTaskHandler(event) {
        // event.preventDefault();
        // event?.preventDefault(); // NULL safe operator
        if (event) { event.preventDefault(); }

        fetch(BASE_URL)
            .then((data) => data.json())
            .then((tasksResponse) => {
                todoListContainer.innerHTML = '';
                const tasks = Object.values(tasksResponse);
                // console.log(tasks);
                for (const { _id, name } of tasks) {
                    const li = document.createElement('li');
                    li.id = _id;
                    const span = document.createElement('span');
                    const removeBtn = document.createElement('button');
                    const editBtn = document.createElement('button');
                    editBtn.addEventListener('click', editTaskHandler);

                    span.textContent = name;
                    removeBtn.textContent = 'Remove';
                    removeBtn.addEventListener('click', removeTaskhandler);
                    editBtn.textContent = 'Edit';
                    // May not work in JUDGE

                    li.append(span, removeBtn, editBtn);
                    todoListContainer.appendChild(li);
                }

            })
            .catch((err) => {
                console.log(err);
            })
    }

    function editTaskHandler(event) {
        const liParent = event.currentTarget.parentNode;
        // const children = Array.from(liParent.children);
        // console.log(children);
        const [span, _removeBtn, editBtn] = Array.from(liParent.children);
        const editInput = document.createElement('input');
        editInput.value = span.textContent;
        liParent.prepend(editInput);
        const submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit';
        submitBtn.addEventListener('click', submitTaskHandler)
        liParent.appendChild(submitBtn);
        span.remove();
        editBtn.remove();
    }

    function submitTaskHandler(event) {
        const liParent = event.currentTarget.parentNode;
        const id = liParent.id;
        const [input] = Array.from(liParent.children);
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({ name: input.value })
        }
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadTaskHandler())
            .catch((err) => {
                console.log(err);
            })

    }

    function addTaskHandler(event) {
        if (event) { event.preventDefault(); }
        const name = titleInput.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        }
        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadTaskHandler();
                titleInput.value = '';
            })
            .catch((err) => {
                console.log(err);
            })
    }

    function removeTaskhandler(event) {
        if (event) { event.preventDefault(); }
        const liParent = event.currentTarget.parentNode;
        const id = liParent.id;
        const httpHeaders = {
            method: 'DELETE'
        };
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadTaskHandler())
            .catch(handleError);

    }

    function handleError(err) {
        console.log(err);
    }
}

attachEvents();
