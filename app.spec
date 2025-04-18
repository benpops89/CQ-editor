# -*- mode: python ; coding: utf-8 -*-

import importlib.util
import os

os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

# Spyder
spyder_spec = importlib.util.find_spec("spyder")
spyder_path = os.path.dirname(spyder_spec.origin)

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[
      (os.path.join(spyder_path, "fonts"), "spyder/fonts"),
      (os.path.join(spyder_path, "images"), "spyder/images"),
    ],
    hiddenimports = [
      'vtkmodules.vtkCommonCore',
      'vtkmodules.vtkCommonDataModel',
      'vtkmodules.vtkCommonExecutionModel',
      'vtkmodules.vtkCommonMath',
      'vtkmodules.vtkCommonMisc',
      'vtkmodules.vtkCommonTransforms',
      'vtkmodules.vtkFiltersCore',
      'vtkmodules.vtkFiltersExtraction',
      'vtkmodules.vtkFiltersGeneral',
      'vtkmodules.vtkIOCore',
      'vtkmodules.vtkIOExport',
      'vtkmodules.vtkIOImage',
      'vtkmodules.vtkIOXML',
      'vtkmodules.vtkIOXMLParser',
      'vtkmodules.vtkImagingCore',
      'vtkmodules.vtkRenderingContext2D',
      'vtkmodules.vtkRenderingCore',
      'vtkmodules.vtkRenderingFreeType',
      'vtkmodules.vtkRenderingSceneGraph',
      'vtkmodules.vtkRenderingVtkJS',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["debugpy"],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    
    [],
    exclude_binaries=True,
    name='CQ-editor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CQ-editor',
)
