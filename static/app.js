let my_form = document.getElementById('add-button');
let addButton = document.getElementById('add-person');
let form = document.getElementById('form');
let my_form2 = document.querySelector('.my-form');
let removeButton = document.getElementById('remove-person');

let node = my_form2.cloneNode(true)

addButton.addEventListener("click", () => {
    form.insertBefore(node.cloneNode(true), my_form)
});


removeButton.addEventListener("click", () => {
    let field = [...document.querySelectorAll('.my-form')].reverse();
    field[0].remove();
});
