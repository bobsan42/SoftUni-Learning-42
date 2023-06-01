window.addEventListener("load", solve);

//- always use array from to transform a collection -> queryselectorall, children

function solve() {
  // const p = createElement('p', document.getElementById('preview-list'), 'My Paragraph<br>My Paragraph', ['story', 'test', 'paragraph'], 'my-pid', null)
  const inputDOMSelectors = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    title: document.getElementById('story-title'),
    genre: document.getElementById('genre'),
    story: document.getElementById('story')
  }

  const otherDOMselectors = {
    publishBtn: document.getElementById('form-btn'),
    previewList: document.getElementById('preview-list'),
    main: document.getElementById('main')
  }

  const storyData = {
    firstName: null,
    lastName: null,
    age: null,
    title: null,
    genre: null,
    story: null
  };

  otherDOMselectors.publishBtn.addEventListener('click', publishStoryHandler);

  function publishStoryHandler(event) {
    // debugger;
    // validate - check is all input fields are filled
    const allFieldsHaveValue = Object.values(inputDOMSelectors)
      .every((input) => input.value !== '');
    // console.log (allFieldsHaveValue);
    if (!allFieldsHaveValue) {
      // console.log('SOME FIELDS ARE EMPTY!');
      return;
    }
    // create elements and add data to preview
    const { firstName, lastName, age, title, genre, story } = inputDOMSelectors;
    const li = createElement('li', otherDOMselectors.previewList, null, ['story-info']);
    const article = createElement('article', li);
    createElement('h4', article, `Name: ${firstName.value} ${lastName.value}`);
    createElement('p', article, `Age: ${age.value}`);
    createElement('p', article, `Title: ${title.value}`);
    createElement('p', article, `Genre: ${genre.value}`);
    createElement('p', article, story.value);

    const saveBtn = createElement('button', li, 'Save Story', ['save-btn']);
    const editBtn = createElement('button', li, 'Edit Story', ['edit-btn']);
    const deleteBtn = createElement('button', li, 'Delete Story', ['delete-btn']);
    
    
    
    
    // save data to another object - to be able to return it to the form
    for (const key in inputDOMSelectors) {
      storyData [key] = inputDOMSelectors[key].value; 
    }
    
    
    clearAllInputs();
    // otherDOMselectors.publishBtn.setAttribute('disabled', true) ;
    otherDOMselectors.publishBtn.disabled = true;
    
    editBtn.addEventListener ('click', editStoryHandler);
    
    function editStoryHandler () {
      for (const key in storyData) {
        inputDOMSelectors[key].value = storyData[key];
      }

      // otherDOMselectors.publishBtn.removeAttribute('disabled');
      otherDOMselectors.publishBtn.disabled = false;
      
      // otherDOMselectors.previewList.innerHTML = '';
      // createElement ('h3',otherDOMselectors.previewList, 'Preview' );
      // delete li; 
      otherDOMselectors.previewList.removeChild(li);
    }
    
    saveBtn.addEventListener('click', saveBtnHandler );
    
    function saveBtnHandler () {
      otherDOMselectors.main.innerHTML='';
      createElement('h1', otherDOMselectors.main, 'Your scary story is saved!');
    }
    
    deleteBtn.addEventListener ('click', deleteBtnHandler);
    
    function deleteBtnHandler (event) {
      // event.currentTarget.parentNode.remove();
      // this.parentNode.remove();
      li.remove();
      otherDOMselectors.publishBtn.disabled = false;
    }


    function clearAllInputs() {
      Object.values(inputDOMSelectors)
        .forEach(element => {
          element.value = '';
        });
    }


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
