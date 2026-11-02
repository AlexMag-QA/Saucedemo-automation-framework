from selenium import webdriver


def create_driver(browser, headless, remote_url=None):
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }

        options.add_experimental_option("prefs", prefs)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if remote_url:
        return webdriver.Remote(
            command_executor=remote_url,
            options=options,
        )

    if browser == "chrome":
        return webdriver.Chrome(options=options)

    return webdriver.Firefox(options=options)