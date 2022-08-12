# This code consumes an API, in this case is 'https://api.github.com/events'.

# The library 'requests' allows to send HTTP requests using Python
import requests


# Function to define the response of the get method in json format,
# if it is ok, all right, it gives json data;
# else it gives the status code, the content and an exception.
def get_json(end):
    response = requests.get(end)

    if response.ok:
        json_data = response.json()
        return json_data
    else:
        print('Status Code: ', response.status_code)
        print('Response Content: ', response.content)
        raise Exception('Something went wrong..')

# If statement to consume an API, GET reads an existing resource.
if __name__ == '__main__':
    endpoint = 'https://api.github.com/events'
    data = get_json(endpoint)
    print(data)