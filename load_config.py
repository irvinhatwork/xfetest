import hydra
from omegaconf import DictConfig

@hydra.main(config_path = "config/config.yaml")
def load_config(cfg: DictConfig) -> None:
    print(cfg.pretty())
    
if __name__ == "__main__":
    load_config()

# def read_config()
