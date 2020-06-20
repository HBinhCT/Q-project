class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i
                j = n // i
                if i != j:
                    total += j
        return total


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
