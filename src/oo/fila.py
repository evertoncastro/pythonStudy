
class Fila(object):

    c_fila = []

    def __init__(self):
        self.s_fila = []

    def self_add(self, number):
        self.c_fila.append(number)
        print self.c_fila

    @classmethod
    def cls_add(cls, number):
        cls.c_fila.append(number)
        print cls.c_fila 

    def print_self_fila(self):
        print self.c_fila

    @classmethod
    def print_cls_fila(cls):
        print cls.c_fila            