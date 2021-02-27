
filetypedict = {
    "py": ".py",
    "python": ".py",
    "pi": ".py",
    "json": ".json",
    "js": ".js",
    "javascript": ".js",
    "java": ".java",
    "Java": ".java",
    "text": ".txt",
    "txt": ".txt",
    "csv": ".csv",
    "tsv": ".tsv",
    "c++": ".cpp",
    "c": ".c",
}


def file_type(rawtype: str):
    try:
        res = filetypedict[rawtype]
    except KeyError as e:
        print(f"file Type not present in dictionary: \n {e}")
        res = ""
    return res
