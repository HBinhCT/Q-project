const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    expect(solution.__get__('getCount')([
        {x: 1, y: 1},
        {x: 2, y: 3},
        {x: 3, y: 3},
        {x: 3, y: 4},
        {x: 4, y: 5},
    ])).toBe(2);
})
