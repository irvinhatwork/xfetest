import hydra
from omegaconf import DictConfig
import logging
import hydra_get_config

class ConfigManager(object):

    def __init__(self):
        # Configure Logging
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        # self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.logger.info('Initializing Config Manager.')
        self.local_config = self.load_config()
        # self.api_user = self.local_config.get_full_key('api_key')
        # self.api_pass =

    def load_config(self):
        my_config = hydra_get_config.hydra_get_config()
        self.logger.info('TYPE: %s', type(my_config))
        return my_config

    # @hydra.main(config_path="config/config.yaml")
    # def load_config_hydra(self, cfg: DictConfig) -> None:
    #     print(cfg.pretty())
    
# if __name__ == "__main__":
#     load_config()

# def read_config()
