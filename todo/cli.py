"""Command line interface. Run with:  python3 -m todo <command>"""
import argparse
import sys

from . import core


def build_parser():
    parser = argparse.ArgumentParser(prog="todo", description="A tiny to-do app")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Add a task")
    add.add_argument("title")

    sub.add_parser("list", help="Show all tasks")

    done = sub.add_parser("done", help="Mark a task as done")
    done.add_argument("id", type=int)

    rm = sub.add_parser("remove", help="Delete a task")
    rm.add_argument("id", type=int)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    tasks = core.load_tasks()

    try:
        if args.command == "add":
            task = core.add_task(tasks, args.title)
            print(f"Added #{task['id']}: {task['title']}")
        elif args.command == "list":
            if not tasks:
                print("No tasks yet. Add one with: python3 -m todo add \"Buy milk\"")
            for t in tasks:
                mark = "x" if t["done"] else " "
                print(f"[{mark}] {t['id']}. {t['title']}")
        elif args.command == "done":
            task = core.complete_task(tasks, args.id)
            print(f"Completed #{task['id']}: {task['title']}")
        elif args.command == "remove":
            task = core.remove_task(tasks, args.id)
            print(f"Removed #{task['id']}: {task['title']}")
    except (KeyError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    core.save_tasks(tasks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
