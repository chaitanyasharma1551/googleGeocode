import requests


def getGeoCode(address):
    api_key = "YOUR_ACCESS_KEY"
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), api_key))
    try:
        response = requests.get(url)
        api_response = response.json()
        lat = api_response['results'][0]['geometry']['location']['lat']
        lon = api_response['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR')
        lat = 0
        lng = 0
    return lat, lon