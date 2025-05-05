from core.parser import *
from core.run import *



def main():
    args = parse_arguments()
    run_simulation(args)

if __name__ == "__main__":
    main()
