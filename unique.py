def extract_unique_entries(input_file, output_file):
    # Create a set to store the unique entries
    unique_entries = []
    # Read the input file line by line
    with open(input_file, 'r') as file:
        for line in file:
            line2 = line.split(' ')[-1]
            # Strip the newline character and add the line to the set
            if line2[0:43] not in unique_entries:
                unique_entries.append(line2[0:43].strip())
    # Write the unique entries to the output file
    with open(output_file, 'w') as file:
        for entry in unique_entries:
            file.write(entry + '\n')
# Example usage
#input_file = 'input.txt'
input_file = 'youtube_urls.txt'
#output_file = 'output.txt'
output_file = 'youtube_urls.txt'
extract_unique_entries(input_file, output_file)
print(f"Unique entries written to {output_file}")
