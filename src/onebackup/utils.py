__author__ = 'junaid'

import abc
import os.path

class Utilities(object):
    """
    Abstract class for utility functions
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_home_dir(self):
        """
        Returns the home directory for the user
        """
        pass


class Win32Utilities(Utilities):
    """
    Windows Platform implementation of Utilities
    """

    def get_home_dir(self):
        """
        Returns the home directory for the user
        """
        pass

class LinuxUtilities(Utilities):
    """
    Linux Platform implementation of Utilities
    """
    def get_home_dir(self):
        """
        Returns the home directory for the user
        """
        pass