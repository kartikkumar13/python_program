import argparse
import sys


def cal(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "something went wrong"


parser = argparse.ArgumentParser()

parser.add_argument('--x', type=int, default=0, help='first value')

parser.add_argument('--y', type=int, default=0, help='second value')

parser.add_argument('--o', type=str, default='add', help='operation')

args = parser.parse_args()

sys.stdout.write(str(cal(args)))
