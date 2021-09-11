class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        """
        a + b = (x + yi) + (u + vi) = (x + u) + (y + v)i
        :param no: Complex
        :return: Complex
        """
        real_sum = self.real + no.real
        imaginary_sum = self.imaginary + no.imaginary
        return Complex(real_sum, imaginary_sum)

    def __sub__(self, no):
        """
        a - b = (x + yi) - (u + vi) = (x - u) + (y - v)i
        :param no: Complex
        :return: Complex
        """
        real_diff = self.real - no.real
        imaginary_diff = self.imaginary - no.imaginary
        return Complex(real_diff, imaginary_diff)

    def __mul__(self, no):
        """
        z . w = (x + yi) . (u + vi)
              = x(u + vi) + yi(u + vi)          by the (right) distributive law
              = xu + xvi + yiu + yivi           by the (left) distributive law
              = xu + yivi + xvi + yiu           by the commutativity of addition
              = xu + yvi^2 + xvi + yui          by the commutativity of multiplication
              = (xu + yvi^2) + (xvi + yui)      by the associativity of addition
              = (xu - yv) + (xvi + yui)         by the defining property of i
              = (xu - yv) + (xv + yu)i          by the distributive law
        :param no: Complex
        :return: Complex
        """
        real_prod = self.real * no.real - self.imaginary * no.imaginary
        imaginary_prod = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_prod, imaginary_prod)

    def __truediv__(self, no):
        """
        a = x + yi
        ā = x - yi

        1 / a = ā / (a . ā)
              = ā / |a|^2
              = ā / (x^2 + y^2)
              = x / (x^2 + y^2) - (y / (x^2 + y^2))i

        w / a = w . 1 / a
              = (u + vi) . (x / (x^2 + y^2) (y / (x^2 + y^2))i)
              = ((ux + vy) + (vx - uy)i) / (x^2 + y^2)
        :param no: Complex
        :return: Complex
        """
        conj = Complex(no.real, -no.imaginary)
        num = self * conj
        denom = no * conj
        real_quo = num.real / denom.real
        imaginary_quo = num.imaginary / denom.real
        return Complex(real_quo, imaginary_quo)

    def mod(self):
        """
        |z| = sqrt( a^2 + b^2 )
        :return: Complex
        """
        m = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
