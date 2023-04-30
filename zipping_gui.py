import shutil
import PySimpleGUI
from zipping import make_archive

PySimpleGUI.theme("DarkGreen4")

select_files = PySimpleGUI.Text("Select files for zipping:")
input1 = PySimpleGUI.Input()
choose_button1 = PySimpleGUI.FilesBrowse("Browse", key="selected_files")

select_destinations = PySimpleGUI.Text("Select destination folder:")
input2 = PySimpleGUI.Input()
choose_button2 = PySimpleGUI.FolderBrowse("Browse", key="selected_folder")

name_file = PySimpleGUI.InputText(".zip", key="name_file")

zip_button = PySimpleGUI.Button("Zip", button_color=("white", "purple"), size=(6, 1))
message = PySimpleGUI.Text(key="message", text_color="DarkOrchid1", justification="right", font="Futura 11 bold")

layout = [[select_files, PySimpleGUI.Push(), input1, choose_button1],
          [select_destinations, input2, choose_button2],
          [PySimpleGUI.Push(), name_file, zip_button],
          [PySimpleGUI.Push(), message]]

window = PySimpleGUI.Window("File Zipper", layout=layout, default_button_element_size=(6, 1))
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
