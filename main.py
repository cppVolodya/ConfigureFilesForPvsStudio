from scripts import *


def main():
    arguments_parser = ArgumentsParser()
    arguments_parser.Start()

    arguments_handler = ArgumentsHandler(arguments_parser.GetArgs())
    arguments_handler.Start()


if __name__ == "__main__":
    main()
