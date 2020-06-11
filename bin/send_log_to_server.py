import pymysql.cursors 
import sys

priority = int(sys.argv[1])
src_ip = sys.argv[2]
dest_ip = sys.argv[3]
alarm_name = sys.argv[4]
md5 = "NA"
destinationUserName = "NA"
sourceUserName = "NA"
end_time = "NA"
url = "NA"
device_ip = "NA"
source_dns = "NA"
countryName = "NA"                                                                  
device_product = "NA"
device_vendor = "NA"
ioc = "ip_address"
ioc_provider = "Splunk"

# Connect to the database.
connection = pymysql.connect(host='<ip address>',
                             user='<username>',
                             password='<password>',                             
                             db='<db>',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()		
    sql = sql = """INSERT INTO siem_temp_table(alarm_name,src_ip,dst_ip,device_ip,md5,source_dns,country_name,dst_user_name,src_user_name,
		 device_product,device_vendor,priority,end_time,ioc,ioc_provider,url,is_new)
         VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','Yes')""".format(alarm_name, src_ip, dest_ip,device_ip ,md5, source_dns, countryName, destinationUserName, sourceUserName, device_product, device_vendor, priority, end_time, ioc, ioc_provider, url)

    try:
        check_success = cursor.execute(sql)
        print(check_success)
        # Commit your changes in the database
        connection.commit()
    except pymysql.Error as e:
        print(e.args[0])
        print(e.args[1])

    finally:
        cursor.close()


print ("connect successful!!")