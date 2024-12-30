from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass

# 1) Configure Chrome (Headless mode)
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--disable-dev-shm-usage")

# 2) Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 3) Get LinkedIn credentials via terminal
email = input("Enter your LinkedIn email: ")
password = getpass.getpass("Enter your LinkedIn password (hidden): ")

# 4) Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(3)
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# 5) Go to People-Only search results for Human Resources
driver.get("https://www.linkedin.com/search/results/people/?keywords=human%20resources")
time.sleep(3)

# 6) Define a function to invite all profiles on the current page
def invite_all_on_page():
    connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[text()='Connect']]")
    print(f"Found {len(connect_buttons)} 'Connect' buttons on this page.")

    for button in connect_buttons:
        try:
            button.click()
            time.sleep(2)
            # Click 'Send' or 'Send now' in the popup
            send_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Send')]")
            if send_buttons:
                send_buttons[0].click()
                print("✅ Sent an invitation!")
            else:
                print("⚠️ Could not find the 'Send' button after clicking 'Connect'.")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Skipped a profile due to error: {e}")
            continue

# 7) Loop through multiple pages
PAGE_LIMIT = 5  # Adjust this as you like

for page_number in range(1, PAGE_LIMIT + 1):
    print(f"--- Inviting on Page {page_number} ---")
    invite_all_on_page()

    # Attempt to click the Next button
    try:
        next_button = driver.find_element(By.XPATH, "//button[contains(@class,'artdeco-pagination__button--next')]")
        # If the next button is disabled or not displayed, break
        if not next_button.is_enabled():
            print("No more pages or Next button disabled.")
            break
        next_button.click()
        time.sleep(4)  # Let the page load
    except Exception as e:
        print(f"Could not find or click Next button (end of pages). Error: {e}")
        break

# 8) Close the browser
driver.quit()
print("✅ Done sending invitations in headless mode!")
