#!/usr/bin/env python3
# coding: utf8

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title RTEU Rehberden Bul
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon ☎️
# @raycast.argument1 { "type": "text", "placeholder": "İsim veya Dahili No", "percentEncoded": false }
# @raycast.packageName rteu-rehber

# Documentation:
# @raycast.author Uygar
# @raycast.authorURL https://github.com/uygaraydin

import sys
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from tabulate import tabulate
import ast

url = 'http://rehber.erdogan.edu.tr/search_json.php'
post_fields = {"search":sys.argv[1]}

data = urlencode(post_fields).encode('utf-8')
request = Request(url, data=data)
json = urlopen(request).read().decode('unicode-escape')[3:]
print(data)
arr=ast.literal_eval(json)

print(tabulate(arr, headers=["AD SOYAD", "BİRİM", "DAHİLİ"], tablefmt="grid", maxcolwidths=[40, 30, 20])) if len(arr)>0 else print("No Record")


