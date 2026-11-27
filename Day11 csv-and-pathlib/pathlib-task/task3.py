from pathlib import Path

file=Path("data/raw_data.txt")

absolute_path=file.resolve()

print("Relative Path:",file)
print("Absolute Path:",absolute_path)