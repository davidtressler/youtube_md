
# youtube_md

import sys
import subprocess
import json


into_jsondata = {}

class metadata:
    def __init__(self, link_url):
        global into_jsondata
        try:
            self.link = link_url
        except:
            pass

        try:
            proc = subprocess.Popen(["youtube-dl", "--cookies", "cookies.txt","-j", self.link],stdout=subprocess.PIPE,)
            out = proc.communicate()[0]
        except:
            print("Error, update youtube-dl and check cookies.txt is in current directory")

        try:
            into_jsondata = json.loads(out.decode('utf-8')) #Format into JSON
        except:
            pass
    def showall(self):
        pass

    def thumbnail(self):
        try:
            return into_jsondata["thumbnails"][3]["url"]
        except:
            pass

    def title(self):
        try:
            return into_jsondata["title"]
        except:
            pass

    def url(self):
        """ Finds Number Of Videos Formats, then sets count to minus 3, as this is HD with audio (needs more testing on range of videos formats)"""
        count = 0
        while True:
            try:
                stream_link = into_jsondata["formats"][count]["url"]
                count = count + 1
            except:
                break
        count = count - 1

        try:

            return into_jsondata["formats"][count]["url"]
        except:

            pass

        #return into_jsondata

    def find_number_of_formats():
        """ Finds Number Of Videos Formats and Minus one (needs more testing on range of videos formats)"""
        count = 0
        while True:
            try:
                stream_link = into_jsondata["formats"][count]["url"]
                count = count + 1
            except:
                break
        try:
            return count - 1
        except:
            pass
