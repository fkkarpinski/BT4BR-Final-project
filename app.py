from pathlib import Path
from shiny import App, render

import shiny_ui as pages
import logic

app_ui = pages.app_ui()

#server activity
def server(input, output, session):
    history, intro_seen = logic.init_state()
    logic.bind_events(input, history, intro_seen)

    @output
    @render.ui
    def screen():
        s = logic.current(history)
        back = logic.can_back(history)

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
            "step1":   lambda: pages.screen_step1(back),
            "step2":   lambda: pages.screen_step2(back),
            "step3":   lambda: pages.screen_step3(back),
            "step4":   lambda: pages.screen_step4(back),
            "step5":   lambda: pages.screen_step5(back),
            "step6":   lambda: pages.screen_step6(back),
            "step7":   lambda: pages.screen_step7(back),
            "step8":   lambda: pages.screen_step8(back),
            "step9":   lambda: pages.screen_step9(back),
            "step10":   lambda: pages.screen_step10(back),
            "step11":   lambda: pages.screen_step11(back),
            "step12":   lambda: pages.screen_step12(back),
            
            #success
            "success": lambda: pages.screen_success(back),
        }

        return ROUTES.get(s, lambda: pages.screen_welcome())()

#line to fix no image bug
app_dir = Path(__file__).parent

#app
app = App(app_ui, server, static_assets=app_dir / "www")