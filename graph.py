import argparse
import csv
import sys

from person import Person
from genealogy import Genealogy

from PrettyPrint import PrettyPrintTree

def parse_genealogy(source_file):
    persons = []
    with open(source_file, encoding='utf-8-sig') as source_file_csv:
        source_csv_reader = csv.DictReader(source_file_csv)
        for row in source_csv_reader:
            person = Person(id=row['Id'], 
                            name=row['Name'],
                            parent1_id=row['Parent1'],
                            parent2_id=row['Parent2'],
                            birthdate=row['Birthdate'])
            persons.append(person)
    genealogy = Genealogy(persons=persons)
    return genealogy


def graph_pretty(genealogy, max_depth = None, limit_parent = None):
    root = genealogy.get_persons()[0]

    def get_parent(person):
        filtered_parents = []
        parents = person.get_resolved_parents()
        for i in range(0, len(parents)):
            parent = parents[i]
            if not parent:
                continue
            elif not limit_parent or (limit_parent-1) == i:
                filtered_parents.append(parent)
        return filtered_parents
    
    def get_display(person):
        return person.get_display()

    pt = PrettyPrintTree(
        get_children=lambda p: get_parent(p), 
        get_val=lambda p: get_display(p),
        max_depth=max_depth,
        orientation=False)
    pt(root)


def main():

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--source', help='Path to source csv file', required=True)
    arg_parser.add_argument('--out', help='Out path', required=False)
    arg_parser.add_argument('--max_depth', help='Max ancestry depth to write', required=False, type=int)
    arg_parser.add_argument('--limit_parent', help='1 or 2 depending on which parent', type=int)
    args = arg_parser.parse_args()

    if args.out:
        sys.stdout = open(args.out, 'w', encoding='utf-8-sig')

    genealogy = parse_genealogy(args.source)
    
    # graph(genealogy)
    graph_pretty(
        genealogy=genealogy,
        max_depth=args.max_depth,
        limit_parent=args.limit_parent)


if __name__ == '__main__':
    main()