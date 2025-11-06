"""Parser module for extracting intents and descriptions from sample files."""

import re
import csv
from pathlib import Path
from typing import List, Tuple

def clean_description(text: str) -> str:
    """Remove annotation tags from the description text.
    
    Args:
        text: The description text that may contain annotation tags
        
    Returns:
        The cleaned text with annotation tags removed
    """
    # Remove any <annotation>...</annotation> tags and their content
    cleaned_text = re.sub(r'<annotation[^>]*>.*?</annotation>', '', text)
    return cleaned_text.strip()

def parse_sample(line: str) -> Tuple[str, str]:
    """Parse a single sample line to extract intent and description.
    
    Args:
        line: A line containing the sample XML-like structure
        
    Returns:
        A tuple of (intent_name, cleaned_description)
    """
    # Extract intent name using regex
    intent_match = re.search(r'intentref="([^"]*)"', line)
    intent_name = intent_match.group(1) if intent_match else ""
    
    # Extract description between >< tags
    desc_match = re.search(r'>([^<].*?)</sample>', line)
    description = desc_match.group(1) if desc_match else ""
    
    # Clean the description
    cleaned_description = clean_description(description)
    
    return intent_name, cleaned_description

def process_file(input_path: str, output_path: str) -> None:
    """Process the input file and write results to CSV.
    
    Args:
        input_path: Path to the input file containing samples
        output_path: Path where the CSV output should be written
    """
    samples: List[Tuple[str, str]] = []
    
    # Read and process input file
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '<sample' in line and 'intentref=' in line:
                intent, description = parse_sample(line.strip())
                if intent and description:
                    samples.append((intent, description))
    
    # Write to CSV file
    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Intent', 'Description'])  # Header
        writer.writerows(samples)

def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Parse sample files and extract intents and descriptions')
    parser.add_argument('input_file', help='Path to the input file containing samples')
    parser.add_argument('output_file', help='Path to the output CSV file')
    
    args = parser.parse_args()
    
    process_file(args.input_file, args.output_file)

if __name__ == '__main__':
    main()