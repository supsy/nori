"""Module Interface"""

class Interface(object):
    """ Interface model """

    def __init__(self):
        """Construct"""
        self.index = None
        self.name = None
        self.alias = None
        self.description = None
        self.speed = None

    @staticmethod
    def get_interface_paramlist():
        return ['IFdesc', 'IFname', 'IFalias']

    def set_index(self, index):
        """Set Index"""
        self.index = index

    def get_index(self):
        """Get Index"""
        return self.index

    def set_name(self, name):
        """Set Name"""
        self.name = name

    def get_name(self):
        """Get Name"""
        return self.name

    def set_alias(self, alias):
        """Set Alias"""
        self.alias = alias

    def get_alias(self):
        """Get Alias"""
        return self.alias

    def set_description(self, description):
        """Set Description"""
        self.description = description

    def get_description(self):
        """Get Description"""
        return self.description

    def set_speed(self, speed):
        """Set Speed"""
        self.speed = speed

    def get_speed(self):
        """Get Speed"""
        return self.speed