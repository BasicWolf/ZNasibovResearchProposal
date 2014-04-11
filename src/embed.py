#!/usr/bin/env python3

import argparse


def main():
    args = parse_args()
    print(args)
    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password', help='password')

    cmd_parsers = parser.add_subparsers(help='A command to execute')
    parser_embed = cmd_parsers.add_parser(
        'embed', help='Decrypt and embed data to a LaTeX file(s)')
    parser_clear = cmd_parsers.add_parser(
        'clear', help='Clear embedded data from a LaTeX file(s)')
    parser_encrypt = cmd_parsers.add_parser(
        'encrypt', help='Extract and encrypt the data from a LaTeX file(s)')

    return parser.parse_args()


def run_commands(command):
    pass


if __name__ == '__main__':
    main()
