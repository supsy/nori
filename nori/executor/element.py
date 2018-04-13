import re

class ElementExecuter(object):
    def __init__(self, config, logger, snmp_client):
        self.config = config
        self.logger = logger
        self.snmp_client = snmp_client
        self.sysobjdef = None

    def get_sysoid(self, element):
        element.set_sysoid(self.snmp_client.snmpget('1.3.6.1.2.1.1.2.0'))

        return

    def collect_system_infos(self, element):
        for param in element.get_system_paramlist():
            self.collect_param(element, param)

    def collect_param(self, element, param):
        print(param)
        if param in self.sysobjdef and self.sysobjdef[param] != None:
            search_result = re.search('(.*)\((.*)\)', self.sysobjdef[param])
            if search_result:
                action = search_result.group(1)
                if action == "snmp":
                    value = self.snmp_client.snmpget(search_result.group(2))
                    #print(value)

                func = getattr(element, 'set_' + param.lower(), None)
                if callable(func) and "value" in locals() and value != None:
                    func(value)

    def set_sysobjdef(self, sysobjdef):
        self.sysobjdef = sysobjdef