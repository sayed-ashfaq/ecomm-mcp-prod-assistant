import importlib.metadata

packages= [
    "langchain",
    "python-dotenv",
    "langchain_core"
]

for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}: {version}")
    except:
        