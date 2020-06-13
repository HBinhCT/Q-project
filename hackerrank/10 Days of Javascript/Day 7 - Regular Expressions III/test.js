const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const re = solution.__get__('regexVar')();
    expect('102, 1948948 and 1.3 and 4.5'.match(re)).toEqual(['102', '1948948', '1', '3', '4', '5']);
})

test('Test case 1', async () => {
    const re = solution.__get__('regexVar')();
    expect('1 2 3'.match(re)).toEqual(['1', '2', '3']);
})
