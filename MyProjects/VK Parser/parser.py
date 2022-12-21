import vk, auth_keys, unittest
from time import perf_counter

t1 = perf_counter()


def write_data(path, data):
    with open(path, 'w') as auth_keys.group_name:
        return auth_keys.group_name(data)


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.readlines()


def get_wall(groupid):
    data = vk_api.wall.get(domain=groupid, count=2, v=auth_keys.api_ver)
    return data


vk_api = vk.API(access_token=auth_keys.api_token)

raw_data = get_wall(auth_keys.group_name)


# tests - not implemented
class AllTestsParser(unittest.TestCase):

    def setUp(self) -> None:
        self.path = auth_keys.path
        self.data = ''

    def test01_read_data(self):
        expected = 's'
        actual = read_data(self.path)[3]


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
