import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Configure Chrome options
options = Options()
options.add_argument("--start-maximized")  # Start the browser maximized
options.add_argument("--disable-extensions")
options.add_argument("--headless")  # Optional: To run the browser in the background (no UI)

# Set path to ChromeDriver
service = Service('path_to_chromedriver')  # e.g., "C:/path_to/chromedriver.exe"
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Go to the Ticketmaster website
driver.get('https://www.ticketmaster.com')

# Step 2: Search for "Taylor Swift"
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Taylor Swift')
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for search results to load

# Step 3: Click on the first available show
# We assume the first link is the show you're interested in (this can be adjusted depending on the site structure)
first_show = driver.find_element(By.XPATH, '(//div[contains(@class, "event-card")])[1]')
first_show.click()

time.sleep(3)  # Wait for the event page to load

# Step 4: Check for queue and join if available
def check_and_join_queue():
    try:
        # Check if the queue button is present (assuming a "Join Queue" button exists)
        join_button = driver.find_element(By.XPATH, '//button[contains(text(), "Join Queue")]')
        if join_button.is_displayed():
            print("Queue is available. Joining the queue...")
            join_button.click()
            time.sleep(5)  # Wait for the page to load after joining the queue
            return True
    except Exception as e:
        print("Queue not found, refreshing...")
        return False

# Keep refreshing until queue is available
queue_available = False
while not queue_available:
    queue_available = check_and_join_queue()
    if not queue_available:
        driver.refresh()  # Refresh the page to try again
        time.sleep(5)  # Wait before trying again

# Step 5: Go to buy tickets page
print("Queue joined. Proceeding to buy tickets...")
# Assuming we are now on the ticket purchasing page (modify as necessary)
# You can replace the following line with any specific actions for buying tickets
# e.g., select ticket quantity, add to cart, etc.
time.sleep(5)  # Wait for any transitions
buy_button = driver.find_element(By.XPATH, '//button[contains(text(), "Buy Tickets")]')
buy_button.click()

# Close the browser after completing the task
time.sleep(5)  # Wait for the page to load
driver.quit()
