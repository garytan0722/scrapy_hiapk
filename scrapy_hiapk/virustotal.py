# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import simplejson
import urllib
import urllib2
import time
import json
import os
class virustotal():
    def report(self,md5,path):
        print("report")
        print(md5)
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        parameters = {"resource": " ","apikey": "e83d749addb188c2742ce86849e31704731a06d6331136a40b0be573265d2db7"}
        parameters["resource"]=md5
        print(parameters)
        data = urllib.urlencode(parameters)    
        req = urllib2.Request(url, data)
        time.sleep(30)
        response = urllib2.urlopen(req)
        result=json.load(response)
        filename=md5+".apk"
        os.system("mv /Users/garytan/Desktop/android_hack/android_apk/"+path+" /Users/garytan/Desktop/android_hack/android_apk/full/"+filename)
        positives=result["positives"]
        if positives>5:
            command="mv /Users/garytan/Desktop/android_hack/android_apk/full/"+filename+" /Users/garytan/Desktop/android_hack/android_problem/"+filename
            os.system(command)
        else:
            command="mv /Users/garytan/Desktop/android_hack/android_apk/full/"+filename+" /Users/garytan/Desktop/android_hack/android_normal/"+filename
            os.system(command)
        
        #os.system("sh /Users/garytan/Desktop/android_hack/android_apk/md5.sh")   