__author__ = 'ict'

from calculate.distance import euclid

method_set = {
    "euclid": euclid,
}


def method(mtd, data_a, data_b):
    if mtd not in method_set:
        raise Exception("No such distance mothod")
    return method_set[mtd].compute(data_a, data_b)


def names():
    return list(method_set)