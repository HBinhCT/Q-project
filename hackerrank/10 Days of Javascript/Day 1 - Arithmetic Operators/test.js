const rewire = require('rewire');

const solution = rewire('./solution')

test('Test case 0', async () => {
    expect(solution.__get__('getArea')(3, 4.5)).toBe(13.5);
    expect(solution.__get__('getPerimeter')(3, 4.5)).toBe(15)
})