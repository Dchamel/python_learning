import vk, auth_keys, unittest, csv, time
from time import perf_counter
from datetime import date, datetime

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


def get_some_from_wall(groupid, offset):
    data_vk = vk_api.wall.get(domain=groupid, count=100, offset=offset, v=auth_keys.api_ver)

    return data_vk


def get_all_from_wall(groupid):
    time.sleep(0.35)
    wall_count = vk_api.wall.get(domain=groupid, count=1, v=auth_keys.api_ver)['count']
    print(wall_count)
    steps = wall_count // 100 + 1
    offset = 0
    raw_data = []
    for counter in range(steps):
        time.sleep(0.35)
        raw_data.append(get_some_from_wall(groupid, offset))
        offset += 100
        print(f'Number of steps: {steps}. Now is - {counter}')

    raw_data1 = {'items': []}
    for each in raw_data:
        raw_data1['items'] += (each['items'])

    print(raw_data)

    return raw_data1


def data_proc(data_vk):
    # get all users id and filter attachments
    from_id_list = []
    for index, each in enumerate(data_vk['items']):
        from_id_list.append(str(each['from_id']))

        # deleting links, trash-info and other photos
        try:
            data_vk['items'][index]['attachments'] = each['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            continue

    # deleting duplicates
    from_id_list = list(set(from_id_list))
    from_id_string = ','.join(from_id_list)

    # get user names & surnames from id
    time.sleep(0.35)
    data_vk_from_id = vk_api.users.get(user_ids=from_id_string, v=auth_keys.api_ver, lang=auth_keys.lang)

    # processing data_vk again just for change 'id' to 'names'
    # and change UNIX-date to humanfriendly
    for index, each in enumerate(data_vk['items']):

        # work with names
        if str(each['from_id']) == auth_keys.group_id:
            data_vk['items'][index]['from_id'] = auth_keys.group_name_ru
        else:
            for each_user_name in data_vk_from_id:
                print(each_user_name['id'])
                if each_user_name['id'] == each['from_id']:
                    full_name = each_user_name['first_name'] + ' ' + each_user_name['last_name']
                    data_vk['items'][index]['from_id'] = full_name

        # work with date
        data_vk['items'][index]['date'] = str(datetime.fromtimestamp(each['date']))

    print(data_vk)
    return data_vk


def write_data(path, all_data_from_wall):
    try:
        file_name = auth_keys.group_name
        current_date = date.today().strftime('%d%m%Y')
        with open(path + file_name + current_date + '.csv', 'w', encoding='utf-8', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(('post_id', 'from_user', 'date', 'text', 'attachment'))
            for linedata in all_data_from_wall['items']:
                linedata['from_id'] = linedata['from_id']
                csvwriter.writerow((linedata['id'], linedata['from_id'], linedata['date'], linedata['text'],
                                    linedata['attachments']))
        return True
    except:
        return False


def read_data(path):
    file_name = auth_keys.group_name
    current_date = date.today().strftime('%d%m%Y')
    with open(path + file_name + current_date + '.csv', 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
    return data


vk_api = vk.API(access_token=auth_keys.api_token)

raw_data = get_all_from_wall(auth_keys.group_name)
processed_data = data_proc(raw_data)

# get_all_from_wall(auth_keys.group_name)

result_write_file = write_data(auth_keys.path, processed_data)
print(result_write_file)

rawData = read_data(auth_keys.path)


# print(rawData)


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
