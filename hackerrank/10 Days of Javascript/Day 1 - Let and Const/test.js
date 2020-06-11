const rewire = require('rewire');

const solution = rewire('./solution');
const logMock = jest.fn();
const errorMock = jest.fn();
solution.__set__('console', {log: logMock, error: errorMock});

test('Test case 0', async () => {
    solution.__set__('readLine', jest.fn(() => 2.6));
    solution.__get__('main')();
    expect(logMock.mock.calls.length).toBe(2);
    expect(logMock.mock.calls[0][0]).toBe(21.237166338267002);
    expect(logMock.mock.calls[1][0]).toBe(16.336281798666924);
    expect(errorMock.mock.calls.length).toBe(1);
    expect(errorMock.mock.calls[0][0]).toBe("You correctly declared 'PI' as a constant.");
})
