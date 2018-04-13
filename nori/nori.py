import logging
import os
import sys
import yaml 
import getopt

from nori.connection.snmp import Snmp
from nori.model.element import Element
from nori.executor.element import ElementExecuter
from nori.executor.interface import InterfaceExecuter

class Nori(object):
    def __init__(self):
        """Construct"""
        self.config = {"debug_level": 250, "log_file": "nori.log", "sysobjdef_folder": "sysobj", "snmp_default_port": 161}
        self.logger = None
        self.load_logger()

    def run(self):
        """Run"""
        self.get_options(sys.argv[1:])

        element = Element()
        element.set_ipaddr(self.config['ipaddr'])
        element.set_snmpcommunity_read(self.config['community'])

        snmp_client = Snmp(element.get_ipaddr(), self.config['snmp_default_port'],
                                element.get_snmpcommunity_read())
        elementexecuter = ElementExecuter(self.config, self.logger, snmp_client)
        interfaceexecuter = InterfaceExecuter(self.config, self.logger, snmp_client)

        self.logger.info("####Start run####")
        elementexecuter.get_sysoid(element)

        self.logger.debug("Found SysObj via SNMP: {}".format(element.get_sysoid()))

        sysobjdef = self.get_definition_file(element.get_sysoid())
        self.logger.debug(sysobjdef)
        elementexecuter.set_sysobjdef(sysobjdef)
        interfaceexecuter.set_sysobjdef(sysobjdef)

        if sysobjdef:
            elementexecuter.collect_system_infos(element)
            interfaceexecuter.collect_interfaces(element)

        print(element.get_bootimage())
        print(element.get_interfaces()[1].get_speed())

    def get_definition_file(self, sysoid):
        sysobjdef_filename = "{}/{}.yml".format(self.config["sysobjdef_folder"], sysoid)

        if os.path.isfile(sysobjdef_filename):
            self.logger.debug("File found")
            with open(sysobjdef_filename, "r") as sysobjdef_file:
                try:
                    sysobjdef = yaml.load(sysobjdef_file)

                    return sysobjdef
                except yaml.YAMLError as ex:
                    raise ValueError(ex) 	 
        else:
            raise Exception("Def file not found")

    def load_logger(self):
        """Load logger"""
        self.logger = logging.getLogger("script")

        if self.config["debug_level"] > 10:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(self.config["log_file"])
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(thread)d] %(name)s.%(levelname)s: %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_options(self, argv):
        """Get options"""
        required_options = ["-i", "-c"]

        try:
            opts, _ = getopt.getopt(argv, "hd:i:c:")
        except getopt.GetoptError:
            self.usage()

        for opt, arg in opts:
            if opt == "-h":
                self.usage()
            elif opt in "-i":
                self.config["ipaddr"] = arg
                required_options.remove("-i")
            elif opt in "-c":
                self.config["community"] = arg
                required_options.remove("-c")
            elif opt in "-d":
                self.config["debug_level"] = int(arg)

            else:
                self.usage()

        if len(required_options) != 0:
            print("Missing the option(s) {}".format(str(required_options)))
            self.usage()

        if self.config["debug_level"] > 10:
            print("getConfig:\n{}\n".format(str(self.config)))

    @staticmethod
    def usage():
        """Usage"""
        script_name = os.path.basename(__file__)

        print ("NORI - Network Discovery Tool \n")
        print("usage: {} [-h] [-i <ip>] [-c <community>]".format(script_name))
        print("Arguments:")
        print("\t-i\tIP Address\t\t*Required")
        print("\t-c\tCommunity\t\t*Required")
        print("")
        print("\t-d\tDebugging level")
        print("\t-h\tPrint Help (this message) and exit")
        sys.exit(2)