import random
from math import sqrt


class KeyGen:
    def __init__(self):
        self.rand = random

    @staticmethod
    def convert_to_seed(key):
        gen_key = 0
        for letter in key:
            gen_key += ord(letter)
        return gen_key

    @staticmethod
    def square_like(alpha_len):
        x = int(sqrt(alpha_len))
        if alpha_len % x != 0:
            y = x + 1
            return {"x": x, "y": y}
        return {"x": x, "y": x}

    @staticmethod
    def matrix_check(matrix_x, matrix_y, key, matrix_string, pos):
        if matrix_x == len(matrix_string):
            pos = 0
            if matrix_y > len(key) - 1:
                key.append(matrix_string)
            matrix_string = {}
        return matrix_string, pos

    def set_seed(self, seed):
        self.rand.seed(seed)

    def generate_key(self, alphabet):
        key = list()
        alphabet = sorted(list(set(alphabet)))
        matrix_size = self.square_like(len(alphabet))
        matrix_string = dict()
        pos = 0
        while len(alphabet) > 0:
            matrix_string[alphabet.pop(self.rand.randint(0, len(alphabet)) - 1)] = pos
            pos += 1
            matrix_string, pos = self.matrix_check(matrix_size["x"], matrix_size["y"], key, matrix_string, pos)
        if matrix_string:
            key.append(matrix_string)
        return key