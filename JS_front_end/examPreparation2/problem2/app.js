window.addEventListener('load', solve);

function solve() {
    const inputDOMSelectors = {
        title: document.getElementById('task-title'),
        category: document.getElementById('task-category'),
        description: document.getElementById('task-content')
    }
    const otherDOMselectors = {
        publishBtn: document.getElementById('publish-btn'),
        reviewList: document.getElementById('review-list'),
        publishedList: document.getElementById('#published-list'),
        main: document.getElementById('main')
    }

    const taskData = {
        title: null,
        category: null,
        description: null
    };

    otherDOMselectors.publishBtn.addEventListener('click', publishTask);

    function publishTask() {
        console.log('clicked')
        // validate - check is all input fields are filled
        const allFieldsHaveValue = Object.values(inputDOMSelectors)
            .every((input) => input.value !== '');
        if (!allFieldsHaveValue) {
            return;
        }

        const { title, category, description } = inputDOMSelectors;
        const li = createElement('li', otherDOMselectors.reviewList, null, ['rpost']);
        const article = createElement('article', li);
        createElement('h4', article, `${title.value}`);
        createElement('p', article, `Category: ${category.value}`);
        createElement('p', article, `Content: ${description.value}`);

        const editBtn = createElement('button', li, 'Edit', ['action-btn', 'edit']);
        const postBtn = createElement('button', li, 'Post', ['action-btn', 'post']);

    }




    function clearAllInputs() {
        Object.values(inputDOMSelectors)
            .forEach(element => {
                element.value = '';
            });
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

}