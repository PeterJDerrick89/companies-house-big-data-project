from os import listdir
from os.path import isfile, join
import time
import argparse
import sys
import cv2
import configparser

config = configparser.ConfigParser()
config.read("cha_pipeline.cfg")

xbrl_web_scraper = config.get('cha_workflow', 'xbrl_web_scraper')
xbrl_functions = config.get('cha_workflow', 'xbrl_functions')
pdf_web_scraper = config.get('cha_workflow', 'pdf_web_scraper')
pdfs_to_images = config.get('cha_workflow', 'pdfs_to_images')
train_classifier_model = config.get('cha_workflow', 'train_classifier_model')
binary_classifier = config.get('cha_workflow', 'binary_classifier')
ocr_functions = config.get('cha_workflow', 'ocr_functions')
nlp_functions = config.get('cha_workflow', 'nlp_functions')
merge_xbrl_to_pdf_data = config.get('cha_workflow', 'merge_xbrl_to_pdf_data')

from src.data_processing.cst_data_processing import DataProcessing
from src.classifier.cst_classifier import Classifier


def main():

    print("-"*50)

    # Execute module xbrl_web_scraper
    if xbrl_web_scraper == str(True):
        print("XBRL web scraper running...")

    # Run all xbrl related functions in order
    if xbrl_functions == str(True):
        print("Running all XBRL functions...")

    # Execute PDF web scraper
    if pdf_web_scraper == str(True):
        print("PDF web scraper running...")

    # Convert PDF files to images
    if pdfs_to_images == str(True):
        print("Converting all PDFs to images...")

    # Train the Classifier model
    if train_classifier_model == str(True):
        print("Training classifier model...")

    # Execute binary Classifier
    if binary_classifier == str(True):
        print("Executing binary classifier...")

    # Execute OCR
    if ocr_functions == str(True):
        print("Running all OCR functions...")

    # Execute NLP
    if nlp_functions == str(True):
        print("Running all NLP functions...")

    # Merge xbrl and PDF file data
    if merge_xbrl_to_pdf_data == str(True):
        print("Merging XBRL and PDF data...")


    """
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--input_imgs", required = True,
        help = "path to a directory containing images to be used as input data")
    ap.add_argument("-c", "--cascade_file", required = True,
        help = "path to cascade classifier.")
    ap.add_argument("-s", "--scale_factor", required = True,
        help = "cascade classifier scale factor.")
    ap.add_argument("-m", "--min_neighbors", required = True,
        help = "cascade classifier min neighbors.")
    ap.add_argument("-x", "--cascade_width", required = True,
        help = "cascade classifier starting sample width.")
    ap.add_argument("-y", "--cascade_height", required = True,
        help = "cascade classifier starting sample height.")
    ap.add_argument("-o", "--classifier_output_dir", required = True,
        help = "path to classifier output.")
    ap.add_argument("-p", "--processed_images_dir", required = True,
        help = "path to images processed by the classifier.")
    ap.add_argument("-v", "--show_classifier_output", required = False,
        help = "display the output of the classifier to the user.")
    args = vars(ap.parse_args())

    detector = cv2.CascadeClassifier(args["cascade_file"])

    # load the input image and convert it to grayscale
    for image in listdir(args["input_imgs"]):
        img = Classifier.classifier_input(join(args["input_imgs"], image))
        grey = Classifier.imgs_to_grey(img)

        rects = Classifier.ensemble(detector,
                           grey,
                           float(args["scale_factor"]),
                           int(args["min_neighbors"]),
                           int(args["cascade_width"]),
                           int(args["cascade_height"]))

        print("\n[INFO] Found " + str(Classifier.count_classifier_output(rects)) + " companies house stamps.")

        Classifier.classifier_output(rects, img, args["classifier_output_dir"])

        Classifier.classifier_process(img, join(args["processed_images_dir"], image))

        if args["show_classifier_output"] == "True": 
            Classifier.display_classifier_output(image, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            pass
    """


if __name__ == "__main__":
    process_start = time.time()

    main()

    print("-" * 50)
    print("Process Complete")
    print("The time taken to process an image is: ", "{}".format((time.time() - process_start) / 60, 2), " minutes")
