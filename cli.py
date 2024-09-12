import argparse
from db_function import *

parser = argparse.ArgumentParser(description="A python CLI for SQLite3")

parser.add_argument("database", type=str, nargs='?', help="The database you want to affect.")  # Optional argument

parser.add_argument('-c', '--create', type=str, help='Create a database with the specified name.')

parser.add_argument("-w", "--write", action="store_true", help="Write in the database.")
parser.add_argument('-r', '--read', action="store_true", help='Read all data from a column') 
parser.add_argument('-d', '--delete', type=str, help='Delete a specific value in a column')
parser.add_argument('-dT', '--delete-table', type=str, help='Delete all values in a table')
parser.add_argument('-dC', '--delete-column', type=str, help='Delete all values in a column')

args = parser.parse_args()

# Handle database creation
if args.create:
    create_db(args.create)

# Handle other operations, checking if `database` is provided and not overridden by `--create`
elif args.database:
    if args.write:
        # Implement write functionality here
        pass
    elif args.read:
        # Implement read functionality here
        pass
    elif args.delete:
        # Implement delete functionality here
        pass
    elif args.delete_table:
        # Implement delete table functionality here
        pass
    elif args.delete_column:
        # Implement delete column functionality here
        pass
    else:
        print("No operation specified.")
else:
    print("No database specified.")
