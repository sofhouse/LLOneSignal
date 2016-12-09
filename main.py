import OneSignal.OSConnection

connection = OneSignal.OSConnection.OSConnection()
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


response = connection.createNotification(payload)
print(response.response)

response = connection.cancelNotification("37854982356923695")
print(response.response)