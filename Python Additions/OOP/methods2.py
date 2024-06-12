class A:
    qwe = 'qwe'

    def __new__(cls, *args, **kwargs):
        print('new ' + str(cls.__name__))
        return super().__new__(cls)

    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y

    @classmethod
    def cls_method(cls):
        print('cls_method - {}'.format(A.qwe))


a1 = A(1, 2)
print(a1.qwe)
A.cls_method()
a2 = A(3, 4)
