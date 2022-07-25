# Importing libraries
import difflib
import webbrowser

# Opening and reading contents of two files by taking input from user.
with open(input("Enter complete path of file 1 for comparison: ")) as file1:
    file1_text = file1.read()
with open(input("Enter complete path of file 2 for comparison: ")) as file2:
    file2_text = file2.read()

# Calculating the differnce using HtmlDiff() function from difflib library.
difference = difflib.HtmlDiff().make_file(file1_text.splitlines(), file2_text.splitlines(), fromdesc='file1', todesc='file2')

# Storing the difference in a separate file.
html_file_path = "C:\\Users\\Prasad Charde\\Jupyter Notebook files\\Difference.html"
with open(html_file_path, 'w') as out_file:
    out_file.write(difference)
    
# Opening the output HTML file in new tab of a web browser. 
webbrowser.open_new_tab(html_file_path)   

print()
print(r"Comparison Done!   Please open file: C:\Users\Prasad Charde\Jupyter Notebook files\Difference.html")