users = [
    {
        'id': 1,
        'username': 'him',
        'password': '123abc'
    }
]

username_mapping = {'bob':
    {
        'id': 1,
        'username': 'him',
        'password': '123abc'
    }
}

userid_mapping = {1:
    {
        'id': 1,
        'username': 'him',
        'password': '123abc'
    }
}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user && user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)