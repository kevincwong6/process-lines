import sys

input_file_path = 'data.txt'
output_file_path = 'output.txt'

# Open the input file in read mode and the output file in write mode
with open(input_file_path, 'r', encoding="utf-8") as infile, open(output_file_path, 'w', encoding="utf-8") as outfile:
    # Read and write each line one by one
    for line in infile:
        
        if "correct answer" not in line:
            outfile.write(line)
            print(line)
            
       
