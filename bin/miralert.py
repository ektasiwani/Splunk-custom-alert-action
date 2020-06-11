import requests
import sys,os
import json
import logging
import logging.handlers
import subprocess


def setup_logger(level):
    logger = logging.getLogger("mir_alert_logger")
    logger.propagate = False
    logger.setLevel(level)
    file_handler = logging.handlers.RotatingFileHandler("/opt/splunk/var/log/splunk/mir_alert.log",maxBytes=2500000000)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger(logging.INFO)

def main():
    if len(sys.argv) > 1 and sys.argv[1]== "--execute":
        
       
        payload = json.loads(sys.stdin.read())
        logger.info(payload)
        result = payload.get('result')
	src_ip = result.get('Attacker IP')
        dest_ip = result.get('Destination IP')
	attack = result.get('attack')
        config = payload.get('configuration')
        severity = config.get('severity')
        p  = os.system("/opt/splunk/bin/python3 /opt/splunk/etc/apps/miralert/bin/send_log_to_server.py "+ str(severity)+ " " +src_ip+ " " +dest_ip+ " " +attack)
        #p  = os.system("/usr/bin/python /opt/splunk/etc/apps/miralert/bin/send_log_to_mongod.py "+ str(severity)+ " " +src_ip+ " " +dest_ip+ " " +attack)

if __name__ == "__main__":
    main()
