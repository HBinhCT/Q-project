const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    expect(solution.__get__('factorial')(4)).toBe(24);
})
