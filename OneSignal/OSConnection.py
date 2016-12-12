import json

import OneSignal.OSHeader
import OneSignal.OSPayload
import OneSignal.OSResponse
import requests

from OneSignal.OSPayload import OSPayload


class OSConnection:

    def __init__(self, oneSignalUrl, authToken, app_id):

        self.oneSignalUrl = oneSignalUrl
        self.authToken = authToken
        self.app_id = app_id
        self.header = OneSignal.OSHeader.OSHeader(self.authToken)
        self.response = OneSignal.OSResponse.OSResponse()
        self.payload = None

    def createNotification(self, osPayload):
        self.payload = osPayload
        self.payload.app_id = self.app_id
        jsonPayload = json.dumps(self.payload.__dict__, default=OSPayload.encodeFilters, indent=4, sort_keys=True)
        print(jsonPayload)
        self.response = requests.post(self.oneSignalUrl, headers=self.header.getHeader(), data=jsonPayload)
        return self.response

    def cancelNotification(self, notificationId):
        self.response = requests.delete(self.oneSignalUrl + "/"+notificationId+"?app_id="+self.app_id, headers=self.header.getHeader())
        return self.response

    def createBatchNotification(self, osPayload, recipients, chunkSize):
        responses = list()
        chunked = [recipients[i:i + chunkSize] for i in range(0, len(recipients), chunkSize)]
        for chunk in chunked:
            filters = list()
            for recipient in chunk:
                filter = OneSignal.OSFilter.OSFilter()
                filter.field = "tag"
                filter.relation = "="
                filter.value = recipient
                filters.append(filter)

            osPayload.filters = filters
            responses.append(self.createNotification(osPayload))
        return responses