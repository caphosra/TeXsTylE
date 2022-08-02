#!/bin/python3

import os
import glob
import re
import shutil
import subprocess

#
# Visit all style files in this project.
#
for path in glob.glob("./*.sty"):
    print(f"Processing {path}...")

    #
    # Get all commands defined in the file.
    #
    with open(path, "r") as fs:
        style = fs.read()
        commands = re.findall("%\s#def\s(.+)", style)

    #
    # Copy the file to a temporary directory.
    #
    if not os.path.exists("./tmp"):
        os.makedirs("./tmp")
    filename = os.path.basename(path)
    shutil.copy(path, f"./tmp/{filename}")

    #
    # Generate a .cwl file.
    #
    file_without_ext = os.path.splitext(filename)[0]
    cwl_file_path = f"./tmp/{file_without_ext}.cwl"
    with open(cwl_file_path, "w") as fs:
        for command in commands:
            fs.write(f"{command}\n")

    #
    # Call `pkgcommand.py` to compile a .cwl file.
    #
    if not os.path.exists("./dist"):
        os.makedirs("./dist")
    subprocess.run([
        "python3",
        "./workshop/dev/pkgcommand.py",
        "-i",
        cwl_file_path,
        "-o",
        "./dist"
    ])

print("Done (๑>◡<๑)")
