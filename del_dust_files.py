import os
import shutil

def read_del_list(del_list_path):
    try:
        with open(del_list_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File not found: {del_list_path}")
        return []

def delete_files_and_dirs(directory, del_list):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if item in del_list:
                try:
                    shutil.rmtree(item_path)  # ディレクトリ名がdel_lstにある場合はディレクトリごと削除
                    print(f"Deleted directory: {item_path}")
                except Exception as e:
                    print(f"Error deleting directory {item_path}: {e}")
            else:
                delete_files_and_dirs(item_path, del_list)
        else:
            item_base_name = os.path.basename(item_path)
            if item_base_name in del_list:
                try:
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
                except Exception as e:
                    print(f"Error deleting file {item_path}: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python delete_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        sys.exit(1)

    del_list = read_del_list("del.lst")

    if not del_list:
        print("No files/directories to delete in del.lst")
        sys.exit(1)

    delete_files_and_dirs(directory_path, del_list)
    print("Deletion completed.")
