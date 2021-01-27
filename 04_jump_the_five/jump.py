import argparse


def get_args():
    parser = argparse.ArgumentParser(description = 'jump the five', formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number', help='the number used to jumo 5 from', metavar='number')
    return parser.parse_args()


def main():
    args = get_args()
    number = args.number
    nums={'0':'5', '1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '9':'1', '8':'2', '7':'3', '6':'4'}
    
    """one solution"""
    # print_string = ''
    # for char in number:
    #     print_string += nums.get(char, char)
    # print(print_string)

    """one liner"""
    print(number.translate(str.maketrans(nums)))

    """another solution"""
    #print_string = [nums.get(char, char) for char in number]
    #print(''.join(print_string))


if __name__ == '__main__':
    main()
