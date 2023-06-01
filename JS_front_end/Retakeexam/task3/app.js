function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    const inputTitle = document.getElementById('course-name');
    const inputType = document.getElementById('course-type');
    const inputDescription = document.getElementById('description');
    const inputTeacher = document.getElementById('teacher-name');

    const addBtn = document.getElementById('add-course');
    const saveBtn = document.getElementById('edit-course');
    const loadBtn = document.getElementById('load-course');

    const mainForm = document.getElementById('form');
    const coursesList = document.getElementById('list');

    loadBtn.addEventListener('click', loadBtnHandler);
    saveBtn.addEventListener('click', saveBtnHandler);
    addBtn.addEventListener('click', addBtnHandler);

    function loadBtnHandler(event) {
        if (event) { event.preventDefault(); }

        saveBtn.disabled = true;

        fetch(BASE_URL)
            .then((data) => data.json())
            .then((tasksResponse) => {
                coursesList.innerHTML = '';
                const tasks = Object.values(tasksResponse);
                // console.log(tasks);
                for (const { _id, title, type, description, teacher } of tasks) {
                    const div = document.createElement('div');
                    div.classList.add('container');
                    div.id = _id;

                    const h2Title = document.createElement('h2');
                    h2Title.textContent = title;
                    const h3Teacher = document.createElement('h3');
                    h3Teacher.textContent = teacher;
                    const h3Type = document.createElement('h3');
                    h3Type.textContent = type;
                    const h4Descr = document.createElement('h4');
                    h4Descr.textContent = description;

                    const finishBtn = document.createElement('button');
                    finishBtn.classList.add('finish-btn');
                    finishBtn.textContent = 'Finish Course'
                    finishBtn.addEventListener('click', finishTaskHandler);

                    const editBtn = document.createElement('button');
                    editBtn.classList.add('edit-btn');
                    editBtn.textContent = 'Edit Course'
                    editBtn.addEventListener('click', editBtnHandler);

                    div.append(h2Title, h3Teacher, h3Type, h4Descr, editBtn, finishBtn);
                    coursesList.appendChild(div);
                }

            })
            .catch((err) => {
                console.log(err);
            })

    }

    function saveBtnHandler(event) {
        const liParent = event.currentTarget.parentNode;
        const id = documernt.getElementById('record-id').textContent;
        const [input] = Array.from(liParent.children);
        const httpHeaders = {
            method: 'PUT',
            body: JSON.stringify({
                title: inputTitle.value,
                type: inputType.value,
                description: inputDescription.value,
                teacher: inputTeacher.value
            })
        }
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadTaskHandler())
            .catch((err) => {
                console.log(err);
            })


    }


    function editBtnHandler(event) {
        const divParent = event.currentTarget.parentNode;
        const _id = divParent.id;
        divParent.remove()
        console.log(BASE_URL + _id)
        fetch(BASE_URL + _id)
            .then((data) => data.json())
            .then((response) => {
                const task = Object.values(response);
                // console.log(task);
                // const { _id, title, type, description, teacher } = task;
                inputTitle.value = task[0];
                inputDescription.value = task[2];
                inputType.value = task[1];
                inputTeacher.value = task[3];


                const idx = document.createElement('label')
                idx.textContent = _id;
                idx.id = 'record-id'
                idx.hidden = true;
                mainForm.appendChild(idx);
                addBtn.setAttribute('disabled', true);
                saveBtn.removeAttribute('disabled');
            })

    }

    function addBtnHandler(event) {
        if (event) { event.preventDefault(); }
        const title = inputTitle.value;
        const description = inputDescription.value;
        const type = inputType.value;
        const teacher = inputTeacher.value;

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ title, type, description, teacher })
        }
        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadBtnHandler();
                inputTitle.value = '';
                inputDescription.value = '';
                inputType.value = '';
                inputTeacher.value = '';
            })
            .catch((err) => {
                console.log(err);
            })
    }

    function finishTaskHandler(event) {

    }

}




















attachEvents();