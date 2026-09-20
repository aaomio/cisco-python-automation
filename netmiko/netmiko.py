# Netmiko
# Install Netmiko: python3 -m pip install netmiko

from netmiko import ConnectHandler


# Device connection details
credentials = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "YOUR_PASSWORD",
    "secret": "YOUR_PASSWORD"
}


# Create an SSH connection to the Cisco device
# **credentials unpacks the dictionary into the function
connection = ConnectHandler(**credentials)


# Check whether the connection is alive
connection_status = connection.is_alive()
print(connection_status)


# Enter privileged EXEC mode
connection.enable()


# Send the commands stored in conf1.cfg
# The file should contain Cisco IOS configuration commands
config_output = connection.send_config_from_file("conf1.cfg")
print(config_output)


# Run a show command and store the returned output
# The output is returned as a Python string
command_output = connection.send_command("show ip interface brief")
print(command_output)


# Close the SSH connection
connection.disconnect()


# Check the connection again after disconnecting
connection_status = connection.is_alive()
print(connection_status)
