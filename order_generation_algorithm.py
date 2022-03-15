import time
from datetime import datetime
from random import randint
from substitution_cipher_algorithm import SubstitutionCipherAlgorithm
ORDER_MASKING_ID_LENGTH = 14


class OrderMaskingIdAlgorithm:

    def __init__(self):
        self.substitution_cipher_algorithm = SubstitutionCipherAlgorithm()

    def generate(self, date=None):
        #generate unix timestamp using date
        now = date if date else datetime.now()
        unix_timestamp = time.mktime(now.timetuple())*1e3 + now.microsecond/1e3
        absolute_unix_timestamp = str(int(unix_timestamp))

        #pad with additional random digits
        if len(absolute_unix_timestamp) < ORDER_MASKING_ID_LENGTH:
            pad = ORDER_MASKING_ID_LENGTH - len(absolute_unix_timestamp)
            absolute_unix_timestamp += self.__random_number_with_N_digits(pad)

        #encrypt
        absolute_unix_timestamp = self.substitution_cipher_algorithm.encrypt(absolute_unix_timestamp)

        #slice
        order_id_part_1, order_id_part_2, order_id_part_3 = \
            absolute_unix_timestamp[:4], absolute_unix_timestamp[4:10], absolute_unix_timestamp[10:]

        return str.join('-', (order_id_part_1, order_id_part_2, order_id_part_3))

    def __random_number_with_N_digits(self, length):
        range_start = 10**(length-1)
        range_end = (10**length)-1
        return str(randint(range_start, range_end))
