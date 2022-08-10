import requests


def get_json(endpoint):
    response = requests.get(endpoint)

    if response.ok:
        json_data = response.json()
        return json_data
    else:
        print('Status Code: ', response.status_code)
        print('Response Content: ', response.content)
        raise Exception('Something went wrong..')

if __name__ == '__main__':
    endpoint = 'https://api.github.com/events'
    data = get_json(endpoint)
    print(data)

