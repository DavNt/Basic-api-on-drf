"""
    get data and populate model script
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task101.settings')
import django
django.setup()

import requests

from taskapp.models import Picture, PicId


# fetching data then populate model
def getting():
    r = requests.get('https://picsum.photos/v2/list')
    data = r.json()
    for pic in data:
        ids = pic['id']
        author = pic['author']
        width = pic['width']
        height = pic['height']
        url = pic['url']
        download_url = pic['download_url']

        # populate the model
        pic = Picture.objects.get_or_create(id=ids, author=author, width=width, height=height, url=url,
                                      download_url=download_url)
        PicId.objects.get_or_create(id=pic, url=download_url)


if __name__ == '__main__':
    print('populating script')
    getting()
    print('done!')
