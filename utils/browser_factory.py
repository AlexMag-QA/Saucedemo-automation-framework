from selenium import webdriver


def create_driver(browser, headless):
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)

        return driver

    else:
        raise ValueError(f"Unsupported browser: {browser}")