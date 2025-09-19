import json
from gendiff.scripts.gendiff import make_parser

def read_json(file):
    with open(file) as f:
        return json.load(f)
    
def main():
    parser = make_parser()
    args = parser.parse_args()

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)

    return data1, data2

if __name__ == "__main__":
    main()