const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const Rectangle = solution.__get__('Rectangle');
    const Square = solution.__get__('Square');
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);
    expect(rec.area()).toBe(12);
    expect(sqr.area()).toBe(9);
})
