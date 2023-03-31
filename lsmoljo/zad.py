import re
import datetime

log_path = "C:/Users/A507/lsmoljo/setupapi.dev2.log"
regex = r"^>>>  \[Device Install.*#(Disk&Ven_[A-Za-z0-9]+)&(Prod_([\w\s\S]+?))&(Rev_([\w\s\S]+?))#([\w\s\S]+?)#.*\]"
usb_devices = {
    "device_vendor_id": "",
    "device_product_id": "",
    "device_instance_id": "",
    "serial_number": "",
    "event_time": "",
}
# Read the contents of the setupapi.dev.log file
with open(log_path, "r") as log_file:
     # Store information about each USB device in a dictionary
     
     for line in log_file:
     # Find all USB device installation events and extract information about each device
        match =re.match(regex,line)
        if match:
            print(match.groups())
            usb_devices["device_vendor_id"] = match.groups()[0]
            usb_devices["device_product_id"] = match.groups()[1]
            usb_devices["device_instance_id"] = match.groups()[2]
            usb_devices["serial_number"] = match.groups()[5]
            match = next(log_file)
            usb_devices["event_time"] = match.split("start ", 1)[1].split("\n", 1)[0]
print(usb_devices)

