from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories

from textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        """
        Initializes the ConfigurationManager.

        Args:
            config_filepath (str, optional): Path to the configuration file. Defaults to CONFIG_FILE_PATH.
            params_filepath (str, optional): Path to the parameters file. Defaults to PARAMS_FILE_PATH.
        """
        # Load configuration and parameters from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure the existence of directories specified in the configuration
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves the data ingestion configuration.

        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        # Extract data ingestion configuration from the overall configuration
        config = self.config.data_ingestion

        # Ensure the existence of the root directory specified in the data ingestion configuration
        create_directories([config.root_dir])

        # Create and return a DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
