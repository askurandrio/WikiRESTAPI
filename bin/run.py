"""This file run APP"""


from lib.rest import APP


if __name__ == '__main__':
    APP.run(port=80) #TODO: Replace to WSGI server
