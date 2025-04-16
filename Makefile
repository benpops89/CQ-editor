.PHONY: bundle build clean

DOCKER_IMAGE := appimagecrafters/appimage-builder:1.1.0

bundle:
	@echo "Bundling the application with pyinstaller..."
	pyinstaller run.spec --noconfirm --clean

build:
	@echo "Preparing the build environment"
	./prepare.sh
	@echo "Building the AppImage now..."
	appimage-builder --recipe AppImageBuilder.yml --build-dir build/

clean:
	@echo "This is the clean step"
