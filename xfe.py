import logging
import ConfigManager


class Xfe(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.INFO)

        self.logger.info('Initializing XFE')
        self.xfe_config = ConfigManager.ConfigManager()
        self.logger.debug('API key: %s', self.xfe_config.get_api_key())
        self.logger.debug('API pass: %s', self.xfe_config.get_api_pass())
        #self.logger.info('API USER: %s', self.xfe_config.xfe.api_key)


def main():
    xfe_test = Xfe()


if __name__ == "__main__":
    main()
