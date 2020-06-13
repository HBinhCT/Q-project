const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('Mr.X')).toBe(true);
})

test('Test case 1', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('Mrs.Y')).toBe(true);
})

test('Test case 2', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('Dr#Joseph')).toBe(false);
})

test('Test case 3', async () => {
    const re = solution.__get__('regexVar')();
    expect(re.test('Er .Abc')).toBe(false);
})
