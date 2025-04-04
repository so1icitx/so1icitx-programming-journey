import csv
import statistics
import argparse
import logging
from collections import defaultdict

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_parser():
    """Set up command-line argument parser."""
    parser = argparse.ArgumentParser(description="Analyze numerical data in a CSV file.")
    parser.add_argument('csv_file', type=str, help="Path to the CSV file")
    parser.add_argument('--column', type=str, required=True, help="Column name to analyze")
    return parser

def read_csv_file(csv_file, column_name):
    """Read numerical data from the specified column in a CSV file."""
    data = []
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            if column_name not in reader.fieldnames:
                logging.error(f"Column '{column_name}' not found in CSV.")
                raise ValueError(f"Column '{column_name}' not found.")
            
            for row in reader:
                try:
                    value = float(row[column_name])
                    data.append(value)
                except (ValueError, TypeError):
                    logging.warning(f"Skipping invalid value in row: {row[column_name]}")
        return data
    except FileNotFoundError:
        logging.error(f"CSV file '{csv_file}' not found.")
        raise
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        raise

def analyze_data(data):
    """Compute statistics for the data."""
    if not data:
        logging.warning("No valid data to analyze.")
        return defaultdict(lambda: None)
    
    stats = {
        'count': len(data),
        'sum': sum(data),
        'average': statistics.mean(data),
        'median': statistics.median(data),
        'min': min(data),
        'max': max(data)
    }
    return stats

def print_stats(stats):
    """Print the computed statistics."""
    for key, value in stats.items():
        if value is not None:
            logging.info(f"{key.capitalize():<10}: {value:.2f}")

def main():
    """Main function to analyze CSV data."""
    parser = setup_parser()
    args = parser.parse_args()
    
    try:
        data = read_csv_file(args.csv_file, args.column)
        stats = analyze_data(data)
        print_stats(stats)
    except Exception as e:
        logging.error(str(e))
        exit(1)

if __name__ == "__main__":
    main()
