const rewire = require('rewire');

const solution = rewire('./solution');
let logMock;

beforeEach(() => {
    logMock = jest.fn();
    solution.__set__('console', {log: logMock});
});

test('Test case 0', async () => {
    solution.__get__('vowelsAndConsonants')('javascriptloops');
    const result = logMock.mock.calls.map(value => value[0]).join('\n');
    expect(result).toBe(
        'a\n' +
        'a\n' +
        'i\n' +
        'o\n' +
        'o\n' +
        'j\n' +
        'v\n' +
        's\n' +
        'c\n' +
        'r\n' +
        'p\n' +
        't\n' +
        'l\n' +
        'p\n' +
        's'
    );
})
