import math


class QuadraticEquation:

    def discriminant(a, b, c):
        result = (b*b) - 4 * a * c
        return result

    def roots_equation(a, b, discriminant):
        solutions = [0, 1]
        solutions[0] = (- b + math.sqrt(discriminant))/2 * a
        solutions[1] = (- b - math.sqrt(discriminant))/2 * a
        return solutions
