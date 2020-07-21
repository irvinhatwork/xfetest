import logging
import ConfigManager


class Xfe(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.xfe_config = ConfigManager()


def main(parameter_list):
        xfe_test = Xfe()