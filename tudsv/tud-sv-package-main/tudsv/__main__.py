""" The main script containing general functions and the entry points """
import os
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from tkinter import Tk
from tkinter.filedialog import askdirectory


import tudthemes

""" 
On Windows, we need to fix the DPI awareness to avoid blurry text in 
GUI windows
"""
if os.name == 'nt':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

""" 
This is necessary to avoid a root window showing up when opening a 
dialog
"""
root = Tk()
root.withdraw()


def generate_submission_list():
    """
    Generates a list of files required for submission
    :return A list of strings containing the full path to each required file
    """
    root_dir = get_notebook_dir()
    file_list = []
    for folder, _, files in os.walk(root_dir):
        if is_folder_included(folder):
            # All files in this folder are required for submission
            for file in files:
                file_list.append(str(Path(folder) / file))
    return file_list


def get_notebook_dir():
    """
    Returns a string containing the path to the notebook directory
    """
    pkg_root = Path(os.path.dirname(__file__))
    return str(pkg_root / Path('notebooks'))


def get_output_directory():
    """
    Lets the user choose an output directory and returns it.
    """
    print("Opening a dialog to let you choose the output folder...", end="")
    path = askdirectory(title='Select a folder to store the submission '
                              'files')
    if not path:
        print("...user canceled.")
        raise NotADirectoryError
    else:
        print("...folder selected.")
    return path


def get_user_data():
    """
    Prompts the user to enter their name and matriculation number
    :return The user name and matriculation number
    """
    first_name = input("Please enter your First Name: ")
    last_name = input("Please enter your Last Name: ")
    matriculation_number = input("Please enter your matriculation number: ")
    while not validate_matriculation_number(matriculation_number):
        matriculation_number = input("Matriculation number invalid. Please "
                                     "enter a valid matriculation number (7 "
                                     "digits): ")

    return first_name, last_name, matriculation_number


def is_folder_included(folder):
    """
    Checks if a folder should be included in the submission.
    """
    return (Path(folder) / '.include_in_submission').exists()


def package_notebooks(filename: str):
    """
    Packages all notebooks into a zip file
    """
    print("Collecting all required files into a ZIP archive...", end="")
    files_to_submit = generate_submission_list()
    with ZipFile(filename + '.zip', mode='w',
                 compression=ZIP_DEFLATED, compresslevel=5) as zf:
        for file in files_to_submit:
            # The name of the file in the archive should start at the
            # notebook root folder
            arc_name = file.replace(get_notebook_dir(), "")
            zf.write(file, arcname=arc_name)
    print("...done.")


def prepare_submission():
    """
    Prepares the submission of the lab by packaging the notebooks into a zip
    file and naming it with the users name and matriculation number.
    """
    print("***\nWelcome to the submission preparation.\n***\nThe following "
          "steps "
          "will "
          "produce a ZIP archive containing all the files required "
          "for submitting a completed lab.")

    print("*** Step 1 ***")
    first_name, last_name, mat_num = get_user_data()
    filename = f"{first_name}-{last_name}-{mat_num}"

    try:
        print("*** Step 2 ***")
        filename = Path(get_output_directory()) / Path(filename)

        print("*** Step 3 ***")
        package_notebooks(str(filename))

    except NotADirectoryError:
        print("Submission preparation canceled. Abort.")

    print("***")
    print(f"Submission preparation successful. Please submit the file "
          f"{filename}.zip to your lab supervisor.")


def start_jupyter_server():
    """
    Start a Jupyter server with notebook theming
    """
    notebook_dir = get_notebook_dir()
    tudthemes.start_notebook(theme_select='bright', notebook_dir=notebook_dir)


def validate_matriculation_number(mat_num: str):
    """
    Validates a matriculation number contained in a string
    :param mat_num: A string containing the matriculation number
    :return: True: Matriculation number is valid. False: Matriculation
    number is invalid.
    """

    # Check if input is an integer number
    try:
        mat_num = int(mat_num)
    except ValueError:
        return False

    # Check if number is in allowed range (must be seven digits)
    return 10_00_00_0 <= mat_num <= 99_99_99_9


if __name__ == '__main__':
    # start_jupyter_server()
    prepare_submission()
