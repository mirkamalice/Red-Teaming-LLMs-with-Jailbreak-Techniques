import os
import glob
import re

def remove_prefix_from_files(directory):
    """
    Removes "zzz-" prefixes from filenames in a directory.

    Args:
        directory (str): The path to the directory containing the files.
    """

    for filepath in glob.glob(os.path.join(directory, "*")):  # Process all files
        filename = os.path.basename(filepath)
        
        match = re.match(r"^(-cant-)(.*)", filename)
        
        if match:
            prefix_to_remove = match.group(1)
            new_filename = filename[len(prefix_to_remove):]  # Remove the matched prefix
            new_filepath = os.path.join(directory, new_filename)
            
            try:
               os.rename(filepath, new_filepath)
               print(f"Renamed '{filename}' to '{new_filename}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")
        

if __name__ == "__main__":
    target_directory = input("Enter the directory path where your files are located: ")

    if not os.path.isdir(target_directory):
        print("Error: The provided path is not a valid directory.")
    else:
      remove_prefix_from_files(target_directory)
      print("Finished processing files.")
