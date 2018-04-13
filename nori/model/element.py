"""Module Element"""

class Element(object):
    """ Element model """

    def __init__(self):
        """Construct"""
        self.ipaddr = None
        self.sysoid = None
        self.snmpcommunity_read = None
        self.sn = None
        self.hostname = None
        self.bootimage = None
        self.config_change = None
        self.config_write = None
        self.interfaces = []

    @staticmethod
    def get_system_paramlist():
        return ['Serial', 'Bootimage', 'CfgChg', 'CfgWrt']

    def set_ipaddr(self, ipaddr):
        """Set IP address"""
        self.ipaddr = ipaddr

    def get_ipaddr(self):
        """Get IP address"""
        return self.ipaddr

    def set_sysoid(self, sysoid):
        """Set SysOid"""
        self.sysoid = sysoid

    def get_sysoid(self):
        """Get SysOid"""
        return self.sysoid

    def set_snmpcommunity_read(self, snmpcommunity_read):
        """Set SNMP Community Read"""
        self.snmpcommunity_read = snmpcommunity_read

    def get_snmpcommunity_read(self):
        """Get SNMP Community Read"""
        return self.snmpcommunity_read

    def set_sn(self, sn):
        """Set Serial Number"""
        self.sn = sn

    def get_sn(self):
        """Get Serial Number"""
        return self.sn

    def set_hostname(self, hostname):
        """Set Hostname"""
        self.hostname = hostname

    def get_hostname(self):
        """Get Hostname"""
        return self.hostname

    def set_bootimage(self, bootimage):
        """Set Bootimage"""
        self.bootimage = bootimage

    def get_bootimage(self):
        """Get Bootimage"""
        return self.bootimage

    def set_interfaces(self, interfaces):
        """Set Interfaces"""
        self.interfaces = interfaces

    def get_interfaces(self):
        """Get Interfaces"""
        return self.interfaces

    def get_interface_by_index(self, index):
        """Get Interface by Index"""
        for interface in self.interfaces:

            if interface.get_index() == index:
                return interface

    def get_interface_by_name(self, name):
        """Get Interface by Name"""
        for interface in self.interfaces:
            if interface.get_name() == name:
                return interface

    #def __str__(self):
    #    return self.get_ipaddr()
