document.querySelector('#toggle_header').onclick = function () {
    document.querySelector('header').classList.toggle('red');
    document.querySelector('header').classList.toggle('green');
    if (document.querySelector('header').classList.contains('red')) {
        document.querySelector('#toggle_header').textContent = 'Change to Green';
    }
    else {
        document.querySelector('#toggle_header').textContent = 'Change to Red';
    }
}