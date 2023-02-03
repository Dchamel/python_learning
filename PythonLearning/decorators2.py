# ---------------------------------------------------

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


user = User('just_user', ' user')
admin = User('just_admin', 'admin')

current_user = admin


def do_admin_work():
    if current_user.role != 'admin':
        raise Exception('Access Forbidden!')
    return 'Doing somth'


# print(do_admin_work())

# ---------------------------------------------------

def do_admin_work2():
    return 'Doing somth2'


def check_access(func):
    if current_user.role != 'admin':
        raise Exception('Access Forbidden2!')
    return func()


print(check_access(do_admin_work2))


# ---------------------------------------------------
def check_access2(func):
    def wrapper():
        if current_user.role != 'admin':
            raise Exception('Access Forbidden2!')
        return func()

    return wrapper


do_admin_work2 = check_access2(do_admin_work2)
print(do_admin_work2.__name__)


# ---------------------------------------------------
@check_access2
def do_admin_work3():
    return 'Doing somth3'


print(do_admin_work3())
print(do_admin_work3.__name__)


# ---------------------------------------------------
def check_access3(func):
    def wrapper(*args, **kwargs):
        if current_user.role != 'admin':
            raise Exception('Access Forbidden2!')
        return func(*args, **kwargs)

    return wrapper


@check_access3
def do_admin_work4(input):
    return f'Doing somth4 {input}'


print(do_admin_work4(1))
