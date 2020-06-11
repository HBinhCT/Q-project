const rewire = require('rewire');

const solution = rewire('./solution');
const logMock = jest.fn();
solution.__set__('console', {log: logMock});

test('Test case 0', async () => {
    solution.__get__('greeting')('Welcome to 10 Days of JavaScript!');
    expect(logMock.mock.calls.length).toBe(2);
    expect(logMock.mock.calls[0][0]).toBe('Hello, World!');
    expect(logMock.mock.calls[1][0]).toBe('Welcome to 10 Days of JavaScript!');
})
