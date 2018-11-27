import imp
from argparse import ArgumentParser

def main():
    if __name__ == "__main__":
        parser = ArgumentParser()
        parser.add_argument('-f', '--file', 
                type=str, 
                help="Name of Crawler file to run",
                required=True)
        args = parser.parse_args()
        if args.file:
            f = args.file
            path = "crawlers/"+f+".py"
            ff = imp.load_source(f, path)

main()

