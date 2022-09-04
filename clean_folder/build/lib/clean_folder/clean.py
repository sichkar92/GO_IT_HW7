import os
import pprint
import sys
from trash_sorter import arrange_folder, folder_handler, extentions_handler


def main():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Target folder doesn't defined!")
        return
    if not os.path.exists(target_folder):
        print("Bad path!")
        return
    arrange_folder(target_folder)
    # Output results of script
    print("\n*****FILES BY CATEGORY:*****\n")
    pprint.pprint(folder_handler(target_folder))
    print("\n*****SORTED EXTENTIONS:*****\n")
    pprint.pprint(extentions_handler(folder_handler(target_folder)))


if __name__ == "__main__":
    main()
