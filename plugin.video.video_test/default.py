import sys
import xbmcgui
import xbmcplugin

import urllib
from bs4 import BeautifulSoup as bs

main_url = "http://fs.to/video/"
url_detailed = "?view=detailed"

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

html = urllib.urlopen(main_url + "films/" + url_detailed)
soup = bs(html, 'html.parser', from_encoding="utf-8")
content = soup.find_all("a", { "class" : "b-poster-detail__link" })
for data in content:
	li = xbmcgui.ListItem(data.span.span.img['alt'])
	#li.setIconImage('http:' + data.span.span.img['src'])
	xbmcplugin.addDirectoryItem(addon_handle, "", li)

li = xbmcgui.ListItem("Mune: Guardian of the Moon")
xbmcplugin.addDirectoryItem(addon_handle, "http://fs.to/get/dl/60pmsbw417f6vfittth1856ra.0.1139013157.2284938935.1468126747/Despicable.Me.2010.1080p.Eng.Rus.Dub.mkv", li);
#xbmcplugin.addDirectoryItem(addon_handle, "/home/rimmed/Downloads/Mune: Guardian of the Moon.mkv", li)

#li = xbmcgui.ListItem('My First Video!', iconImage='http://img.dotua.org/fsua_items/cover/00/42/35/2/00423542.jpg')
#info = {
#	'genre': 'Horror',
#	'year': 1979,
#	'title': 'Alien',
#	}
#li.setInfo('video', info)
#xbmcplugin.addDirectoryItem(addon_handle, "", li)

xbmcplugin.endOfDirectory(addon_handle)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs

# html = urlopen("http://fs.to/video/films/").read()
# soup = bs(html, 'html5lib', from_encoding="utf-8")
# soup.find("div", { "class" : "b-poster-tile   " })
# p.find('a')['href']
