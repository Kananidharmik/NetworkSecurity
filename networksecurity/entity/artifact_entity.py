from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trainde_file_path:str
    test_file_path:str