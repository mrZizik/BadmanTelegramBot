# -*- coding: utf-8 -*-
mem_id = "82468060"
url = "https://api.imgflip.com/caption_image"
import urllib, urllib2
import json


text0 = "Mem0" + ","
loc="ru"
if loc=="ru":
	text1="МОЖЕМ ЛИ МЫ ДОВЕРЯТЬ ЕМУ?"
else:
	text1= "CAN WE TRUST HIM?"

post_fields = {'User-Agent' : "Magic Browser",'template_id': mem_id, 'username': 'batman_bot', 'password':'batmanmojemlimidoveryat', 'text0': text0, 'text1': text1}     # Set POST fields here
request = urllib2.Request(url, urllib.urlencode(post_fields).encode(), headers={'User-Agent' : "Magic Browser"})
j = urllib2.urlopen(request).read().decode()
ret = json.loads(j)
print ret["data"]["url"]