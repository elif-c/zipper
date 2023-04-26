import shutil
import PySimpleGUI
from zipping import make_archive

select_files = PySimpleGUI.Text("Select files to zip:")
input1 = PySimpleGUI.Input()
choose_button1 = PySimpleGUI.FilesBrowse("Browse", key="selected_files")

select_destinations = PySimpleGUI.Text("Select destination folder:")
input2 = PySimpleGUI.Input()
choose_button2 = PySimpleGUI.FolderBrowse("Browse", key="selected_folder")

name_file = PySimpleGUI.InputText(".zip", key="name_file")

zip_button = PySimpleGUI.Button("Zip", button_color=("white", "purple"))
message = PySimpleGUI.Text(key="message", text_color="purple")

window = PySimpleGUI.Window("File Zipper", layout=[[select_files, input1, choose_button1],
                                                   [select_destinations, input2, choose_button2],
                                                   [name_file, zip_button, message]])
while True:
    event_key, value = window.read()

    match event_key:
        case "Zip":
            filepaths = value["selected_files"].split(";")
            folder = value["selected_folder"]
            name = value["name_file"]
            if ".zip" not in name:
                name = name + ".zip"
            make_archive(filepaths, folder, name)
            window["message"].update(value="Zipping successful!")
        case PySimpleGUI.WINDOW_CLOSED:
            break


window.close()
