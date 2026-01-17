from pathlib import Path
from shiny import App, render, ui

import ui as pages
import logic

app_ui = pages.app_ui()

def server(input, output, session):

    history, chosen_topic = logic.init_state()
    logic.bind_events(input, history, chosen_topic)

    @output
    @render.ui
    def screen():
        s = logic.current(history)
        back = logic.can_back(history)
        topic = chosen_topic.get()

        ROUTES = {
            "welcome": lambda: pages.screen_welcome(),
            "topic":   lambda: pages.screen_topic(back),
            "step1":   lambda: pages.screen_step1(back, topic),
            "step2":   lambda: pages.screen_step2(back, topic),
            "success": lambda: pages.screen_success(back, topic),
        }

        return ROUTES.get(s, lambda: pages.screen_welcome())()

app_dir = Path(__file__).parent
app = App(app_ui, server, static_assets=app_dir / "www")
