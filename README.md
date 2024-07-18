#### Content_MatchingApp

This is a simple Python web application (app) that recommends content to users based on their interests. The app consumes two JSON files—one containing user information and interests, and the other containing tagged content, and provide a user interface (UI) to display which content is relevant to which users based on specified interest thresholds.

### Structure the app to:
1.	Load and parse the JSON files for users and content.
2.	Implement the matching logic to find relevant content for each user.
3.	Develop a UI to display the users and their relevant content.
4.	Include unit tests for data ingestion and matching logic.
5.	Provide instructions, in a README file, for running the application locally.
# The matching logic for content and users is based on the following rules:
•	Each user has a list of interests with a type, value, and threshold.
•	Each piece of content has tags with a type, value, and threshold.
•	A piece of content is considered relevant to a user if the user's interest threshold is equal to or greater than the tag's threshold.
•	The function also handles scenarios where no content matches a user's interests by adding a default message or handling multiple matches appropriately.
•	At the front-end, clear messages are displayed for cases where no content matches a user’s interests.
•	The UI is user friendly and clearly lists matched content. The UI is responsive and easy to navigate.

### Setup to run the app locally 

1.	Install a version of Python 3. Options include:
o	(macOS) An installation through Homebrew on macOS using brew install python3.
o	(All operating systems) A download from Anaconda (for data science purposes).
2.	Clone this git repo: https://github.com/remimomo/content_matchingApp.git 
3.	Navigate to the project directory: cd content_matchingApp
4.	Create and activate a virtual environment:
•	python3 -m venv venv 
•	source venv/bin/activate # On Windows use `venv\Scripts\activate`

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Save the JSON data into `users.json` and `content.json` in the root directory, or use the upload feature on the webpage.

4. Run the application:
    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000` to view the content recommendations.

6. To upload new JSON files, use the file upload form on the webpage.

# Running Tests
To run the tests, execute:
```bash
python -m unittest discover -s app/tests


### Explanation of the Unit Test 
The unit tests are located in the ‘app/tests/test_matching.py’ file. They use Python’s built-in unittest framework to define and run the tests.
# setUp Method
•	setUp method is called before each test method to initialise common test data (users and content) that will be used in the test methods.
•	self.users and self.content are initialised with sample data.
# Test Methods
# Test Case: No Matching Content
def test_no_matching_content(self):
    # Test case where no content matches the user's interests
    matches = match_content_to_users(self.users, self.content)
    self.assertEqual(len(matches["John Dow"]), 0)  # Expecting no matches for John Dow
•	test_no_matching_content: Tests the scenario where there is no matching content for the user's interests.
•	Calls match_content_to_users with the initialized test data.
•	Asserts that the length of the matched content list for "John Dow" is 0 using self.assertEqual. This means no content should match his interests based on the provided data.
# Test Case: Matching Content
•	test_matching_content: Tests the scenario where content matches the user's interests.
•	Adds a new content item to self.content that matches one of John Dow's interests.
•	Calls match_content_to_users with the modified test data.
•	Asserts that the length of the matched content list for "John Dow" is 1 using self.assertEqual. This means one piece of content should match his interests.
•	Asserts that the title of the matched content is "Investment News" using self.assertEqual. This ensures the correct content is matched.
# Main Block
•	Runs the tests when the script is executed directly.
## How the Unit Test Works
•	Execution:
o	The unittest framework is used to run the tests. When the script is executed, it automatically finds any class that inherits from unittest.TestCase and runs all methods that start with test.
o	The if __name__ == '__main__': unittest.main() line ensures that the tests are executed when the script is run directly.
•	Assertions:
o	The assertEqual method is used to check if the actual value matches the expected value.
o	The assertTrue method checks if the given expression evaluates to True.
o	If any assertion fails, the test will fail, indicating that there is an issue with the corresponding functionality.
•	Output:
o	The test results are printed to the console. If all tests pass, it will show a success message. If any test fails, it will show which test failed and why.
### UI Structure and Functionality
The index.html template provides the main content for the home page. It displays the matched content for each user.The UI is built using HTML, Bootstrap for styling, and JavaScript for handling dynamic actions like form submissions. Here's a detailed walkthrough of the different components and how they interact with each other:

1. Head Section
The head section includes the necessary meta tags, links to Bootstrap CSS for styling, and some custom CSS for additional styling.

2. Body Section
The body section is structured into different parts: the container, header, upload section, search form, user sections, and pagination.

2.1. Container
The entire content is wrapped inside a Bootstrap container to ensure proper alignment and spacing.

2.2. Header
A simple header displays the title of the application.

2.3. Upload Section
This section allows users to upload JSON files for users and content.
•	Form: The form uses POST method and multipart/form-data encoding to allow file uploads.
•	Flash Messages: Displays messages to the user after file uploads.

2.4. Search Form
A search bar allows users to filter content by title.
•	Input Field: Allows users to enter search queries.
•	Button: Submits the search form to filter content.

2.5. User Sections
Displays the list of users and the content that matches their interests.
•	Conditional Rendering: If there are no matches, an error message is displayed. Otherwise, the matched content for each user is displayed.
•	User Sections: Each user has their own section with a list of matched content.

2.6. Pagination
Pagination controls allow users to navigate through pages of users.
•	Previous Button: Navigates to the previous page if not on the first page.
•	Page Numbers: Displays page numbers and highlights the current page.
•	Next Button: Navigates to the next page if not on the last page.

2.7. JavaScript for File Uploads
Handles form submissions for file uploads without reloading the page.
•	Event Listener: Prevents the default form submission behavior.
•	FormData: Creates a FormData object from the form.
•	Fetch API: Sends the form data to the server using the Fetch API.
•	Response Handling: Reloads the page on successful upload, or displays an error message if the upload fails.
![image](https://github.com/user-attachments/assets/1dc98caf-377e-4404-8e83-3f06c254408b)
