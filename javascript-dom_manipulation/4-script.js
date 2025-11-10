document.querySelector('#add_item').onclick = function () {
    var li = document.createElement('li');
    li.innerHTML = 'Item';
    document.querySelector('ul.my_list').appendChild(li);
}