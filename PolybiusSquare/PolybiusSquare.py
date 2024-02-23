from PolybiusSquare.KeyGen import KeyGen


class PolybiusSquare:
    def __init__(self, alpha):
        self.alphabet = sorted(list(set(alpha)))

    @staticmethod
    def set_logic(seed):
        gen = KeyGen()
        gen.set_seed(gen.convert_to_seed(seed))
        return gen

    @staticmethod
    def add_to_data(data, keys, pos, letter, letter_pos):
        for key, value in keys[pos].items():
            if value == letter_pos:
                data[letter] = key
                return data
        return data

    @staticmethod
    def reverse(position, key):
        position -= 1
        if position < 0:
            position = len(key) - 1
        return position

    @staticmethod
    def direct(position, key):
        position += 1
        if position > len(key) - 1:
            position = 0
        return position

    @staticmethod
    def iteration(pos, reverse):
        if reverse:
            return pos - 1
        return pos + 1

    @staticmethod
    def next_row(key, reverse):
        if reverse:
            return len(key) - 1
        return 0

    def under_string(self, position, key, reverse=False):
        if reverse:
            return self.reverse(position, key)
        return self.direct(position, key)

    def polybius(self, cript_data, letter, key, pos, reverse=False):
        while not (letter in key[pos].keys()):
            pos = self.iteration(pos, reverse)
        letter_pos = key[pos][letter]
        pos = self.under_string(pos, key, reverse)
        cript_data = self.add_to_data(cript_data, key, pos, letter, letter_pos)
        if not cript_data.get(letter, False):
            pos = self.under_string(pos, key, reverse)
            cript_data = self.add_to_data(cript_data, key, pos, letter, letter_pos)
        return cript_data

    def prepare_cryption(self, open_text, key, reverse=False):
        cript_data = {}
        set_alpha = set(open_text)
        for letter in set_alpha:
            pos = self.next_row(key, reverse)
            cript_data = self.polybius(cript_data, letter, key, pos, reverse)
        return cript_data

    def get_key(self, seed):
        gen = self.set_logic(seed)
        key = gen.generate_key(self.alphabet)
        return key

    def start(self, open_text, seed, reverse=False):
        text = str()
        gen = self.set_logic(seed)
        key = gen.generate_key(self.alphabet)
        cript_data = self.prepare_cryption(open_text, key, reverse)
        for i in open_text:
            text += cript_data.get(i, " ")
        return text
