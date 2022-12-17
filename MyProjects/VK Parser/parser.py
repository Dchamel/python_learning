import vk, auth_keys


def get_wall(groupid):
    data = vk_api.wall.get(owner_id=groupid, count=2, v=5.131)
    return data


# Сервисный ключ доступа

# session = vk.session(access_token=token)  # Авторизация
vk_api = vk.API(access_token=auth_keys.token)

print(get_wall(auth_keys.group_id))
