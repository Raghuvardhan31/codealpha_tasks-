Internet Search Tool
This project is a simple Python script that performs internet searches using the googlesearch library. It allows users to enter a search query and returns a list of URLs related to the query.

Features
Accepts user input for a search query.
Fetches search results directly from the internet.
Displays a specified number of search results (default is 10).
Handles exceptions gracefully.
Requirements
To run this project, you need the following:

Python 3.x installed on your system.
The googlesearch-python library.
Installation
Clone this repository or copy the script into a .py file.
Install the required library:
bash
Copy code
pip install googlesearch-python  
Usage
Run the script:

bash
Copy code
python script_name.py  
Replace script_name.py with the name of your Python file.

Enter your search query when prompted.

View the results displayed in the terminal.

Code Explanation
internet_search(query, num_results=10)
This function performs the following steps:

Accepts a search query as input.
Uses the search function from the googlesearch library to fetch URLs related to the query.
Returns a list of search results or an error message in case of failure.
Main Script
Prompts the user to enter a search query.
Calls the internet_search function with the query.
Displays the search results in a numbered list format.
Example Output
plaintext
Copy code
Enter your search query: Python programming tutorials  
Searching for: Python programming tutorials  

1. https://www.python.org/  
2. https://realpython.com/  
3. https://www.geeksforgeeks.org/python-programming-language/  
4. https://www.w3schools.com/python/  
5. https://docs.python.org/3/tutorial/  
...  
Limitations
The googlesearch library may not work in certain regions due to restrictions or API limitations.
Results depend on the accuracy and availability of the googlesearch library.
Future Improvements
Add support for extracting content from the returned URLs.
Enhance the script to store results in a file (e.g., JSON or CSV).
Implement a graphical user interface (GUI) for better usability.
License
This project is licensed under the MIT License.
