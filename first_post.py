import requests


def login(credentials):
    response = requests.post('http://127.0.0.1:8080/api/rest-auth/login', data=credentials)

    if response.ok:
        print('Login: Success!')
        print(response.json())
        auth_token = response.json()['key']
        print(auth_token)
        #return auth_token
    else:
        raise Exception('Error. ', response.status_code)


if __name__ == '__main__':
    credentials = {"username": "polly", "password" : "viva la vita"}
    login(credentials)