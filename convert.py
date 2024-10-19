import json
import re
import sys
import os

def convert_to_json(input_file):
    channels = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip lines that don't start with #EXTINF
        if not line.startswith('#EXTINF'):
            i += 1
            continue
        
        # Extract the name using regex
        name_match = re.search(r'tvg-name="([^"]+)"', line)
        if name_match:
            name = name_match.group(1)
            
            # Look for the next non-empty line (should be the URL)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            
            if i < len(lines):
                url = lines[i].strip()
                
                # Create a dictionary for the channel
                channel = {
                    "name": name,
                    "url": url
                }
                
                channels.append(channel)
        
        i += 1
    
    # Convert the list of channels to JSON
    json_output = json.dumps(channels, ensure_ascii=False, indent=2)
    return json_output

def main():
    # Check if the input file path is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python convert_to_json.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: The file '{input_file_path}' does not exist.")
        sys.exit(1)

    # Convert the input file to JSON
    json_output = convert_to_json(input_file_path)

    # Define the output file name
    output_file_path = 'tv.json'

    # Save the JSON output to tv.json
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(json_output)

    print(f"JSON output has been saved to {output_file_path}")

if __name__ == "__main__":
    main()
