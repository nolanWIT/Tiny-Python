import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="picnic items",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "items", help="items we are bringing", metavar="food", nargs="+"
    )
    parser.add_argument(
        "-s", "--sorted", help="whether to sort the items", action="store_true"
    )

    return parser.parse_args()


def main():
    args = get_args()
    items = args.items
    sorted = args.sorted

    num_items = len(items)
    if sorted:
        items.sort()

    bringing = ''
    if num_items == 1:
        bringing = items[0]
    elif num_items == 2:
        bringing = ' and '.join(items)
    else:
        #items[-1] = f'and {items[-1]}.'
        #bringing = ', '.join(items)
        bringing = ', '.join(items[:-1]) + f', and {items[-1]}'
    print(f'You are bringing {bringing}.')
if __name__ == "__main__":
    main()