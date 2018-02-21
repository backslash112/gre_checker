from bs4 import BeautifulSoup
import urllib2
import json
import time
import os
import subprocess
import webbrowser

def refresh():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', '<...>; JSESSIONID=<...>; step=myStatus.do; ajaxStep=viewAppointment; arp_scroll_position=402'))
    url = "https://gre.etest.net.cn/testSites.do?p=testSites&m=ajax&adminDate=2017-10-13&neeaID=71434856&cities=BEIJING_BEIJING%3BHEBEI_SHIJIAZHUANG%3B&citiesNames=%25E5%258C%2597%25E4%25BA%25AC%3B%25E7%259F%25B3%25E5%25AE%25B6%25E5%25BA%2584%3B&whichFirst=AS&isFilter=1&opt=reschedule"
    f = opener.open(url)
    res = f.read()
    jd = json.loads(res)
    return jd


def main():
    jd = refresh()
    # print(jd)
    # return
    for data in jd:
        for item in data['dates'][0]['sites']:
            print("%d: %s" % (item['realSeats'], item['siteName']))
            if item['realSeats'] > 0:
            	return True
    return False


def run():
	while True:
		ret = main()
		if not ret:
			open_website()
			play()
			
		time.sleep(30)

def play():
    mp3='file/sound.mp3'
    return_code = subprocess.call(["afplay",mp3])

def open_website():
    url = "https://gre.etest.net.cn/myStatus.do?neeaID=71434856"
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

if __name__ == "__main__":
	run()
