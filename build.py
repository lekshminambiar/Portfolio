# Builds the GitHub Pages index.html from the artifact source (index-v3.html)
import re
src=open('/home/user/site/index-v3.html').read()
head_bits=[]
def grab(m):
    head_bits.append(m.group(0));return ''
top,rest=src[:6000],src[6000:]
top=re.sub(r'<title>.*?</title>|<meta (?:name|property)="(?:description|og:[^"]+|twitter:[^"]+)"[^>]*>|<link rel="canonical"[^>]*>',grab,top,flags=re.S)
body=top+rest
out='<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+'\n'.join(head_bits)+'\n<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style></head><body>\n'+body+'\n</body></html>\n'
open('/home/user/portfolio/index.html','w').write(out)
print(len(head_bits),'head tags')
