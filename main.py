import OneSignal.OSConnection

oneSignalUrl = "https://onesignal.com/api/v1/notifications"
authToken = "NTI1NDBlMTItNzZiZS00ZDhkLTgxM2EtMjE0YzQ3YjI2NWM5"
app_id = "7d02bfcd-e065-42a3-9949-21506a47f788"

connection = OneSignal.OSConnection.OSConnection(oneSignalUrl=oneSignalUrl, authToken=authToken,app_id=app_id)

response = OneSignal.OSResponse.OSResponse()
payload = OneSignal.OSPayload.OSPayload()

filters = list()

filter1 = OneSignal.OSFilter.OSFilter()
filter1.field = "tag"
filter1.key = "level"
filter1.relation = "="

operator1 = OneSignal.OSOperator.OSOperator("OR")

filter2 = OneSignal.OSFilter.OSFilter()
filter2.field = "tag"
filter2.key = "level"
filter2.relation = "="
filter2.value = "50"

filters.append(filter1)
filters.append(operator1)
filters.append(filter2)

payload.filters = filters

payload.send_after = "September 24th 2016, 2:00:00 pm UTC-07:00"
payload.delayed_option =  "timezone"
payload.delivery_time_of_day = "9:00AM"
payload.ttl = 600
payload.priority = 10

payload.included_segments = ["All"]

payload.content = {
       "id": "Notification ID Number",
       "tipo_notificacion": "string",
       "titulo": "Titulo" ,
       "subtitulo": "Subtitulo" ,
       "fecha_entrega": "fecha",
       "parametros": { "param1": "param1" , "param2": "param2" },
       "estado": True
}

response = connection.createNotification(payload)
print(response.response)

response = connection.cancelNotification("37854982356923695")
print(response.response)