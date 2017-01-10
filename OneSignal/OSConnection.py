import json
import requests

from .OSHeader import OSHeader
from .OSPayload import OSPayload
from .OSResponse import OSResponse
from .OSFilter import OSFilter
from .OSOperator import OSOperator


class OSConnection:

    def __init__(self, one_signal_url, auth_token, app_id):
        self.oneSignalUrl = one_signal_url
        self.authToken = auth_token
        self.app_id = app_id
        self.header = OSHeader(self.authToken)
        self.response = OSResponse()
        self.payload = None

    def create_notification(self, os_payload):
        self.payload = os_payload
        self.payload.app_id = self.app_id
        json_payload = json.dumps(self.payload.__dict__, default=OSPayload.encode_filters, indent=4, sort_keys=True)
        self.response = requests.post(self.oneSignalUrl, headers=self.header.get_header(), data=json_payload)
        return self.response

    def cancel_notification(self, notification_id):
        self.response = requests.delete(
            self.oneSignalUrl + "/"+notification_id+"?app_id="+self.app_id,
            headers=self.header.get_header()
        )
        return self.response

    def create_batch_notification(self, os_payload, recipients):
        or_operator = OSOperator("OR")
        filters = list()
        for recipient in recipients:
            os_filter = OSFilter()
            os_filter.field = "tag"
            os_filter.key = "email"
            os_filter.relation = "="
            os_filter.value = recipient
            filters.append(os_filter)
            filters.append(or_operator)
        filters = filters[0:len(filters)-1]
        os_payload.filters = filters
        return self.create_notification(os_payload)
