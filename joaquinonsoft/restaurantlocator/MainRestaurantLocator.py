import csv
import getopt
import sys

from joaquinonsoft.file.CSVWriter import CSVWriter
from joaquinonsoft.restaurantlocator.RodillasLocatorURLReader import RodillasLocatorURLReader
from joaquinonsoft.restaurantlocator.VIPsLocatorURLReader import VIPsLocatorURLReader


def print_help():
    print('Scrap the VIPs ans Rodilla web pages')
    print('\nExecution:')
    print('\tMainRestaurantLocator.py -o <output_file>')
    print('where:')
    print('\t-h: Print this help')
    print('\t-o: (Mandatory) output folder')


def write_csv(file_path, rows):
    print(rows)
    writer = CSVWriter(file_path, ";", csv.QUOTE_ALL)
    writer.write(rows)


def main(argv):
    output_folder = None

    try:
        opts, args = getopt.getopt(argv, "ho:", ["output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-o", "--output"):
            output_folder = arg

    if output_folder is not None:
        rodilla_locator = RodillasLocatorURLReader()
        rodillas = rodilla_locator.read()
        write_csv(output_folder + "\\rodilla.csv", rodillas)

        vips_locator = VIPsLocatorURLReader()
        vips = vips_locator.read()
        write_csv(output_folder + "\\vips.csv", rodillas)
    else:
        print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
