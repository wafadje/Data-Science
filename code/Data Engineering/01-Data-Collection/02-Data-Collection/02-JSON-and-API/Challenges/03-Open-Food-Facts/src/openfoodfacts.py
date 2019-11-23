"""
The Open Food Facts API url is https://world.openfoodfacts.org/api/v0/product/[barcode].json for a given [barcode].

    Write a function get_description(barcode) to retrieve the description of any given repository.
    Write a function save_description(description) storing a given description in a barcode.json file located in the output folder
    Write a function shorten(description) returning only the following informations for a given product : bar code, product name, brand, nutrition grade, nutrient level tags, additives.
    Create a class Food and populate it with the products in input/barcodes.csv. The attributes should correspond to the fields in shorten(description). Save your instances in a binary file products.bin.
    Serialize your instances in a products.csv file with a proper header
    Sort all the products in input/barcodes.csv by decreasing nutrition grade and write the result in a sorted_products file.

Your code must be written in src/openfoodfacts.py.
"""

def main():
    pass

if __name__ == "__main__":
    main()
