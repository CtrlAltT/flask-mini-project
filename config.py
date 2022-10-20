"""
Get json file path
"""
import os


def get_path():
    try:
        path = os.path.dirname(__file__)
        file = path + '/cv.json'
        return file
    except IOError as ex:
        raise ex




