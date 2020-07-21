import hydra
from omegaconf import DictConfig

Class ConfigManager(object):

def __init__(self):
    # Configure Logging
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.WARNING)
    self.logger = logging.getLogger(__name__)
    # self.logger.setLevel(logging.INFO)
    self.logger.setLevel(logging.DEBUG)
    # self.logger.setLevel(logging.WARNING)

@hydra.main(config_path = "config/config.yaml")
def load_config(cfg: DictConfig) -> None:
    print(cfg.pretty())
    
# if __name__ == "__main__":
#     load_config()

# def read_config()
