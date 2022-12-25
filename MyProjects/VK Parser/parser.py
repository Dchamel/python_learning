import vk, auth_keys, unittest, csv
from time import perf_counter
from datetime import date

t1 = perf_counter()


# Old way
# response = requests.get('https://api.vk.com/method/wall.get',
#                         params={
#                             'access_token': auth_keys.api_token,
#                             'v': auth_keys.api_ver,
#                             'domain': auth_keys.group_name,
#                             'count': 2
#                         })
#
# print(response.json())


def read_data(path):
    file_name = auth_keys.group_name
    current_date = date.today().strftime('%d%m%Y')
    with open(path + file_name + current_date + '.csv', 'r') as rawDataCsv:
        return rawData.readlines()


def get_all_from_wall(groupid):
    data = vk_api.wall.get(domain=groupid, count=2, v=auth_keys.api_ver)
    return data


def write_data(path, all_data_from_wall):
    file_name = auth_keys.group_name
    current_date = date.today().strftime('%d%m%Y')
    with open(path + file_name + current_date + '.csv', 'w', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(('post_id', 'from_user', 'date', 'text', 'attachment'))
        for linedata in all_data_from_wall['items']:
            linedata['from_id'] = int(str(linedata['from_id'])[1:])
            csvwriter.writerow((linedata['id'], linedata['from_id'], linedata['date'], linedata['text'],
                                linedata['attachments']))


vk_api = vk.API(access_token=auth_keys.api_token)

all_data_from_wall = get_all_from_wall(auth_keys.group_name)
write_data(auth_keys.path, all_data_from_wall)

read_data(auth_keys.path)


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
