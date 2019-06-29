

# BUILTIN
import time

# SELENIUM
from selenium.webdriver import Firefox

def main():
    #get the webdriver
    browserDriver = Firefox()

    #go to google
    browserDriver.get('https://www.google.de')

    #find the Search Input Element
    inputSearch  = browserDriver.find_element_by_css_selector(".gLFyf.gsfi")
    #type "do a barrel role"
    inputSearch.send_keys("do a barrel roll")
    #start the search by submitting the input
    inputSearch.submit()

if __name__ == '__main__':
    main()
