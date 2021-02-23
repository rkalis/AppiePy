from appiepy import Product
from pprint import pprint
import json
import sys

def main():
    product = Product(sys.argv[1])
    print(json.dumps(product.__dict__, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()
