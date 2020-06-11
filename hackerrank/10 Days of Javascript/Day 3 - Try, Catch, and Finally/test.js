const rewire = require('rewire');

const solution = rewire('./solution');
let logMock;

beforeEach(() => {
    logMock = jest.fn();
    solution.__set__('console', {log: logMock});
});

test('Test case 0', async () => {
    solution.__get__('reverseString')('1234');
    expect(logMock.mock.calls.length).toBe(1);
    expect(logMock.mock.calls[0][0]).toBe('4321');
})

test('Test case 1', async () => {
    solution.__get__('reverseString')(Number(1234));
    expect(logMock.mock.calls.length).toBe(2);
    expect(logMock.mock.calls[0][0]).toBe('s.split is not a function');
    expect(logMock.mock.calls[1][0]).toBe(1234);
})
