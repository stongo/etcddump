from . import operations
import argparse

def main(**kw):
    parser = argparse.ArgumentParser(**kw)
    parser.add_argument('--file', default=None, help='File where the dump is located')
    parser.add_argument('--preserve-indexes',
                        dest='preserve_indexes',
                        action='store_true',
                        help='Try to keep the same indexes as before.'
    )
    parser.add_argument('--watch',
                        dest='watch',
                        action='store',
                        help='Specify a path to watch.',
    )

    parser.add_argument('action', help='What to do: watch, dump or restore')
    parser.add_argument('host', default='http://localhost:4001', help='full url of the etcd host to act upon', nargs='?')
    args = parser.parse_args()

    if args.action == 'dump' and args.watch == None:
        cl = operations.Dumper(url=args.host)
        cl.dump(filename=args.file)
    elif args.action == 'dump' and args.watch != None and len(args.watch) > 0:
        print 'WATCHING: ' + args.watch
        cl = operations.Watcher(url=args.host)
        cl.watch(watch_path=args.watch, filename=args.file, )
    elif args.action == 'restore':
        cl = operations.Restorer(url=args.host)
        cl.restore(filename=args.file, preserve_indexes=args.preserve_indexes)
