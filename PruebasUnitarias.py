import unittest
import OneSignal


class TestOneSignalConnection(unittest.TestCase):

    def setUp(self):
        oneSignalUrl = "https://onesignal.com/api/v1/notifications"
        authToken = "NTI1NDBlMTItNzZiZS00ZDhkLTgxM2EtMjE0YzQ3YjI2NWM5"
        app_id = "7d02bfcd-e065-42a3-9949-21506a47f788"
        self.connection = OneSignal.OSConnection.OSConnection(oneSignalUrl=oneSignalUrl, authToken=authToken, app_id=app_id)

    def test_createNotification(self):
        print("test_createNotification")
        payload = OneSignal.OSPayload.OSPayload()
        payload.included_segments = ["All"]
        response = self.connection.createNotification(osPayload=payload)
        respPayload = response.json()
        print(respPayload)
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertEqual(respPayload["id"], "")
        self.assertNotEquals(respPayload["recipients"], 0)


    def test_createBatchNotification(self):
        print("test_createBatchNotification")
        payload = OneSignal.OSPayload.OSPayload()
        payload.included_segments = ["All"]
        with open("recipients.list") as f:
            recipients = f.read().splitlines()
        responses = self.connection.createBatchNotification(osPayload=payload, recipients=recipients, chunkSize=200)
        for response in responses:
            respPayload = response.json()
            print(respPayload)
            self.assertEqual(response.status_code, 200)
            self.assertFalse('errors' in respPayload)
            self.assertEqual(respPayload["id"], "")
            self.assertNotEquals(respPayload["recipients"], 0)

    def test_cancelNotification(self):
        print("test_cancelNotification")
        response = self.connection.cancelNotification(notificationId="37854982356923695")
        respPayload = response.json()
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)

if __name__ == '__main__':
    unittest.main()