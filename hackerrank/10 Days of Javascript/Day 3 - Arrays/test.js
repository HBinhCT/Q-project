const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    expect(solution.__get__('getSecondLargest')([2, 3, 6, 6, 5])).toBe(5);
})
