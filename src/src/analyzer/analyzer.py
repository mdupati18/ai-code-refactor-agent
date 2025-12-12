import json
from utils.file_utils import read_file

class CodeAnalyzer:
    def __init__(self, config):
        self.config = config

    def analyze(self, file_path):
        content = read_file(file_path)
        return {
            "file": file_path,
            "length": len(content.splitlines()),
            "issues": [
                "Possible long function bodies",
                "Check unused imports",
                "Check naming consistency"
            ]
        }
