import os
import glob
import re

def check_and_rename_files(directory):
    """
    Opens text files in a directory, checks if "can't" is present,
    and adds "zzz" to the beginning of the filename if it is.

    Args:
        directory (str): The path to the directory containing the text files.
    """

    for filepath in glob.glob(os.path.join(directory, "*.txt")):  # Only process .txt files
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if re.search(r"\bI'm sorry\b", content, re.IGNORECASE):  # Use re for case-insensitive word check
                    
                    filename = os.path.basename(filepath)
                    new_filename = "zzz-Im sorry-" + filename
                    new_filepath = os.path.join(directory, new_filename)

                    os.rename(filepath, new_filepath)
                    print(f"Renamed '{filename}' to '{new_filename}'")
        except Exception as e:
            print(f"Error processing '{filepath}': {e}")


if __name__ == "__main__":
    target_directory = input("Enter the directory path where your text files are located: ")

    if not os.path.isdir(target_directory):
        print("Error: The provided path is not a valid directory.")
    else:
      check_and_rename_files(target_directory)
      print("Finished processing files.")
