from shiny import ui

def app_ui():
# how to main window looks like, this is present on all screens
# throughout the game
    return ui.page_fluid(
        ui.h1(ui.strong("🧬 Publish or Perish")),
        ui.h2("A Peer-Review Simulation Game"),
        ui.output_ui("screen"),
    )

def back_btn(can_back: bool):
    return ui.input_action_button("back", "<= Back") if can_back else None

#Screen builders
def screen_welcome():
    return ui.div(
        ui.div(
            ui.img(
                src="dumb_cat.jpg",
                style="max-width: 300px; height: auto;"
            ),
            style="text-align: center; margin: 20px 0;"
        ),

        ui.div(
            ui.input_action_button("rules_btn", "Rules"),
            ui.input_action_button("next0", "Let's begin!"),
            style="text-align: center;"
        )
    )

def screen_topic(can_back: bool):
    return ui.div(
        ui.h3("Wybierz temat pracy"),

        ui.div(
            ui.img(
                src="dumb_cat.jpg",
                style="max-width: 300px; height: auto;"
            ),
            
            ui.div(
                ui.input_select(
                    "topic_select",
                    "Temat:",
                    choices=["a", "b", "c"],
                ),
                style="max-width: 400px; margin: 0 auto;"
            ),
            
            ui.div(
                back_btn(can_back),
                ui.input_action_button("topic_ok", "Next"),
                style="margin-top: 10px;"
            ),
            style="text-align: center; margin: 20px 0;"
        )        
    )

def screen_step1(can_back: bool, chosen_topic: str | None):
    return ui.div(
        ui.h3("Krok 1"),
        ui.p(f"Wybrany temat: {chosen_topic}"),
        ui.p("Wybierz 1 lub 2."),
        
        ui.div(
            ui.div(
                ui.img(
                    src="dumb_cat.jpg",
                    style="max-width: 300px; height: auto; margin-top: 10px;"
                ),
                ui.input_action_button("pick1", "1")
            ),
        
            ui.div(
                ui.img(
                    src="dumber_cat.jpg",
                    style="max-width: 300px; height: auto; margin-top: 10px;"
                ),
                ui.input_action_button("pick2", "2"),
            ),
        back_btn(can_back),
        style="text-align: center; margin: 20px 0;"
        )  
    )

def screen_step2(can_back: bool, chosen_topic: str | None):
    return ui.div(
        
        ui.h3("Krok 2"),
        ui.p(f"Wybrany temat: {chosen_topic}"),
        ui.p("Wybierz 3 lub 4."),
        
        ui.div(
            ui.div(
                ui.img(
                    src="dumber_cat.jpg",
                    style="max-width: 300px; height: auto; margin-top: 10px;"
                ),
                ui.input_action_button("pick3", "3")
            ),
        
            ui.div(
                ui.img(
                    src="dumb_cat.jpg",
                    style="max-width: 300px; height: auto; margin-top: 10px;"
                ),
                ui.input_action_button("pick4", "4"),
            ),
        back_btn(can_back),
        style="text-align: center; margin: 20px 0;"
        )  
    )

def screen_success(can_back: bool, chosen_topic: str | None):
    return ui.div(
        ui.h3("SUCCESS"),
        ui.p(f"You just uploaded your first paper on {chosen_topic}"),
        ui.img(
            src="yay.jpg",
            style="max-width: 300px; height: auto; margin-top: 10px;",
        ),        
        ui.div(
            ui.input_action_button("restart", "start again"),
            style="text-align: center; margin: 20px 0;"
        ),
        style="text-align: center; margin: 20px 0;",
    )