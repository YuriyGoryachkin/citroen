import obd

# connection = obd.OBD()  # auto-connects to USB or RF port
ports = obd.scan_serial()  # return list of valid USB or RF ports
print(ports)  # ['/dev/ttyUSB0', '/dev/ttyUSB1']
connection = obd.OBD()
cmd = obd.commands.RPM  # select an OBD command (sensor)
response = connection.query(cmd)  # send the command
print(response)  # "2410 RPM"
