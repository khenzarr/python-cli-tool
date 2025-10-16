import argparse; p=argparse.ArgumentParser(); p.add_argument("text",nargs="+"); args=p.parse_args(); print(args.text)
