# Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach.
# Wielomian będzie reprezentowany przez listę swoich współczynników,
# np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. Napisać kod testujący moduł polys.


def add_poly(poly1, poly2):
    poly3 = poly1
    length = len(poly2)
    for i in range(length):
        if i < len(poly3):
            poly3[i] = poly3[i] + poly2[i]
        else:
            poly3.append(poly2[i])

    return poly3


def sub_poly(poly1, poly2):
    poly3 = poly1
    length = len(poly2)
    for i in range(length):
        if i < len(poly3):
            poly3[i] = poly3[i] - poly2[i]
        else:
            poly3.append(-poly2[i])

    return poly3


def mul_poly(poly1, poly2):
    poly3 = [0] * (len(poly1) + len(poly2))

    length1 = len(poly1)
    length2 = len(poly2)

    for i in range(length1):
        for j in range(length2):
            poly3[i + j] = poly3[i + j] + (poly1[i] * poly2[j])

    return poly3


def is_zero(poly):
    length = len(poly)

    for i in range(length):
        if poly[i] != 0:
            return False

    return True


def eq_poly(poly1, poly2):
    if len(poly1) != len(poly2):
        return False

    length = len(poly1)

    for i in range(length):
        if poly1[i] != poly2[i]:
            return False

    return True


def eval_poly(poly, x):
    length = len(poly)
    poly.reverse()
    result = poly[0]

    for i in range(1, length):

        result = result * x + poly[i]

    return result


def pow_poly(poly1, x):
    poly2 = poly1
    if x == 2:
        poly2 = mul_poly(poly1, poly1)
    elif x > 2:
        for i in range(x):
            poly2 = mul_poly(poly1, poly2)

    return poly2


def show_poly(poly1):
    if len(poly1) != 0:
        length = len(poly1) - 1
        print("W(x) = " + str(poly1[0]), end=" ")
        for i in range(length):
            if poly1[i + 1] == 0:
                continue
            else:
                print(f"{poly1[i+1]:+}" + "x^" + str(i + 1), end=" ")
    else:
        print("W(x) =  0")
    print()


def combine_poly(poly1, poly2):
    poly3 = []
    poly3.append(poly1[0])
    length1 = len(poly1)

    for i in range(1, length1):
        poly4 = []
        poly4 = pow_poly(poly2, i)
        poly5 = [element * poly1[i] for element in poly4]
        poly3 = add_poly(poly3, poly5)

    return poly3


def diff_poly(poly1):
    length = len(poly1)
    poly2 = poly1

    for i in range(1, length):
        poly2[i - 1] = poly2[i] * i

    poly2[length - 1] = 0
    return poly2


import unittest


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0, 1]  # W(x) = x
        self.p2 = [0, 0, 1]  # W(x) = x*x

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1, 0])

    def test_is_zero(self):
        self.assertEqual(is_zero(self.p1), False)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 2), 2)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 2), [0, 0, 1, 0])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p2), [0, 2, 0])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()  # uruchamia wszystkie testy
