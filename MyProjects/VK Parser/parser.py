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
    with open(path + file_name + current_date + '.csv', 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
    return data


def get_all_from_wall(groupid):
    data_vk = vk_api.wall.get(domain=groupid, count=5, v=auth_keys.api_ver)
    # get all users id
    from_id_list = []
    for each in data_vk['items']:
        from_id_list.append(str(each['from_id']))
    from_id_string = ','.join(from_id_list)
    data_vk_from_id = vk_api.users.get(user_ids=from_id_string, v=auth_keys.api_ver)
    # print(data_vk_from_id)
    print(data_vk_from_id)

    # deleting links, trash-info and other photos

    return data_vk


def write_data(path, all_data_from_wall):
    file_name = auth_keys.group_name
    current_date = date.today().strftime('%d%m%Y')
    with open(path + file_name + current_date + '.csv', 'w', encoding='utf-8', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(('post_id', 'from_user', 'date', 'text', 'attachment'))
        for linedata in all_data_from_wall['items']:
            linedata['from_id'] = int(str(linedata['from_id'])[1:])
            csvwriter.writerow((linedata['id'], linedata['from_id'], linedata['date'], linedata['text'],
                                linedata['attachments']))


vk_api = vk.API(access_token=auth_keys.api_token)

all_data_from_wall = get_all_from_wall(auth_keys.group_name)
write_data(auth_keys.path, all_data_from_wall)

rawData = read_data(auth_keys.path)
print(rawData)


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
