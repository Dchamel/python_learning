class A(float):
    # def __new__(cls, *args, **kwargs):
    # if cls is A:
    #     print("is A")
    # elif cls.__name__[:3] == "BBB":
    #     print("is BBB")
    # return super().__new__(cls)

    def __init__(self):
        print('class A')
        if self is A:
            print("is A")
        elif self.__class__[:3] == "BBB":
            print("is BBB")
        return super().__new__(self)


class BBB_1241(A):
    def __init__(self):
        super().__init__()
        print('class B')


if __name__ == '__main__':
    a = A()

    print("\n=============\n")

    b = BBB_1241()
