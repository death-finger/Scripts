from urllib import request
from weathercodes import wea_codes

def getWeather(srvr, codes):
    data = request.urlopen(srvr)
    data = data.read().decode().split('\n')
    result = {}
    for chstr, cod in wea_codes:
        for line in data:
            if cod in line:
                result[chstr] = line[len(cod)+2:-len(cod)-3]
    return result


if __name__ == '__main__':
    srvr = 'http://php.weather.sina.com.cn/xml.php?city=%e3%c9%d0%d0&password=DJOYnieT8234jlsK&day=0'
    res = getWeather(srvr, wea_codes)
    print(res)