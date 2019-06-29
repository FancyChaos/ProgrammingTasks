

# BUILTIN
import time

# SELENIUM
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains

def main():
    browserDriver = Firefox()
    weather(browserDriver)

    #hanoi(browserDriver)

def weather(browserDriver):
    browserDriver.get('https://www.wetter.de/')

    inputSearch  = browserDriver.find_element_by_css_selector("#search-header-input")
    inputSearch.send_keys("32052 herford")
    inputSearch.submit()

    time.sleep(5)

    browserDriver.get('https://www.wetteronline.de/wetter')

    inputSearch  = browserDriver.find_element_by_css_selector("#searchstring")
    inputSearch.send_keys("Herford 32052")
    inputSearch.submit()
    time.sleep(5)

    browserDriver.get('https://www.wetter.com/')

    inputSearch  = browserDriver.find_element_by_css_selector(".search-field")
    inputSearch.send_keys("32052 herford")

    time.sleep(0.5)
    suggestions = browserDriver.find_elements_by_css_selector(".autocomplete-suggestion")
    suggestions[0].click()

    time.sleep(5)


def hanoi(browserDriver):
    browserDriver.get('https://www.webgamesonline.com/towers-of-hanoi/')

    hoehe=8

    el = browserDriver.find_element_by_css_selector('select')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == str(hoehe):
            option.click() # select() in earlier versions of webdriver
            break

    time.sleep(1)

    place1 = browserDriver.find_element_by_css_selector("#c51")
    place2 = browserDriver.find_element_by_css_selector("#c52")
    place3 = browserDriver.find_element_by_css_selector("#c53")

    bewege(browserDriver,hoehe,place1,place2,place3,getDisks(browserDriver,hoehe),place1,place2,place3)

    time.sleep(5)

def bewege (browserDriver, hoehe, startPlatz, zwischenPlatz, zielPlatz,disks,place1,place2,place3):
    if hoehe > 0:
        bewege(browserDriver, hoehe-1, startPlatz, zielPlatz, zwischenPlatz,disks,place1,place2,place3)

        #verschiebe oberste Scheibe von a nach c

        if startPlatz == place1:
            listPlatzA=0
        if startPlatz == place2:
            listPlatzA=1
        if startPlatz == place3:
            listPlatzA=2

        if zielPlatz == place1:
            listPlatzC=0
        if zielPlatz == place2:
            listPlatzC=1
        if zielPlatz == place3:
            listPlatzC=2

        obersterPlatzA=0
        while obersterPlatzA<len(disks[0])-1 and disks[listPlatzA][obersterPlatzA] is None:
            obersterPlatzA+=1

        obersterPlatzC=0
        while obersterPlatzC<len(disks[2]) and disks[listPlatzC][obersterPlatzC] is None:
            obersterPlatzC+=1
        obersterPlatzC-=1

        dragDiskToPLace(browserDriver,disks[listPlatzA][obersterPlatzA],zielPlatz)

        disks[listPlatzC][obersterPlatzC] = disks[listPlatzA][obersterPlatzA]
        disks[listPlatzA][obersterPlatzA] = None

        bewege(browserDriver, hoehe-1, zwischenPlatz, startPlatz, zielPlatz,disks,place1,place2,place3)



def getDisks(browserDriver,hoehe):
    disks=[]
    for i in range(3):
        disks.append([])

    for i in range(hoehe):
        disks[0].append(browserDriver.find_element_by_css_selector("#I"+str(i+1)))
        disks[1].append(None)
        disks[2].append(None)

    return disks

def dragDiskToPLace(browserDriver,disk,place):
    touch = ActionChains(browserDriver)

    touch.click_and_hold(disk)
    touch.move_to_element(place)
    touch.release(disk)

    touch.perform()



if __name__ == '__main__':
    main()
