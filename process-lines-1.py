import sys

input_file_path = 'data.txt'
output_file_path = 'output.txt'

found_question_line = False
question_line = ""
# Open the input file in read mode and the output file in write mode
with open(input_file_path, 'r', encoding="utf-8") as infile, open(output_file_path, 'w', encoding="utf-8") as outfile:
    # Read and write each line one by one
    for line in infile:
        
        if found_question_line:
            outfile.write(question_line)
            outfile.write(line + "\n")
            found_question_line = False
            print(question_line)
            print(line)
            print()
            #user_input = input("Please enter something: ")
        elif "Question " in line:
            question_line = line
            found_question_line = True
            
       
