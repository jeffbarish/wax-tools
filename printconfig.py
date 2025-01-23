"""Print the contents of the config file."""

import argparse
import pickle
import sys
from pathlib import Path
from pprint import pprint

from common.constants import CONFIG

parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).stem,
        description='Print contents of config file.',
        epilog='With no options, print all')

parser.add_argument('-c', '--completers', action='store_true',
        help='completers')
parser.add_argument('-f', '--filter', action='store_true',
        help='filter config')
parser.add_argument('-g', '--genre', action='store_true',
        help='genre spec')
parser.add_argument('-k', '--keys', action='store_true',
        help='trackmetadata keys')
parser.add_argument('-m', '--geometry', action='store_true',
        help='geometry')
parser.add_argument('-r', '--random', action='store_true',
        help='random config')
parser.add_argument('-s', '--sort', action='store_true',
        help='sort indicators')
parser.add_argument('-u', '--user', action='store_true',
        help='user props')
parser.add_argument('-v', '--volume', action='store_true',
        help='volume')
parser.add_argument('-w', '--widths', action='store_true',
        help='column widths')

args = parser.parse_args()

with open(CONFIG, 'rb') as config_fo:
    config = pickle.load(config_fo)

if args.filter:
    print('filter config:')
    pprint(config['filter config'], indent=4, sort_dicts=False)
if args.genre:
    print('genre spec:')
    pprint(config['genre spec'], indent=4, sort_dicts=False)
if args.random:
    print('random config:')
    pprint(config['random config'], indent=4, sort_dicts=False)
if args.sort:
    print('sort indicators:')
    pprint(config['sort indicators'], indent=4, sort_dicts=False)
if args.user:
    print('user props:')
    pprint(config['user props'], indent=4, sort_dicts=False)
if args.widths:
    print('column widths:')
    pprint(config['column widths'], indent=4, sort_dicts=False)
if args.completers:
    print('completers:')
    pprint(config['completers'], indent=4, sort_dicts=False)
if args.geometry:
    print('geometry:')
    pprint(config['geometry'], indent=4, sort_dicts=False)
if args.keys:
    print('trackmetadata keys:')
    pprint(config['trackmetadata keys'], indent=4, sort_dicts=False)
if args.volume:
    print(f'volume: {config["volume"]}')
if not any(vars(args).values()):
    pprint(config, indent=4, sort_dicts=False)

