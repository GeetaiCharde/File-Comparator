# Importing libraries
import difflib
import webbrowser

print('''
------------------------------------------------------------------- 
| *************** Welcome to file comparison tool *************** |
------------------------------------------------------------------- \n''')

# extracting text from file 1 
with open(input("Enter complete path of file 1 for comparison: ")) as file1:    # taking input from user 
    f1_start_pos = int(input("Enter starting line number for file 1 : ")) 
    f1_stop_pos = int(input("Enter numbers of line in file 1 to read : ")) 
    file1_data = [] 
    file1_lines = list(range(f1_start_pos-1, f1_stop_pos))                 # converting requirements in range of lines in file 
    
    for position, line in enumerate(file1):                                # extracting required lines from text_file
        if position in file1_lines:  
            file1_data.append(line) 
            
    file1_text = ''.join(str(word) for word in file1_data)                 # converting list into text 
    
# extracting text from file 2 
with open(input("Enter complete path of file 2 for comparison: ")) as file2:
    f2_start_pos = int(input("Enter starting line number for file 2 : "))
    f2_stop_pos = int(input("Enter numbers of line in file 2 to read : "))
    file2_data = [] 
    file2_lines = list(range(f2_start_pos-1, f2_stop_pos)) 
    
    for position, line in enumerate(file2):
        if position in file2_lines:
            file2_data.append(line) 
            
    file2_text = ''.join(str(word) for word in file2_data) 
    
difference = difflib.HtmlDiff().make_file(file1_text.splitlines(), file2_text.splitlines(), fromdesc='file1', todesc='file2') 

html_file_path = "C:\\Users\\Prasad Charde\\Jupyter Notebook files\\Difference.html" 
with open(html_file_path, 'w') as out_file:
    out_file.write(difference) 

webbrowser.open_new_tab(html_file_path) 

print()
print(r'''Comparison Done! 
If difference file is not opened automatically, then please manually open file at : C:\Users\Prasad Charde\Jupyter Notebook files\Difference.html''')