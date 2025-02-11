
import os

def process_text_files():
    """
    Opens text files in the current directory, displays content, and renames them based on user input.
    """

    try:
        files = [f for f in os.listdir() if f.lower().endswith(".txt")]
    except Exception as e:
         print(f"An unexpected error occurred while listing files: {e}")
         return


    for filename in files:
        filepath = os.path.join(filename)
        
        try:
             with open(filepath, 'r') as file:
                  content = file.read()
                  print(f"\n--- Content of {filename} ---")
                  print(content)
        except FileNotFoundError:
              print(f"Error: File not found: {filepath}")
              continue # Skip to next file
        except Exception as e:
              print(f"Error reading file {filename}: {e}")
              continue
        
        while True:
             action = input("Enter 'a' to rename to 'aaa-...' or 'z' to rename to 'zzzzz-...', or any other key to continue to the next file: ").lower()

             if action == 'a':
                 try:
                      new_filename = f"aaa-{filename}"
                      new_filepath = os.path.join(new_filename)
                      os.rename(filepath, new_filepath)
                      print(f"Renamed {filename} to {new_filename}")
                      break  # Move to the next file
                 except Exception as e:
                     print(f"Error renaming {filename}: {e}")
                     break # Move to the next file after logging error
             elif action == 'z':
                  try:
                       new_filename = f"zzzzz-{filename}"
                       new_filepath = os.path.join(new_filename)
                       os.rename(filepath, new_filepath)
                       print(f"Renamed {filename} to {new_filename}")
                       break  # Move to the next file
                  except Exception as e:
                       print(f"Error renaming {filename}: {e}")
                       break
             else:
                  print("Skipping file.")
                  break
                  
if __name__ == "__main__":
    process_text_files()

