from nori.model.interface import Interface

import re

class InterfaceExecuter(object):
    def __init__(self, config, logger, snmp_client):
        self.config = config
        self.logger = logger
        self.snmp_client = snmp_client
        self.sysobjdef = None

    def collect_interfaces(self, element):
        self._collect_ifname(element)
        self._collect_ifdesc(element)
        self._collect_ifspeed(element)


        #for param in Interface.get_interface_paramlist():
        #    if param in self.sysobjdef and self.sysobjdef[param] != None:
        #        search_result = re.search('(.*)\((.*)\)', self.sysobjdef[param])
        #        if search_result:
        #            action = search_result.group(1)
        #            if action == "snmp":
        #                walk = self.walk_snmp_oid(element, search_result.group(2))
        #                for row in walk:
        #                    for name, val in row:
        #                        print(name[11:])
        #                        print(val)
        #                #print(walk)
        #                #print("::" + value + "::")

    def set_sysobjdef(self, sysobjdef):
        self.sysobjdef = sysobjdef

    def _collect_ifname(self, element):
        interfaces = []
        for row in self._collect('IFname'):
            for oid, value in row:
                interface = Interface()
                interface.set_index(oid[11:])
                interface.set_name(value)
                interfaces.append(interface)
        element.set_interfaces(interfaces)

    def _collect_ifdesc(self, element):
        for row in self._collect('IFdesc'):
            for oid, value in row:
                interface = element.get_interface_by_index(oid[10:])
                interface.set_description(value)

    def _collect_ifspeed(self, element):
        for row in self._collect('IFspeed'):
            for oid, value in row:
                interface = element.get_interface_by_index(oid[10:])
                interface.set_speed(value)

    def _collect(self, param):
        if param in self.sysobjdef and self.sysobjdef[param] != None:
            search_result = re.search('(.*)\((.*)\)', self.sysobjdef[param])
            if search_result:
                action = search_result.group(1)
                if action == "snmp":
                    walk = self.snmp_client.snmpwalk(search_result.group(2))

                    return walk