import OneSignal.OSConnection

connection = OneSignal.OSConnection.OSConnection()
response = OneSignal.OSResponse.OSResponse()


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

response = connection.createNotification(filters)
print(response.response)

response = connection.cancelNotification("37854982356923695")
print(response.response)