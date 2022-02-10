import requests

def convert_cur(from_cur, to_cur, amount=1):
    url = f"https://v6.exchangerate-api.com/v6/462078e42ed014b981331528/pair/{from_cur}/{to_cur}/{amount}"
    # Making our request
    response = requests.get(url)
    data = response.json()

    # Your JSON object
    last = data['time_last_update_utc']
    res = data['conversion_result']

    result = {
        'update': last,
        'res': res
    }

    return result