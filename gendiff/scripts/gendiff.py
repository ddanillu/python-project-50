import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()

if __name__ == '__main__':
    main()