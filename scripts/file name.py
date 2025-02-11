import os
import glob

def remove_text_from_files(directory):
    """
    Removes "-im sorry" from filenames in the given directory.

    Args:
        directory (str): The path to the directory containing the files.
    """

    for filepath in glob.glob(os.path.join(directory, "*")):  # Process all files
        filename = os.path.basename(filepath)
        
        if "-im sorry" in filename:
            new_filename = filename.replace("-Im sorry", "")  # Remove the unwanted text
            new_filepath = os.path.join(directory, new_filename)
            
            try:
                os.rename(filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    remove_text_from_files(current_directory)
    print("Finished processing files.")
