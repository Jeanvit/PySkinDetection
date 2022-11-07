'''This is an example script for running the default library processing method'''
import sys
from src.skinDetector import SkinDetector


imageName = sys.argv[1]

detector = SkinDetector(image_path = imageName)
detector.find_skin()
detector.show_all_images()