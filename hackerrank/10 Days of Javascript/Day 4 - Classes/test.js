const rewire = require('rewire');

const solution = rewire('./solution');

test('Test case 0', async () => {
    const Polygon = solution.__get__('Polygon');
    const rectangle = new Polygon([10, 20, 10, 20]);
    const square = new Polygon([10, 10, 10, 10]);
    const pentagon = new Polygon([10, 20, 30, 40, 43]);
    expect(rectangle.perimeter()).toBe(60);
    expect(square.perimeter()).toBe(40);
    expect(pentagon.perimeter()).toBe(143);
})
