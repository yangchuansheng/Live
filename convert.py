import json
import re
import sys
import os

def convert_to_json(input_file):
    channels = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process the lines in pairs
    for i in range(0, len(lines), 2):
        info_line = lines[i].strip()
        url_line = lines[i+1].strip() if i+1 < len(lines) else ""
        
        # Extract the name using regex
        name_match = re.search(r'tvg-name="([^"]+)"', info_line)
        if name_match:
            name = name_match.group(1)
            
            # Create a dictionary for the channel
            channel = {
                "name": name,
                "url": url_line
            }
            
            channels.append(channel)
    
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
