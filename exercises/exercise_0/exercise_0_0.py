# 0. User input for ETL Parameters

from pathlib import Path

source_file_path= input("source directory: ")
destination_file_path = input("destination directory: ")

print(f"source: {source_file_path} {'*exists*' if Path(destination_file_path).exists() else '*does not exist*'}")
print(f"destination: {destination_file_path} {'*exists*' if Path(destination_file_path).exists() else '*does not exist*'}")
