const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const rec = solution.__get__('Rectangle')(4, 5);
    expect(rec.length).toBe(4);
    expect(rec.width).toBe(5);
    expect(rec.perimeter).toBe(18);
    expect(rec.area).toBe(20);
})
