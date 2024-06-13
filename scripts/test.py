from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to wait for the page to load by waiting for a specific element
def wait_for_page_load(driver, timeout=60):
    try:
        # Wait until an element with a specific tag or attribute is found
        driver.implicitly_wait(15)
        # WebDriverWait(driver, timeout)
    except Exception as e:
        print(f"Exception occurred while waiting for the page to load: {e}")

# Initialize WebDriver
# driver = webdriver.Chrome()
driver = webdriver.Firefox()

try:
    # Open the first URL
    driver.get('https://softclans.co.ke')
    # Wait for the first page to load
    wait_for_page_load(driver)

    # Open the second URL
    driver.get('https://softclans.co.ke/rfda_helpdesk/public/tickets?departments%5B%5D=Support&status%5B%5D=Closed&show%5B%5D=inbox')
    driver.delete_cookie("laravel_session")
    #driver.add_cookie({"name": "XSRF-TOKEN", "value": "eyJpdiI6Im5KQk1sb2ppd2RaV1UvWmxtUk85TGc9PSIsInZhbHVlIjoiZTQ0aURqTVBCU252UmRMaWt3MVFxMlp5TVVIVFIvWjNuUENvZ3NueWR6WkY3Q00vbHEwSFlHZlJ5cENEOXdBdEh0TTQwNjhrN0xrQWxUNDdkeHFmdktJN2tZVGdWdlYyYWJ4aXlwRXF6R2NCQ3N5OFdSQXZLUFdHZ21Pd1NLbGMiLCJtYWMiOiI1ZWRiM2U3MmI5NDllYWRhZDM1NTc5NTJmZGJhN2E5MGQ4NTgyYmZlMjU0NGRkMTAzMTE4OWFlM2RjZDNjZTVhIiwidGFnIjoiIn0="})
    driver.add_cookie({"name": "laravel_session", "value": "eyJpdiI6IndJR21jclFOUGZkZlpiZjBsbnQxNEE9PSIsInZhbHVlIjoiMWVsd0FGQU85aFByb0RTMDJJdGZxeUtOaUwyYVFHSzAvc0N2T2lhUDYwQThCRjVhcE43b1hBd2E1d0p2VTIzOExTQVNaNG1pbXhraUNVdVNtSzhoak5VSXFIQ3N4aVBIZ0ZPNTNIZ1NpSFcrS0xEbjJtNEZ5d09Bcy94TTRaWi8iLCJtYWMiOiIyZWY1OTJlYjQyNmYwOGEzYTljMDgyMDIzYzUwYTlmYzM1NTRjYjYwZTk4MDhhMTgwN2ZkYTRiYTBkNTQyMDQ2IiwidGFnIjoiIn0%3D"})

    # # Wait for the second page to load
    wait_for_page_load(driver)
    # Delete a cookie with name 'test1'
    driver.delete_cookie("laravel_session")
    #driver.add_cookie({"name": "XSRF-TOKEN", "value": "eyJpdiI6Im5KQk1sb2ppd2RaV1UvWmxtUk85TGc9PSIsInZhbHVlIjoiZTQ0aURqTVBCU252UmRMaWt3MVFxMlp5TVVIVFIvWjNuUENvZ3NueWR6WkY3Q00vbHEwSFlHZlJ5cENEOXdBdEh0TTQwNjhrN0xrQWxUNDdkeHFmdktJN2tZVGdWdlYyYWJ4aXlwRXF6R2NCQ3N5OFdSQXZLUFdHZ21Pd1NLbGMiLCJtYWMiOiI1ZWRiM2U3MmI5NDllYWRhZDM1NTc5NTJmZGJhN2E5MGQ4NTgyYmZlMjU0NGRkMTAzMTE4OWFlM2RjZDNjZTVhIiwidGFnIjoiIn0="})
    driver.add_cookie({"name": "laravel_session", "value": "eyJpdiI6IndJR21jclFOUGZkZlpiZjBsbnQxNEE9PSIsInZhbHVlIjoiMWVsd0FGQU85aFByb0RTMDJJdGZxeUtOaUwyYVFHSzAvc0N2T2lhUDYwQThCRjVhcE43b1hBd2E1d0p2VTIzOExTQVNaNG1pbXhraUNVdVNtSzhoak5VSXFIQ3N4aVBIZ0ZPNTNIZ1NpSFcrS0xEbjJtNEZ5d09Bcy94TTRaWi8iLCJtYWMiOiIyZWY1OTJlYjQyNmYwOGEzYTljMDgyMDIzYzUwYTlmYzM1NTRjYjYwZTk4MDhhMTgwN2ZkYTRiYTBkNTQyMDQ2IiwidGFnIjoiIn0%3D"})

    #  Deletes all cookies

    # input("Press Enter to close the browser and exit the script...")
    # driver.delete_all_cookies()
    input("Press Enter to close the browser and exit the script...")
    # driver.get('https://softclans.co.ke/rfda_helpdesk/public/tickets?departments%5B%5D=Support&status%5B%5D=Closed&show%5B%5D=inbox')



finally:
    # Close the WebDriver after a short delay to see the final page
    import time
    time.sleep(10000)  # Adjust this sleep time if you need more time to observe the final page
    # driver.quit()
