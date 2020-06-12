const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const sides = solution.__get__('sides');
    let s1, s2;
    [s1, s2] = [10, 14].sort();
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    expect(s1 === x).toBe(true);
    expect(s2 === y).toBe(true);
})
