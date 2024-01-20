from dataclasses import dataclass # Define return type of a function
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion.

    Attributes:
        root_dir (Path): Root directory where data will be stored.
        source_URL (str): URL from which data will be fetched.
        local_data_file (Path): Local path where the data file will be saved.
        unzip_dir (Path): Directory where the data file will be extracted.
    """

    root_dir: Path  # Root directory where data will be stored
    source_URL: str  # URL from which data will be fetched
    local_data_file: Path  # Local path where the data file will be saved
    unzip_dir: Path  # Directory where the data file will be extracted
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path