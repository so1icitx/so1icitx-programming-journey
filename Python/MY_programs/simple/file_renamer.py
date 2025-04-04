import os
import datetime
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_parser():
    """Set up command-line argument parser."""
    parser = argparse.ArgumentParser(description="Rename files in a directory with a prefix and timestamp.")
    parser.add_argument('directory', type=str, help="Directory containing files to rename")
    parser.add_argument('--prefix', type=str, default='file_', help="Prefix to add to filenames")
    return parser

def validate_directory(directory):
    """Validate that the directory exists."""
    if not os.path.isdir(directory):
        logging.error(f"Directory '{directory}' does not exist.")
        raise ValueError(f"Directory '{directory}' does not exist.")
    return directory

def get_timestamp():
    """Generate a timestamp string for filenames."""
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def rename_files(directory, prefix):
    """Rename all files in the directory with the given prefix and timestamp."""
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            logging.warning(f"No files found in '{directory}'.")
            return

        timestamp = get_timestamp()
        for idx, filename in enumerate(files, 1):
            old_path = os.path.join(directory, filename)
            extension = os.path.splitext(filename)[1]
            new_filename = f"{prefix}{timestamp}_{idx:03d}{extension}"
            new_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_path, new_path)
                logging.info(f"Renamed '{filename}' to '{new_filename}'")
            except Exception as e:
                logging.error(f"Failed to rename '{filename}': {e}")

        logging.info(f"Renamed {len(files)} files in '{directory}'.")
    except Exception as e:
        logging.error(f"Error processing directory '{directory}': {e}")

def main():
    """Main function to run the file renamer."""
    parser = setup_parser()
    args = parser.parse_args()
    
    try:
        directory = validate_directory(args.directory)
        rename_files(directory, args.prefix)
    except ValueError as e:
        logging.error(str(e))
        exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
