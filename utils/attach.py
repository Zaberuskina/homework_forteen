import allure
from allure_commons.types import AttachmentType

def add_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=AttachmentType.PNG
    )

def add_logs(browser):
    allure.attach(
        '\n'.join(log['message'] for log in browser.driver.get_log('browser')),
        name='browser_logs',
        attachment_type=AttachmentType.TEXT
    )

def add_html(browser):
    allure.attach(
        browser.driver.page_source,
        name='page_source',
        attachment_type=AttachmentType.HTML
    )

def add_video(browser):
    video_url = f"https://selenoid.autotests.cloud/video/{browser.driver.session_id}.mp4"
    html = f"<html><body><video width='100%' height='100%' controls autoplay><source src='{video_url}' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')