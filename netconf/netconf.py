# NETCONF
# Install ncclient: python3 -m pip install ncclient

from ncclient import manager
from ncclient.xml_ import to_ele
from xml.dom.minidom import parseString


# Device connection details
credentials = {
    "host": "devnetsandboxiosxe.cisco.com",
    "port": 830,
    "username": "admin",
    "password": "YOUR_PASSWORD",
    "hostkey_verify": False
}


# Create a NETCONF connection
# **credentials passes the dictionary values into manager.connect()
connection = manager.connect(**credentials)


# Retrieve the running configuration
config_data = connection.get_config(source="running")


# Convert the XML into a more readable format
config_show = parseString(config_data.data_xml).toprettyxml()
print(config_show)


# Read the XML configuration file
# The file contains YANG/XML data rather than Cisco CLI commands
with open("config1.xml", "r") as file:
    config = file.read()


# Send the configuration to the running configuration
edit_config = connection.edit_config(
    target="running",
    config=config
)

print(edit_config)


# NETCONF filter
# Requests interface data from the ietf-interfaces YANG model
interface_filter = to_ele("""
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface/>
    </interfaces>
</filter>
""")


# Retrieve only the interface data matching the filter
response = connection.get(interface_filter)


# Pretty-print the returned XML
print(parseString(response.xml).toprettyxml())


# Close the NETCONF session
connection.close_session()
