"""
Author: Nolan McDonald
Purpose: Say hello to user
"""
import argparse


def get_args():
    """ Get CMD args """
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """ main """
    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == "__main__":
    main()
