const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('bcd')).toBe(false);
})

test('Test case 1', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('abcd')).toBe(false);
})

test('Test case 2', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('abcda')).toBe(true);
})

test('Test case 3', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('abcdo')).toBe(false);
})
