import zipfile
import pathlib


def make_archive(filepaths, destination, name=str):
    # pathlib creates a path with the given arguments
    destination_path = pathlib.Path(destination, name)
    with zipfile.ZipFile(destination_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["converter.py", "converter_gui.py"], destination="files_2_zip")