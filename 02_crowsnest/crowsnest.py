"""
Author : KNolan McDonald
Purpose: Print a sentence with arg word
"""

import argparse


def get_args():
    """ Get CMD Line args """
    parser = argparse.ArgumentParser(
        description="Choose the article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("word", metavar="word", help="The thing we see")
    return parser.parse_args()


def main():
    """ main """

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in "aeiou" else 'a'
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


if __name__ == "__main__":
    main()
