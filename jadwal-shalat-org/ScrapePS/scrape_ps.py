import requests
from datetime import datetime
from bs4 import BeautifulSoup

class ScrapePS(object):
    def __init__(self, url='https://jadwalsholat.org/adzan/monthly.php?id=94'):
        """Initialize Class."""
        self.__url = url
        self.__get_website_data()
        self.__get_region_timezone()
        self.__get_datetime()
    
    __id_to_en_month = {
        'Januari' : 'January'
        , 'Februari' : 'February'
        , 'Maret' : 'March'
        , 'April' : 'April'
        , 'Mei' : 'May'
        , 'Juni' : 'June'
        , 'Juli' : 'July'
        , 'Agustus' : 'August'
        , 'September' : 'September'
        , 'Oktober' : 'October'
        , 'November' : 'November'
        , 'Desember' : 'Desember'
    }

    def __get_website_data(self):
        """GET WEBSITE DATA."""
        self.__response = requests.get(self.__url)
        self.__contents = BeautifulSoup(self.__response.text, 'html.parser')

    def __get_region_timezone(self):
        """GET REGION AND TIMEZONE."""
        contents = self.__contents.find_all('h1', class_='h1_edit')[0].string
        temp = str(contents).replace('Jadwal Sholat untuk ', '').strip()
        self.__region, self.__timezone = temp.split(', ')

    def __get_datetime(self):
        """GET DATETIME."""
        curr_month_year = self.__contents.find_all('h2', class_='h2_edit')[0].string
        curr_date_row = self.__contents.find_all('tr', class_='table_highlight')[0]

        temp_pray_time = [data.string for i, data in enumerate(curr_date_row)]

        # -- DATA CLEANING -- 
        clean_pray_time = []

        self.__pray_time = {
            'Imsyak' : None
            , 'Shubuh' : None
            , 'Terbit' : None
            , 'Dhuha' : None
            , 'Dzuhur' : None
            , 'Ashr' : None
            , 'Maghrib' : None
            , 'Isya' : None
        }

        for i, data in enumerate(temp_pray_time):            
            if i == 0:
                str_date = str(data + ' ' + curr_month_year).split(' ')
                str_date[1] = self.__id_to_en_month[str_date[1]]
                str_date = '-'.join(str_date)

                continue

            curr_date_data = str_date + ' ' + data
            time_data = datetime.strptime(curr_date_data, '%d-%B-%Y %H:%M')

            clean_pray_time.append(time_data)

        for key, time in zip(self.__pray_time, clean_pray_time):
            self.__pray_time[key] = time

    def get_url(self):
        """Return website's URL."""
        return self.__url

    def get_response(self):
        """Return response."""
        return self.__response

    def get_region_timezone(self):
        """Return region and it's timezone."""
        return self.__region, self.__timezone

    def get_pray_time(self):
        """Return pray time in dictionary format."""
        return self.__pray_time


if __name__ == "__main__":
    scrape_ps = ScrapePS()
    print(scrape_ps.get_pray_time())
    print(scrape_ps.get_region_timezone())
