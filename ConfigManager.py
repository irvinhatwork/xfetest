# import hydra
# from omegaconf import DictConfig
from omegaconf import OmegaConf
import logging
import hydra_get_config

class ConfigManager(object):

    def __init__(self):
        # Configure Logging
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.logger.info('Initializing Config Manager.')
        # self.local_config = self.load_config()
        self.config = OmegaConf.load("config/config.yaml")
        self.logger.debug('self.local_config - TYPE: %s', type(self.config))

        self.api_key = self.config['xfe']['api_key']
        self.logger.debug('API key: %s', self.api_key)
        self.api_pass = self.config['xfe']['api_pass']
        self.logger.debug('API pass: %s', self.api_pass)

    def load_config(self):
        my_config = hydra_get_config.hydra_get_config()
        self.logger.info('TYPE: %s', type(my_config))
        return my_config

    def get_api_key(self):
        return self.api_key

    def get_api_pass(self):
        return self.api_pass

    # @hydra.main(config_path="config/config.yaml")
    # def load_config_hydra(self, cfg: DictConfig) -> None:
    #     print(cfg.pretty())
    
# if __name__ == "__main__":
#     load_config()

# def read_config()
