from pathlib import Path
import re

def get_md5(input_str):
    #Determine a pattern to search in the text and create a list with all the results
    match_results = re.findall("[0-9a-fA-F]{32}", input_str)
    #Create a new list deleting the results appearing multiple times
    final_results = []
    for element in match_results:
        if element not in final_results:
            final_results.append(element)
    #Create a string by joining all the elements in the list
    output_text = "\n".join(final_results)
    return output_text

#Create a file object for the file I need and extract the text
input_path = Path.home() / "filename.txt"
with input_path.open(mode="r", encoding="utf-8") as input_file:
    text = input_file.read()

#Apply the function to the text extracted from the file
reduced_text = get_md5(text)

#Create a new file containing the text I obtained from the function
output_path = Path.home() / "new_filename.txt"
with output_path.open(mode="w", encoding="utf-8") as output_file:
    output_file.write(reduced_text)
