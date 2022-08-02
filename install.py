#!/bin/python3

import os
import subprocess
import sys
import shutil
import glob

#
# Get TEXMFHOME.
#
kpsewhich_proc = subprocess.run(
    ["kpsewhich", "-var-value=TEXMFHOME"],
    capture_output=True
)
if kpsewhich_proc.returncode:
    print("Failed to get TEXMFHOME (๑> <๑)", file=sys.stderr)
    os.exit(kpsewhich_proc.returncode)
TEX_MF_HOME = kpsewhich_proc.stdout.decode("utf8")[:-1]

#
# Get a directory to install the style files.
#
INSTALL_DIR = f"{TEX_MF_HOME}/tex/latex/commonstuff/"
print(f"Installing files to {INSTALL_DIR} (๑`◡ˊ๑)و")

#
# Copy the files to the directory.
# If files already exist, it will overwrite them.
#
for file in glob.glob("./*.sty"):
    filename = os.path.basename(file)
    shutil.copy(file, f"{INSTALL_DIR}/{filename}")

    print(f"Copied {filename}")

print("Done (๑>◡<๑)")
