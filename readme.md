# Cisco Network Automation with Python

A Python project demonstrating three methods of automating Cisco IOS XE devices:

- **Netmiko** – SSH and Cisco CLI automation
- **NETCONF** – model-driven automation using YANG and XML
- **RESTCONF** – REST API automation using YANG with JSON/XML

## Cisco DevNet Sandbox

The labs use the [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com).

A Cisco IOS XE sandbox host can be created from the DevNet Sandbox portal. The hostname, username and password provided by the sandbox are then used by the Python scripts.

Example host:

```text
devnetsandboxiosxe.cisco.com
```

The sandbox can be used to practise all three automation methods against a Cisco IOS XE device.

## Protocols and Ports

| Technology | Protocol | Port | Purpose |
|---|---|---:|---|
| Netmiko | SSH | 22 | CLI access and configuration |
| NETCONF | SSH | 830 | YANG/XML-based configuration and data retrieval |
| RESTCONF | HTTPS | 443 | YANG-based REST API access |

## Requirements

Python 3 is required.

### Windows

Install Python using WinGet:

```cmd
winget install Python.Python.3.14
```

Check the Python version:

```cmd
python3 --version
```

Check pip:

```cmd
python3 -m pip --version
```

Install the required Python packages:

```cmd
python3 -m pip install netmiko
python3 -m pip install ncclient
python3 -m pip install requests
```

Check an installed package:

```cmd
python3 -m pip show netmiko
```

### Linux

Install Python 3:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
```

Check the Python version:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

Install the required Python packages:

```bash
python3 -m pip install netmiko
python3 -m pip install ncclient
python3 -m pip install requests
```

Check an installed package:

```bash
python3 -m pip show netmiko
```

## Project Structure

### [NETMIKO](./netmiko/)
- [netmiko.py](./netmiko/netmiko.py)
- [conf1.cfg](./netmiko/conf1.cfg)

### [NETCONF](./netconf/)
- [netconf.py](./netconf/netconf.py)
- [config1.xml](./netconf/config1.xml)

### [RESTCONF](./restconf/)
- [restconf.py](./restconf/restconf.py)
- [get_token.py](./restconf/get_token.py)

