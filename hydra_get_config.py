import hydra
from omegaconf import DictConfig
import logging



@hydra.main(config_path="config/config.yaml")
def hydra_get_config(cfg : DictConfig):
    # print(cfg.pretty())
    logging.basicConfig(level=logging.INFO)
    hydra_log = logging.getLogger(__name__)
    hydra_log.setLevel(logging.INFO)
    hydra_log.info(cfg.pretty())
    hydra_log.info('TYPE: %s', type(cfg))
    hydra_log.info('key: %s', cfg.xfe.api_key)
    xfe_api_key = cfg.xfe.api_key
    hydra_log.info('pass: %s', cfg.xfe.api_pass)
    xfe_api_pass = cfg.xfe.api_pass
    return cfg
    #return cfg.xfe.api_key
    #return xfe_api_key

# @hydra.main(config_path="config/config.yaml")
# def hydra_get_config(cfg : DictConfig) -> None:
#     print(cfg.pretty())