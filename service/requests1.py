#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01.06.2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import requests

image = requests.get('https://icdn.lenta.ru/images/2020/06/01/11/20200601111839866/pic_eccb9013380f3365d55588c1b530a9b4.png')

print(image)

with open('foto.jpg', 'wb') as f:
    f.write(image.content)