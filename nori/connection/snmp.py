from pysnmp.entity.rfc3413.oneliner import cmdgen

class Snmp(object):
    def __init__(self, host, port=161, community='public'):
        self.host = host
        self.port = port
        self.community = community

    def snmpget(self, oid):
        cmdGen = cmdgen.CommandGenerator()

        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
          cmdgen.CommunityData(self.community),
          cmdgen.UdpTransportTarget((self.host, self.port)),
          oid
        )

        # Check for errors and print out results
        if errorIndication:
          print(errorIndication)
        else:
          if errorStatus:
            print('%s at %s' % (
              errorStatus.prettyPrint(),
              errorIndex and varBinds[int(errorIndex)-1] or '?'
              )
            )
          else:
            for name, val in varBinds:
              #print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
              return val

    def snmpwalk(self, oid):
        cmdGen = cmdgen.CommandGenerator()

        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(self.community),
            cmdgen.UdpTransportTarget((self.host, self.port)),
            0, 25,
            oid
        )

        if errorIndication:
            print(errorIndication)
        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?'
                )
                      )
            else:
                return varBindTable
                #for varBindTableRow in varBindTable:
                    #for name, val in varBindTableRow:
                    #    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))