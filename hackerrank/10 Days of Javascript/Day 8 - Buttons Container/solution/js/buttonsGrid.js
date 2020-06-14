const nums = [1, 2, 3, 6, 9, 8, 7, 4];
const ids = [...nums];

const btn5 = document.querySelector('#btn5');

btn5.addEventListener('click', () => {
    nums.unshift(nums.pop());
    for (let i = 0; i <= 7; ++i) {
        document.querySelector(`#btn${ids[i]}`).innerHTML = nums[i].toString();
    }
});
