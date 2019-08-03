import obd
import os
import time

def clear():
    os.system('clear')

# connection = obd.OBD()  # auto-connects to USB or RF port
ports = obd.scan_serial()  # return list of valid USB or RF ports
print(ports)  # ['/dev/ttyUSB0', '/dev/ttyUSB1']
time.sleep(2)
connection = obd.OBD()
# print('1')
# time.sleep(1)
# clear()
cmd = obd.commands.RPM  # select an OBD command (sensor)
response = connection.query(cmd)  # send the command
# print('2')
# time.sleep(1)
# clear()
# print('rpm: {}'.format(response))  # "2410 RPM"
while connection:
    clear()
    cmd = obd.commands.RPM  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command
    clear()
    time.sleep(0.5)
    print('rpm: {}'.format(response))  # "2410 RPM"
    time.sleep(0.5)
    print('rere')
    time.sleep(0.5)
