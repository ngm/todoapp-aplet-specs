import xml.etree.ElementTree as et
from os import listdir, path, makedirs
import argparse
import pprint
import sys

arg_parser = argparse.ArgumentParser(description='Draw dot file from FeatureIDE model.xml')
arg_parser.add_argument('reports_dir', help="Location of the test results files for products")
arg_parser.add_argument('productname', help="")

args = arg_parser.parse_args()

# Parse tests results
# For all product reports, go through results
# If there's a failure in any product for a given feature, that's a failure for the PL.
file_path = path.join(args.reports_dir, "report" + args.productname + ".xml")
tree = et.parse(file_path)
root = tree.getroot()
acceptance_suite = root.find('testsuite')

passed = True
for testcase in acceptance_suite:
    if testcase.find("failure") is not None:
        passed = False

if passed is True:
    sys.exit(0)

sys.exit(1)
