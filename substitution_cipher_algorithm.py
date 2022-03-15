import random

ALPHABET = "0123456789"


class SubstitutionCipherAlgorithm:
    def __init__(self):
        self.key = self.__make_key()

    def __make_key(self):
        self.__alphabet = list(ALPHABET)
        random.shuffle(self.__alphabet)
        return ''.join(self.__alphabet)

    def encrypt(self, plain_text):
        key_map = dict(zip(self.__alphabet, self.key))
        return ''.join(key_map.get(c.lower(), c) for c in plain_text)