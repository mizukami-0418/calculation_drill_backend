import random
import math

class NumberGenerator:
    """整数と分数の生成を担当するクラス"""

    @staticmethod
    def generate_integer(digit_type, allow_negative=False):
        ranges = {1: (1, 9), 2: (10, 20), 3: (10, 50), 4: (10, 99)}
        num = random.randint(*ranges[digit_type])
        return num * random.choice([-1, 1]) if allow_negative else num

    @staticmethod
    def generate_fraction(digit_type, allow_negative=False):
        n_ranges = {1: (1, 9), 2: (10, 20), 3: (10, 50), 4: (10, 99)}
        d_ranges = {1: (2, 9), 2: (10, 20), 3: (10, 50), 4: (10, 99)}
        numerator = random.randint(*n_ranges[digit_type])
        denominator = random.randint(*d_ranges[digit_type])  # 分母は2以上
        numerator = numerator * random.choice([-1, 1]) if allow_negative else numerator
        return numerator, denominator


class FractionUtils:
    """分数計算のユーティリティクラス"""
    
    @staticmethod
    def simplify(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd
    
    @staticmethod
    def common_denominator(n1, n2, d1, d2):
        lcm = (d1 * d2) // math.gcd(d1, d2)
        return n1 * (lcm // d1), n2 * (lcm // d2), lcm


class Calculator:
    """計算を担当するクラス"""

    @staticmethod
    def calculate_integer(n1, n2, operator):
        if operator == '+':
            return n1 + n2
        elif operator == '-':
            return n1 - n2
        elif operator == '×':
            return n1 * n2
        elif operator == '÷':
            return round(n1 / n2, 2) if n2 != 0 else None
    
    @staticmethod
    def calculate_fraction(n1, n2, d1, d2, operator):
        if operator == '+':
            n1, n2, d = FractionUtils.common_denominator(n1, n2, d1, d2)
            return FractionUtils.simplify(n1 + n2, d)
        elif operator == '-':
            n1, n2, d = FractionUtils.common_denominator(n1, n2, d1, d2)
            return FractionUtils.simplify(n1 - n2, d)
        elif operator == '×':
            return FractionUtils.simplify(n1 * n2, d1 * d2)
        elif operator == '÷':
            return FractionUtils.simplify(n1 * d2, d1 * n2) if n2 != 0 else None


class DrillGenerator:
    """問題作成を担当するクラス"""

    def __init__(self, use_fraction, digit_type, allow_negative, operator, num_questions):
        self.use_fraction = use_fraction
        self.digit_type = digit_type
        self.allow_negative = allow_negative
        self.operator = operator
        self.num_questions = num_questions

    def generate_question(self):
        if self.use_fraction:
            n1, d1 = NumberGenerator.generate_fraction(self.digit_type, self.allow_negative)
            n2, d2 = NumberGenerator.generate_fraction(self.digit_type, self.allow_negative)
            return {"numerator1": n1, "denominator1": d1, "numerator2": n2, "denominator2": d2, "operator": self.operator}
        else:
            n1 = NumberGenerator.generate_integer(self.digit_type, self.allow_negative)
            n2 = NumberGenerator.generate_integer(self.digit_type, self.allow_negative)
            if self.operator == '-' and not self.allow_negative:
                n1, n2 = max(n1, n2), min(n1, n2)  # 負の数を回避
            return {"number1": n1, "number2": n2, "operator": self.operator}

    def generate_quiz(self):
        queitions = []
        for _ in range(self.num_questions):
            queitions.append(self.generate_question())
        return queitions
    
    
