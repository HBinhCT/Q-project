function onClicked(e) {
    const btn = e.target;
    const action = document.querySelector(`#${btn.id}`).innerHTML;
    const res = document.querySelector('#res');

    switch (action) {
        case '0':
        case '1':
        case '+':
        case '-':
        case '*':
        case '/':
            res.innerHTML += action;
            break;
        case 'C':
            res.innerHTML = '';
            break;
        case '=':
            let expr = res.innerHTML;
            const nums = /(\d+)/g;
            // Replace all base 2 nums with base 10 equivs
            expr = expr.replace(nums, match => parseInt(match, 2));
            // Eval in base 10 and convert to base 2
            res.innerHTML = Math.floor(eval(expr).toString(2)).toString();
            break;
        default:
            console.error('Should not be executed!');
            break;
    }
}

const buttons = document.querySelectorAll('button');
for (let button of buttons) {
    button.addEventListener('click', onClicked);
}
