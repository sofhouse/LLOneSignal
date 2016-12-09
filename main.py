import OneSignal.OSConnection

connection = OneSignal.OSConnection.OSConnection()
response = OneSignal.OSResponse.OSResponse()


response = connection.createNotification()
print(response.response)
response = connection.cancelNotification("37854982356923695")
print(response.response)