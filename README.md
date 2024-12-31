🚀 LinkedIn Auto Connect Bot

An automation script that helps you connect with HR professionals on LinkedIn automatically using Selenium and Python.


📑 Overview

This project automates the process of:


Logging into LinkedIn.

Searching for "Human Resources" professionals.

Sending connection requests.

Scrolling through multiple result pages and repeating the process.

🛠️ Technologies Used

```Python

Selenium

WebDriver Manager
```
📦 Setup Instructions

✅ 1. Clone the Repository

```bash

Copy code

git clone https://github.com/chxikva/linkedin-auto-connect.git  

cd linkedin-auto-connect  
```
✅ 2. Create a Virtual Environment

```bash

Copy code

python -m venv venv  

source venv/bin/activate  # On macOS/Linux  

venv\Scripts\activate     # On Windows  
```
✅ 3. Install Dependencies

```bash

Copy code

pip install -r requirements.txt  
```
✅ 4. Update Script with Chrome Path

Ensure your linkedin_auto_connect.py script has the correct Chrome binary path:


```python

Copy code

options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  
```
🚀 Usage

Run the script:

```bash

Copy code

python linkedin_auto_connect.py  

Enter your LinkedIn credentials when prompted.
```
The script will:

Log in to LinkedIn.

Search for HR professionals.

Send connection requests automatically.

Verify sent invites on your LinkedIn Invitations Page:

👉 LinkedIn Sent Invitations

🔄 Customization

Search Keywords: Update the search keyword in the script:

```python

Copy code

driver.get("https://www.linkedin.com/search/results/people/?keywords=human%20resources")  
```

Scroll Limits: Adjust the number of scrolls/pages to visit:
```python
Copy code
PAGE_LIMIT = 5  
```
🛡️ Security Tips
Avoid sharing your LinkedIn credentials publicly.
Do not run the script excessively to prevent account restrictions.

🤝 Contributing
Contributions are welcome!

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Submit a pull request
📜 License
This project is licensed under the MIT License.

📬 Contact

Author: chxikva

LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/irakli-chkhikvadze-a4972a109/)

Feel free to open an issue for feedback or questions!

⭐ If you find this project useful, please star the repository! ⭐
