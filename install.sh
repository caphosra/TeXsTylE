#!/bin/bash

#
# Get TEXMFHOME
#
TEXMFHOME=$(kpsewhich -var-value=TEXMFHOME)
TEXMFHOME_RES=$?
if [ $TEXMFHOME_RES != 0 ]; then
    echo "Failed to get TEXMFHOME"
    exit $TEXMFHOME_RES
fi

#
# Get a directory to install the style files.
#
INSTALL_DIR="$TEXMFHOME/tex/latex/commonstuff/"
echo "Let me copy the files to $INSTALL_DIR"

#
# Copy the files to the directory
# If files already exist, it will overwrite them.
#
for file in ./*.sty; do
    yes | cp -rf $file $INSTALL_DIR
    echo "Copied $file"
done

echo "Done (๑>◡<๑)"
