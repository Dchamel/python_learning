class ToyClass:
    v1 = 12

    def instancemethod(self):
        return f'{self.v1} - instance method', self

    @classmethod
    def classmethod(cls):
        return f'{cls.v1} - class method - {cls.__name__[:3:-1]}', cls

    @staticmethod
    def staticmethod(v1):
        return f'{v1} - static method'


tc1 = ToyClass()

print(tc1.instancemethod())
print(ToyClass.instancemethod(tc1))

print(tc1.classmethod())
print(ToyClass.classmethod())

print(tc1.staticmethod(ToyClass.v1))
print(ToyClass.staticmethod(ToyClass.v1))
