const rewire = require('rewire');

const solution = rewire('./solution');
const logMock = jest.fn();
solution.__set__('console', {log: logMock});

test('Test case 0', async () => {
    solution.__get__('performOperation')('12', '4.32', 'is the best place to learn and practice coding!');
    expect(logMock.mock.calls.length).toBe(3);
    expect(logMock.mock.calls[0][0]).toBe(16);
    expect(logMock.mock.calls[1][0]).toBe(8.32);
    expect(logMock.mock.calls[2][0]).toBe('HackerRank is the best place to learn and practice coding!');
})
