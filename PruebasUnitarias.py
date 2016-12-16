import unittest
import OneSignal
import datetime


class TestOneSignalConnection(unittest.TestCase):

    notificationId = "987570407512057901579"

    def setUp(self):
        oneSignalUrl = "https://onesignal.com/api/v1/notifications"
        authToken = "NTI1NDBlMTItNzZiZS00ZDhkLTgxM2EtMjE0YzQ3YjI2NWM5"
        app_id = "7d02bfcd-e065-42a3-9949-21506a47f788"
        self.llave = "llave"
        self.valor = "dos"
        self.connection = OneSignal.OSConnection.OSConnection(oneSignalUrl=oneSignalUrl, authToken=authToken, app_id=app_id)
        self.ahora  = datetime.datetime.now()
        self.despues = self.ahora + datetime.timedelta(minutes=2)
        self.ahoraString = self.ahora.strftime('%Y-%m-%d %H:%M:%S GMT-0500')
        self.despuesString = self.despues.strftime('%Y-%m-%d %H:%M:%S GMT-0500')


    def test_00printdate(self):
        print(self.ahoraString)
        print(self.despuesString)
        fecha = "2016-12-16 10:30:00 GMT-0500"

    def test_01notificarEtiqueta(self):
        print("test_01notificarEtiqueta")
        payload = OneSignal.OSPayload.OSPayload()
        filters = list()
        filter1 = OneSignal.OSFilter.OSFilter()
        filter1.field = "tag"
        filter1.key = self.llave
        filter1.value = self.valor
        filter1.relation = "="
        filters.append(filter1)
        payload.filters = filters

        payload.contents = {"en": "English Message test_01notificarEtiqueta", "es": "Spanish Message test_01notificarEtiqueta"}
        payload.headings = {"en": "English Title test_01notificarEtiqueta", "es": "Spanish Title test_01notificarEtiqueta"}

        payload.data = {
            "id": "Notification ID Number",
            "tipo_notificacion": "string",
            "en": "Test Notification",
            "es": "Notificacion prueba",
            "titulo": "Titulo",
            "subtitulo": "Subtitulo",
            "fecha_entrega": "fecha",
            "parametros": {"param1": "param1", "param2": "param2"},
            "estado": True
        }

        response = self.connection.createNotification(osPayload=payload)
        respPayload = response.json()
        print(respPayload)
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertNotEqual(respPayload["id"], "")
        self.assertNotEquals(respPayload["recipients"], 0)

    def test_02notificarEtiquetaDiferida(self):
        print("test_02notificarEtiquetaDiferida")
        payload = OneSignal.OSPayload.OSPayload()
        filters = list()
        filter1 = OneSignal.OSFilter.OSFilter()
        filter1.field = "tag"
        filter1.key = self.llave
        filter1.value = self.valor
        filter1.relation = "="
        filters.append(filter1)
        payload.filters = filters

        payload.contents = {"en": "English Message test_02notificarEtiquetaDiferida", "es": "Spanish Message test_02notificarEtiquetaDiferida"}
        payload.headings = {"en": "English Title test_02notificarEtiquetaDiferida", "es": "Spanish Title test_02notificarEtiquetaDiferida"}

        payload.data = {
            "id": "Notification ID Number",
            "tipo_notificacion": "string",
            "en": "Test Notification",
            "es": "Notificacion prueba",
            "titulo": "Titulo",
            "subtitulo": "Subtitulo",
            "fecha_entrega": "fecha",
            "parametros": {"param1": "param1", "param2": "param2"},
            "estado": True
        }

        payload.send_after = self.despuesString

        response = self.connection.createNotification(osPayload=payload)
        respPayload = response.json()
        print(respPayload)
        TestOneSignalConnection.notificationId = respPayload["id"]
        print(self.notificationId)
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertNotEqual(respPayload["id"], "")
        self.assertNotEquals(respPayload["recipients"], 0)

    def test_03cancelNotification(self):
        print("test_03cancelNotification: "+self.notificationId)
        response = self.connection.cancelNotification(notificationId=self.notificationId)
        respPayload = response.json()
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertEqual(respPayload["success"], True)

    def test_06notificarEtiquetaDiferida(self):
        print("test_06notificarEtiquetaDiferida")
        payload = OneSignal.OSPayload.OSPayload()
        filters = list()
        filter1 = OneSignal.OSFilter.OSFilter()
        filter1.field = "tag"
        filter1.key = self.llave
        filter1.value = self.valor
        filter1.relation = "="
        filters.append(filter1)
        payload.filters = filters

        payload.contents = {"en": "English Message test_06notificarEtiquetaDiferida", "es": "Spanish Message test_06notificarEtiquetaDiferida"}
        payload.headings = {"en": "English Title test_06notificarEtiquetaDiferida", "es": "Spanish Title test_06notificarEtiquetaDiferida"}

        payload.data = {
            "id": "Notification ID Number",
            "tipo_notificacion": "string",
            "en": "Test Notification",
            "es": "Notificacion prueba",
            "titulo": "Titulo",
            "subtitulo": "Subtitulo",
            "fecha_entrega": "fecha",
            "parametros": {"param1": "param1", "param2": "param2"},
            "estado": True
        }

        payload.send_after = self.despuesString

        response = self.connection.createNotification(osPayload=payload)
        respPayload = response.json()
        print(respPayload)
        TestOneSignalConnection.notificationId = respPayload["id"]
        print(self.notificationId)
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertNotEqual(respPayload["id"], "")
        self.assertNotEquals(respPayload["recipients"], 0)

    def test_04notificarTodos(self):
        print("test_04notificarTodos")
        payload = OneSignal.OSPayload.OSPayload()
        payload.included_segments = ["All"]
        payload.contents = {"en": "English Message test_04notificarTodos", "es": "Spanish Message test_04notificarTodos"}
        payload.headings = {"en": "English Title test_04notificarTodos", "es": "Spanish Title test_04notificarTodos"}
        response = self.connection.createNotification(osPayload=payload)
        respPayload = response.json()
        print(respPayload)
        self.assertEqual(response.status_code, 200)
        self.assertFalse('errors' in respPayload)
        self.assertNotEqual(respPayload["id"], "")
        self.assertNotEquals(respPayload["recipients"], 0)

    def test_05createBatchNotification(self):
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

if __name__ == '__main__':
    unittest.main()