from sys import argv
from pathlib import Path
from pprint import pprint as pp
from inventory_parse import inventory as inv


def main():
    try:
        inv_csv_file = Path(str(argv[1]))
        inventory = inv.Inventory(inv_csv_file)

        pp(inventory.items)
        pp(inventory.certs)
        pp(inventory.item_types)

        pp(inventory.get_items_by_paint("Titanium White"))
        pp(inventory.get_items_by_cert('shotsongoal'))
        pp(inventory.get_items_by_type('player banner'))
    except FileNotFoundError:
        print(f'Error: File not found\n\t{inv_csv_file}')
        exit(1)
    except IndexError:
        print("Error: Must provide path to inventory CSV file")
        exit(1)


if __name__ ==  '__main__':
    main()
