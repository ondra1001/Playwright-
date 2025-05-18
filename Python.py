import pytest

URL = "https://engeto.cz/"

def test_konzultace(page):
    page.goto(URL)
    button = page.locator("#top-menu > li:nth-child(8) > a")
    button.click()
    button = page.locator("body > main > div:nth-child(1) > div > div > a")
    text = page.locator("#kontakt > div.form-company__head.flex.flex-column.gap-20.text-centered > h2")

    assert text.inner_text() == "S\xa0čím můžeme pomoct?"


def test_kurzy(page):
    page.goto(URL)
    button = page.locator("//*[@id='top-menu']/li[3]/a")
    button.hover()
    button = page.locator("//*[@id='top-menu']/li[3]/ul/li[2]/ul/li[1]/a/span")
    button.click()
    text = page.locator("main > div.full-page-width > div > div.flex-mobile-column > div > div.flex-column > h2")

    assert text.inner_text() == "Tester s\xa0Pythonem"

def test_nevalidni_prihlaseni(page):
    page.goto(URL)
    button = page.locator('//*[@id="main-header"]/div/div/a')
    button.click()
    button = page.locator('body > main > div > div > a')
    button.click()
    email = page.locator('//*[@id="username"]')
    email.fill("Tom")
    heslo = page.locator('//*[@id="password"]')
    heslo.fill("tom123")
    pokracovat = page.locator('body > div > main > section > div > div > div > form > div.c5d45fb63 > button')
    pokracovat.click()
    oznameni = page.locator('//*[@id="error-element-password"]')

    assert oznameni.inner_text() == "Nesprávný e-mail nebo heslo"
