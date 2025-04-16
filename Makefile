.PHONY: bundle build clean

DESKTOP_PATH := AppDir/usr/share/applications
ICON_PATH := AppDir/usr/share/icons/hicolor/256x256/apps

all: bundle build clean

bundle:
	@echo "Bundling the application with pyinstaller..."
	pyinstaller app.spec --noconfirm --clean

build:
	@echo "Preparing the build environment..."
	rm -rf AppDir | true
	mkdir -p AppDir/usr/src
	mkdir -p $(DESKTOP_PATH)
	mkdir -p $(ICON_PATH)
	@echo "Copy the bundled application..."
	cp -r dist/* AppDir/usr/src/
	@echo "Copy the assets..."
	cp assets/com.cadquery.editor.desktop $(DESKTOP_PATH)
	cp assets/CadQuery.png $(ICON_PATH)
	@echo "Building the AppImage now..."
	appimage-builder --recipe AppImageBuilder.yml --build-dir build/

clean:
	@echo "This is the clean step"
	rm -rf dist/ build/
