import csv
import getopt
import sys

from joaquinonsoft.file.CSVReader import CSVReader
from joaquinonsoft.file.CSVWriter import CSVWriter
from joaquinonsoft.restaurantlocator.CentersToRestaurantDistanceCalculator import CentersToRestaurantDistanceCalculator


def print_help():
    print('Calculate the distance of each center to the nearest restaurant')
    print('\nExecution:')
    print('\tMainDistanceCalculator.py -r <rodilla csv> -v <vips csv> -c <centers csv> -o <output_file>')
    print('where:')
    print('\t-h: Print this help')
    print('\t-r: (Mandatory) Rodilla\'s restaurants (CSV file)')
    print('\t-v: (Mandatory) VIPs restaurants (CSV file)')
    print('\t-c: (Mandatory) Center\'s list (CSV file with Schools, High schools)')
    print('\t-o: (Mandatory) Output file')


def main(argv):
    center_csv = None
    rodilla_csv = None
    vips_csv = None
    output = None

    try:
        opts, args = getopt.getopt(argv, "hc:r:v:o:", ["center=", "rodilla=", "vips=", "output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-c", "--center"):
            center_csv = arg
        elif opt in ("-r", "--rodilla"):
            rodilla_csv = arg
        elif opt in ("-v", "--vips"):
            vips_csv = arg
        elif opt in ("-o", "--output"):
            output = arg

    if center_csv is not None and rodilla_csv is not None and vips_csv is not None:
        rodillas_reader = CSVReader(rodilla_csv, ";", csv.QUOTE_ALL)
        rodillas = rodillas_reader.read()

        vips_reader = CSVReader(vips_csv, ";", csv.QUOTE_ALL)
        vips = vips_reader.read()

        centers_reader = CSVReader(center_csv, ";", csv.QUOTE_ALL)
        centers = centers_reader.read()

        restaurants = rodillas + vips
        calculator = CentersToRestaurantDistanceCalculator(centers, restaurants)
        centers = calculator.calculate()

        if centers is not None and len(centers):
            writer = CSVWriter(output, ";", csv.QUOTE_ALL)
            writer.write(centers)
    else:
        print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
