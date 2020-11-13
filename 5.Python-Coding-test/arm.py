# Arm Coding test

import collections


class Rare:

    def isiterable(p_object):
        try:
            iter(p_object)
        except TypeError:
            return False
        return True

    def integerchecker(num_check):
        try:
            isinstance(num_check, int)
        except TypeError:
            return False
        return True

    @staticmethod
    def nth_most_rare(elements, to_find):
        Rare.isiterable(elements)
        Rare.integerchecker(to_find)
        if to_find < 1:
            print("'n' must be positive")
        else:
            counts = collections.Counter(elements)
            least = list(reversed(counts.most_common()[-to_find:]))[-1]
            return least[-1]


num = [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5]
rare_num_finder = Rare
print(rare_num_finder.nth_most_rare(num, 0))
