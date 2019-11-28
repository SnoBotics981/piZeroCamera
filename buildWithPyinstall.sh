#!/bin/sh

pyinstaller --onefile --clean basic3-ex13-lastSample.py
pyinstaller --onefile --clean captureImages.py
pyinstaller --onefile --clean continuousExample01.py
pyinstaller --onefile --clean continuousExample02.py
pyinstaller --onefile --clean grabbingVideoStreamFromOrionTelescopeCamera.py
pyinstaller --onefile --clean grabbingVideoStreamFromRaspberryPiCamera.py
pyinstaller --onefile --clean grabbingVideoStreamFromUsbId.py
pyinstaller --onefile --clean liveVideo.py
pyinstaller --onefile --clean raspberryPiCameraMovieExample01.py
pyinstaller --onefile --clean raspberryPiCameraMovieExampleProcessingImages01.py
pyinstaller --onefile --clean raspberryPiCameraStillImagesStreamForProcessing.py
pyinstaller --onefile --clean webcam-cv2.py
