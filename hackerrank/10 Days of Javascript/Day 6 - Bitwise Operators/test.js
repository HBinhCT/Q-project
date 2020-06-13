const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const getMaxLessThanK = solution.__get__('getMaxLessThanK');
    expect(getMaxLessThanK(5, 2)).toBe(1);
    expect(getMaxLessThanK(8, 5)).toBe(4);
    expect(getMaxLessThanK(2, 2)).toBe(0);
})

test('Test case 1', async () => {
    const getMaxLessThanK = solution.__get__('getMaxLessThanK');
    expect(getMaxLessThanK(9, 2)).toBe(1);
    expect(getMaxLessThanK(8, 3)).toBe(2);
})
