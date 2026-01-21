from pathlib import Path
from shiny import App, render

import shiny_ui as pages
import logic

app_ui = pages.app_ui()

def server(input, output, session):
    history, chosen_topic, intro_seen = logic.init_state()
    logic.bind_events(input, history, chosen_topic, intro_seen)

    @output
    @render.ui
    def screen():
        s = logic.current(history)
        back = logic.can_back(history)
        topic = chosen_topic.get()

        ROUTES = {
            #intro section
            "intro1": lambda: pages.screen_intro1(),
            "intro2": lambda: pages.screen_intro2(),
            "intro3": lambda: pages.screen_intro3(),
            "intro4": lambda: pages.screen_intro4(),
            "intro5": lambda: pages.screen_intro5(),
            "intro6": lambda: pages.screen_intro6(),
            "intro7": lambda: pages.screen_intro7(),
            "intro8": lambda: pages.screen_intro8(),

            #main menu
            "welcome": lambda: pages.screen_welcome(),
            "main":   lambda: pages.screen_main(),

            #game flow
            "topic":   lambda: pages.screen_topic(back),
            "step1":   lambda: pages.screen_step1(back, topic),
            "step2":   lambda: pages.screen_step2(back, topic),
            "step3":   lambda: pages.screen_step3(back, topic),
            "step4":   lambda: pages.screen_step4(back, topic),
            "step5":   lambda: pages.screen_step5(back, topic),
            "step6":   lambda: pages.screen_step6(back, topic),
            "step7":   lambda: pages.screen_step7(back, topic),
            "step8":   lambda: pages.screen_step8(back, topic),
            "success": lambda: pages.screen_success(back, topic),
        }

        return ROUTES.get(s, lambda: pages.screen_welcome())()

app_dir = Path(__file__).parent
app = App(app_ui, server, static_assets=app_dir / "www")