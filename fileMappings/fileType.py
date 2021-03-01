class FileType():
    def __init__(self):
        # super().__init__()
        self.file_type_predict = {
            "py": ".py",
            "python": ".py",
            "pi": ".py",
            "json": ".json",
            "js": ".js",
            "javascript": ".js",
            "java": ".java",
            "text": ".txt",
            "txt": ".txt",
            "csv": ".csv",
            "tsv": ".tsv",
            "c++": ".cpp",
            "c": ".c",
        }

    def get_file_type(self) -> dict:
        return self.file_type_predict

    def file_type(self, rawtype: str) -> str:
        try:
            res = self.get_file_type()[rawtype]
        except KeyError as e:
            print(f"file Type not present in dictionary: \n {e}")
            res = ""
        return res
