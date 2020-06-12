const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    expect(solution.__get__('modifyArray')([1, 2, 3, 4, 5])).toStrictEqual([3, 4, 9, 8, 15]);
})
