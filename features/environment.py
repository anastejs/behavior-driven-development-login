# behave не поддерживает fixtures как в pytest, но можно использовать hooks для выполнения кода до и после каждого сценария

from playwright.sync_api import sync_playwright


# запускаем playwright -> открываем браузер -> создаем новую страницу -> сохраняем все в context
def before_scenario(context, _):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    context.page = context.browser.new_page()

# закрываем браузер -> останавливаем playwright
def after_scenario(context, _):
    context.browser.close()
    context.playwright.stop()