class DataParser:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def parseDataAsList(self) -> list:
        if self.file_name == "" or None:
            raise FileNotFoundError("File does not exist")

        with open(self.file_name, mode='r') as file:
            data = [i for i in file.read().strip().split('\n')]
        return data
