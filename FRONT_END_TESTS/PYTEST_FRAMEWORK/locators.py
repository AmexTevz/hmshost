from selenium.webdriver.common.by import By


class FirstPageLocators:
    SMASH_BURGER = (By.XPATH, "//h1[contains(.,'Smash Burger®')]")
    SMASH_BURGER_TITLE = (By.XPATH,"//h2[contains(.,'Smash Burger®')]")
    BACON_CHEESEBURGER = (By.XPATH, "//h3[contains(.,'Bacon Cheeseburger')]")

    MAYO = (By.XPATH, "//label[@for='208910004-2'][contains(.,'Mayo')]")
    LETTUCE = (By.XPATH, "//label[@for='208914002-2'][contains(.,'Lettuce')]")
    BEEF_PATTY = (By.XPATH, "(//label[contains(.,'Single Beef Patty')])[2]")
    DOUBLE_BEEF_PATTY = (By.XPATH, "(//label[contains(.,'Double Beef Patty')])[1]")
    CLASSIC_BUN = (By.XPATH, "//label[contains(.,'Classic Bun')]")
    ADD_TO_CART = (By.CSS_SELECTOR, "button#AddItem")
    GO_TO_CART = (By.XPATH, "//i[contains(.,'A')]")
    PAY_NOW = (By.CSS_SELECTOR, "button#PayNow")
    FIRST_NAME = (By.CSS_SELECTOR, "input#inputNameOnCard")
    PAY_BUTTON = (By.CSS_SELECTOR, "button#btnPay")
    THANK_YOU_MASSAGE = (By.CSS_SELECTOR, "//p[contains(.,'Thanks, your payment is complete')]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input#Email")
    EMAIL_SEND_BUTTON = (By.CSS_SELECTOR, "button#EmailReceipt")


    POP_UP_BUTTON = (By.CSS_SELECTOR, "button#CookiePrefencesModalButton")










