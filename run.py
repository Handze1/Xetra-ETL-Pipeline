"""Running the xetra ETL application"""
import logging
import logging.config

import yaml

def main():
    """
    entry point to run the xetra etl job
    """

    # Parsing yaml file
    config_path = "C:/Users/Alex/xetra_project/Xetra-ETL-Pipeline/configs/xetra_report1_config.yml"
    config = yaml.safe_load(open(config_path))
    # Configure Logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()