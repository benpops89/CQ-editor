#!/bin/bash
set -e

# Create folder structure
rm -rf AppDir | true
mkdir -p AppDir/usr/src
mkdir -p AppDir/usr/share/applications
mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps

# Copy bundled application
cp -r dist/* AppDir/usr/src

# Define paths
DESKTOP_FILE="AppDir/usr/share/applications/com.cadquery.editor.desktop"
ICON_SRC="https://avatars.githubusercontent.com/u/36305429?s=200&v=4"
ICON_PATH="AppDir/usr/share/icons/hicolor/256x256/apps/CadQuery.png"

# Create the .desktop file
cat >"$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=CadQuery Editor
Exec=user/src/run/run %u
Icon=CadQuery
Terminal=false
Categories=Development;Graphics;
EOF

# Move the icon
cp icons/CadQuery.png $ICON_PATH

echo "AppDir structure created and .desktop file + icon added successfully."
