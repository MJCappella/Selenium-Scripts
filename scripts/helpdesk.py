from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initializing the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Locate the email and password fields and input credentials
email_field = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div[1]/input')
email_field.send_keys('helpdesk@softclans.co.ke')


password_field = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div[2]/input')
password_field.send_keys('admin@123')

button = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/form/div[3]/button')
button.click()

# password_field.send_keys(Keys.RETURN) 

try:
    # Opening the helpdesk website
    driver.get('https://softclans.co.ke/rfda_helpdesk/public/tickets?departments%5B%5D=Support&status%5B%5D=Closed&show%5B%5D=inbox')  # Replace with the actual URL

    # Locate all the ordered links (assuming they are in an ordered list <ol>)
    links = driver.find_elements(By.CSS_SELECTOR, 'tbody a')

    # Iterate through each link
    for link in links:
        # Click the link
        link.click()
        time.sleep(10)

        try:
            # Locate the "Generate PDF" button and click it
            generate_pdf_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/section/div[1]/div[5]/div[2]/div[1]/a"]')
            generate_pdf_button.click()
            time.sleep(15)  # Adjust sleep time to ensure the PDF is generated
        except Exception as e:
            print(f"An error occurred: {e}")

        # Navigate back to the main page
        driver.back()
        time.sleep(2)  # Adjust sleep time as needed

        # Re-fetch the links because the DOM might have changed after navigation
        links = driver.find_elements(By.CSS_SELECTOR, 'tbody a')

finally:
    # Close the WebDriver
    time.sleep(1000)
    driver.quit()