# Splunk-custom-alert-action

Use case of this alert:
1. Alert is used to send security events to your SIEM your your SOAR platform
2. Write query to capture security attacks like bruteforce, port scanning etc using your device logs
3. field name for source ip should be "Attacker IP", destination ip should be "Destination IP" and attack name should be "attack" to make this alert action work

update splunk information to mysql database
1. this is a splunk enterprise alert action
2. Code can be used to update the data from splunk query on mysql table
3. Mongo db code will update data on mongodb
4. You may have to add the credentials of you mysql or mongodb database on the bin/send_log_to_server.py or bin/send_log_to_mongod.py file

Steps to install alert action:
1. Copy the code on your splunk app folder, <splunk-home>/etc/apps
2. Restart your splunk enterprise
3. On success, your alert action will be available under alert action on splunk enterprise.

Steps to use it:
1. Create alert by saving your query as alert
2. Under alert action, select your alert
3. add the severity of the attack you are capturing
3. Save the alert
