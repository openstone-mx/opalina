import os


version_filename = "version"
version_filepath = os.path.join(
    os.path.dirname(__file__),
    version_filename,
)

with open(version_filepath, "r") as file:
    version = file.read().strip()
