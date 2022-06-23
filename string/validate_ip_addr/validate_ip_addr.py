"""validate_ip_addr.py

Given a string, return "IPV4" for valid IPV4 address, "IPV6" for valid IPV6 address, or Neither if invalid
"""
from ipaddress import ip_address, IPv6Address

class IPAddress:
    def ValidateIP(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"
