from pymongo import MongoClient
import datetime
import sys

now = datetime.datetime.now()

client = MongoClient('192.168.12.87',27017)
db=client.mir_db
collection = db.siem_temp

alarm_name = sys.argv[4]
src_ip = sys.argv[2]
dest_ip = sys.argv[3]
md5 = "NA"
des_user_name = "NA"
src_user_name = "NA"
priority = int(sys.argv[1])
end_time = "NA"
url = "NA"
device_ip = "NA"
source_dns = "NA"
countryName = "NA"
device_product = "NA"
device_vendor = "NA"
ioc = "ip_address"
ioc_provider = "Splunk"

alarm = {
        "id":now,"alarm_name":alarm_name,
        "src_ip":src_ip,
        "dst_ip":dest_ip, "device_ip":device_ip, "createdAt":now,
        "md5":md5, "source_dns":source_dns, "country":"NA",
        "country_name":countryName, "dst_user_name":des_user_name,
        "src_user_name":src_user_name, "device_product":device_product,
        "device_vendor":device_vendor, "priority":priority, "end_time":end_time,
        "ioc":ioc, "ioc_provider":ioc_provider, "url":url, "is_new":"yes"
        }
rec_id1 = collection.insert_one(alarm)
print(rec_id1)


