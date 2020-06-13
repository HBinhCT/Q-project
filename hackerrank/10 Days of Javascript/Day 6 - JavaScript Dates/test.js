const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const getDayName = solution.__get__('getDayName');
    expect(getDayName('10/11/2009')).toBe('Sunday');
    expect(getDayName('11/10/2010')).toBe('Wednesday');
})
