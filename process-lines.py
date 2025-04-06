import sys

input_file_path = 'data.txt'
output_file_path = 'output.txt'

# Open the input file in read mode and the output file in write mode
with open(input_file_path, 'r', encoding="utf-8") as infile, open(output_file_path, 'w', encoding="utf-8") as outfile:
    a_ans = ""
    b_ans = ""
    c_ans = ""
    d_ans = ""
    e_ans = ""
    f_ans = ""
    g_ans = ""
    h_ans = ""
    no_match = False
    correct_ans = "The correct answer is: "
    # Read and write each line one by one
    for line in infile:
        
        if "a." in line:
            a_ans = line
        elif "b." in line:
            b_ans = line            
        elif "c." in line:
            c_ans = line             
        elif "d." in line:
            d_ans = line             
        elif "e." in line:
            e_ans = line 
        elif "f." in line:
            f_ans = line 
        elif "g." in line:
            g_ans = line 
        elif "h." in line:
            h_ans = line

        if correct_ans in line: ### answer line
            ans_part = line.replace(correct_ans, "")
            line = correct_ans 
            if ans_part in a_ans:
                line += a_ans
            elif ans_part in b_ans:
                line += b_ans            
            elif ans_part in c_ans:
                line += c_ans             
            elif ans_part in d_ans:
                line += d_ans             
            elif ans_part in e_ans:
                line += e_ans 
            elif ans_part in f_ans:
                line += f_ans 
            elif ans_part in g_ans:
                line += g_ans 
            elif ans_part in h_ans:
                line += h_ans             
            else:
                no_match = True
                
            if no_match:
                no_match = False # reset it
            else:
                if ". " in line:    
                    line = line.replace(". ", ") ")                
                else:
                    line = line.replace(".", ") ") 

        outfile.write(line)
            
        print(f'Wrote line: {line.strip()}')  # Optional: print to console
