import requests

class ScrapFloatrates(object):
    def __init__(self, url = 'http://www.floatrates.com/daily/idr.json'):
        self.__set_json_data(url)

    def __set_json_data(self, url = 'http://www.floatrates.com/daily/idr.json'):
        response = requests.get(url)
        json_data = response.json()

        self.__response_status = response.status_code
        self.__json_data = json_data     

    def get_response_status(self):
        return self.__response_status
    
    def get_json_data(self):
        return self.__json_data


if __name__ == "__main__":
    url = 'http://www.floatrates.com/daily/idr.json'
    sfr = ScrapFloatrates(url)

    print(sfr.get_response_status())
    print(sfr.get_json_data())
