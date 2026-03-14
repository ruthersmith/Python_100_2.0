
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
class LinkedInJobApplier:

    # JOB_SEARCH_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102380872&keywords=python%20developer&location=Boston%2C%20Massachusetts%2C%20United%20States"
    JOB_SEARCH_URL =  "https://www.linkedin.com/jobs/"
    def __init__(self):
        # Keep Chrome browser open for now after the program finishes
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=chrome_options)
        
        self.driver = webdriver.Chrome()

    def sign_in(self):
        """ Sign in to LinkedIn using the provided email and password"""

        email =os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        # Wait for the email input to be visible, then type
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "session_key"))
        )
        email_input.send_keys(email)

        # Wait for the password input to be visible, then type
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "session_password"))
        )
        password_input.send_keys(password)

        # Wait for the sign-in button to be visible, then click
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-form__submit-btn--full-width"))
        )
        sign_in_button.click()

    def apply_to_jobs(self):
        time.sleep(2)
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r1:"))
        )
        search_input.send_keys("python developer Easy Apply", Keys.ENTER)

        jobs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[componentkey*="job-card-component"]')
            )
)
        for job in jobs:
            print(job.find_element(By.TAG_NAME, "p").text)


    def run(self):
         # opens the browser at the specified url
        self.driver.get(url=LinkedInJobApplier.JOB_SEARCH_URL)
        time.sleep(3)
        self.sign_in()  
        self.apply_to_jobs()
        self.driver.quit()
        

if __name__ == "__main__":
    job_applier = LinkedInJobApplier()
    job_applier.run()