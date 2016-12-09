import json

import OneSignal.OSHeader
import OneSignal.OSPayload
import OneSignal.OSResponse
import requests

from OneSignal.OSPayload import OSPayload


class OSConnection:

    def __init__(self):
        with open("OneSignal/OneSignal.config") as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content]

        self.oneSignalUrl = content[0]
        self.authToken = content[1]
        self.app_id = content[2]

        self.header = OneSignal.OSHeader.OSHeader(self.authToken)
        self.payload = OneSignal.OSPayload.OSPayload(self.app_id)
        self.response = OneSignal.OSResponse.OSResponse()

    def createNotification(self, filters):
        self.payload.filters = filters
        payload = json.dumps(self.payload.__dict__, default=OSPayload.encodeFilters, indent=4, sort_keys=True)
        print(payload)
        req = requests.post(self.oneSignalUrl, headers=self.header.getHeader(), data=payload)
        print("POST: ",req.status_code, req.reason)
        self.response.response = req.json()
        return self.response

    def cancelNotification(self, notificationId):
        req = requests.delete(self.oneSignalUrl + "/"+notificationId+"?app_id="+self.app_id, headers=self.header.getHeader())
        print("DELETE: ",req.status_code, req.reason)
        self.response.response = req.json()
        return self.response