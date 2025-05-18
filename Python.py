import pytest

def test_title_page(page):
    page.goto("https://www.google.com/")
    title = page.locator("title")
    assert title.inner_text() == "Google"