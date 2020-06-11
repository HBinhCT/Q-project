const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const result = [];
    [1, 2, 3].forEach(num => {
        try {
            result.push(solution.__get__('isPositive')(num));
        } catch (e) {
            result.push(e.message);
        }
    })
    expect(result).toStrictEqual(['YES', 'YES', 'YES']);
})

test('Test case 1', async () => {
    const result = [];
    [2, 0, 6].forEach(num => {
        try {
            result.push(solution.__get__('isPositive')(num));
        } catch (e) {
            result.push(e.message);
        }
    })
    expect(result).toStrictEqual(['YES', 'Zero Error', 'YES']);
})

test('Test case 3', async () => {
    const result = [];
    [-1, 20].forEach(num => {
        try {
            result.push(solution.__get__('isPositive')(num));
        } catch (e) {
            result.push(e.message);
        }
    })
    expect(result).toStrictEqual(['Negative Error', 'YES']);
})
