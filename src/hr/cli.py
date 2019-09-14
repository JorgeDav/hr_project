from argparse import ArgumentParser
from hr import parse_json, users
def create_parser():
    parser=ArgumentParser(description="Manage users on a server using a JSON file")
    parser.add_argument('path',  help="Path of the JSON file to manage the users")
    parser.add_argument('--export', action='store_true', help="Export current settings to inventory file")
    return parser

def main():
    args=create_parser().parse_args()
    if args.export==False:
        user_info=parse_json.load(args.path)
        users.check_users(user_info)

    elif args.export==True:
        parse_json.dump(args.path)
