#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     04.06.2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
