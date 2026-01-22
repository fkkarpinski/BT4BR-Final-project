from shiny import ui

def app_ui():
    # how to main window looks like, this is present on all screens
    # throughout the game
    return ui.page_fluid(
        ui.h1(ui.strong("🧬 placeholder_value")),
        ui.h2("placeholder_value"),
        ui.output_ui("screen"),
    )

def back_btn(can_back: bool):
    return ui.input_action_button("back", "<= Back") if can_back else None


# Screen builders
def screen_welcome():
    return ui.div(
        ui.div(
            ui.h1(
                "WELCOME",
                style="""
                    font-size: 130px;
                    font-weight: 300;
                    margin: 0;
                """
            ),
            ui.h3(
                "This game was developed as the final project for the",
                style="""
                    font-size: 20px;
                    font-weight: 150;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            ui.h3(
                "Basic Toolkit for Bioinformatics Research course (2025/2026).",
                style="""
                    font-size: 20px;
                    font-weight: 150;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            ui.h2(
                "To begin click here:",
                style="""
                    font-size: 25px;
                    font-weight: 170;
                    line-height: 1.1;
                    margin: 13px;
                    margin-top: 16vh;
                """
            ),
            style="""
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                margin-top: 18vh;
                color: #010A0F;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "START"),
            style="text-align: center;"
        )
    )


# main screen
def screen_main():
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
            ui.input_action_button("start_game", "Start a new paper"),
            style="text-align: center;"
        )
    )


# You are a science student
def screen_intro1():
    return ui.div(
        ui.div(
            ui.h1(
                "YOU ARE A SCIENCE STUDENT",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 200px;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 30vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: white;
            color: #010A0F;
            overflow: hidden;
        """
    )


# Science never sleeps
def screen_intro2():
    return ui.div(
        ui.div(
            ui.h1(
                "SCIENCE NEVER SLEEPS",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 200px;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 30vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #010A0F;
            color: white;
            overflow: hidden;
        """
    )


# And neither do you
def screen_intro3():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 30px;
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;
            """
        ),
        ui.div(
            ui.h1(
                "AND NEITHER DO YOU...",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 1vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #021824;
            color: #F5EB47;
            overflow: hidden;
        """
    )


# After a whole night of thinking
def screen_intro4():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 30px;
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;
            """
        ),
        ui.div(
            ui.h1(
                "AFTER A WHOLE NIGHT OF THINKING...",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 1vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #032F44;
            color: #F5EB47;
            overflow: hidden;
        """
    )


# You came up with an idea for your next research
def screen_intro5():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 30px;
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;
            """
        ),
        ui.div(
            ui.h1(
                "...YOU CAME UP WITH AN IDEA FOR YOUR ASSIGNMENT",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 1vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #054C70;
            color: #F5EB47;
            overflow: hidden;
        """
    )


# A new day is rising
def screen_intro6():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                gap: 30px;
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;
            """
        ),
        ui.div(
            ui.h1(
                "A NEW DAY IS RISING",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 1vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #076A9C;
            color: #F5EB47;
            overflow: hidden;
        """
    )


# It's time to start working
def screen_intro7():
    return ui.div(
        ui.div(
            ui.h1(
                "IT'S TIME TO START WORKING",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 200px;
                """
            ),
            style="""
                display: flex;
                justify-content: center;
                text-align: center;
                margin-top: 30vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #AFD3E6;
            color: #023A52;
            overflow: hidden;
        """
    )


# On your next publication
def screen_intro8():
    return ui.div(
        ui.div(
            ui.h1(
                "ON YOUR NEXT\n",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;
                    margin: 0;
                    color: #023A52;
                """
            ),
            ui.h1(
                "PROJECT",
                style="""
                    font-size: 80px;
                    font-weight: 900;
                    line-height: 1.1;
                    margin: 0;
                """
            ),
            style="""
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                margin-top: 50vh;
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #E7F6FE;
            color: #031F2B;
            overflow: hidden;
        """
    )

#All the screen builders
def screen_step1(can_back: bool):
    return ui.div(
        ui.h3(
            "1) You are interested in cancer gene expression - this is the focus of your paper. "
            "You want to prepare an exploratory analysis and a universal pipeline to help in your future works. "
            "How will you begin?",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),
        ui.div(
            ui.img(src="dumb_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),
        ui.div(
            ui.div(
                ui.p(
                    "Write an introduction where you explain your motivation and give some background regarding the data.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick1", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Get straight to work - don’t waste time on text that nobody reads anyways.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick2", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )
    
def screen_step2(can_back: bool):
    return ui.div(
        ui.div(
            ui.img(src="picture_q2.jpg", style="max-height: 280px; width: auto;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.h3(
            "2) You want to be able to reproduce the pipeline on other devices as well as be able to share it with your colleagues. In order to do so:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.div(
                ui.p(
                    "You include a set seed and session info in the code.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 75px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick3", "A", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "You write the code simultaneously on 3 devices and omit any additional info in the paper.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 75px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick4", "B", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
                margin-top: 30px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step3(can_back: bool):
    return ui.div(
        ui.div(
            ui.img(src="picture_q3.jpg", style="max-height: 280px; width: auto;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.h3(
            "3) In order to find interesting data you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Generate a synthetic dataset that mimics The Cancer Genome Atlas because your network only allows you to do so.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 98px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick5", "A", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Visit linked.in and ask your network where to obtain the data from.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 98px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick6", "B", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
                margin-top: 30px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step4(can_back: bool):
    return ui.div(
        ui.h3(
            "4) You obtained the data. The first thing that comes to your mind is to:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumber_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Start the work by generating several boxplots and trying to look for clues.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick7", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "You visualize the first few rows of your data and look for missing values.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick8", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step5(can_back: bool):
    return ui.div(
        ui.h3(
            "5) You were able to catch and take care of any null values. What you want to do now is:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumb_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Give up because the missing values completely ruined your mood.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick9", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Prepare basic summary statistics to better grasp the data.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick10", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step6(can_back: bool):
    return ui.div(
        ui.h3(
            "6) To analyse epigenetic patterns you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),
        ui.div(
            ui.div(
                ui.div(
                    ui.img(src="dumber_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "Generate some Venn diagrams to plot overlapping characteristics.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick11", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.div(
                    ui.img(src="dumb_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "You plot expression and methylation comparison using boxplots.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick12", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 40px auto;
                max-width: 700px;
            """
        ),
        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step7(can_back: bool):
    return ui.div(
        ui.h3(
            "7) To ensure your plots are uniform you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumb_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Perform standardisation and scale the values to Z-score.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick13", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Don’t care about such issues - in worst case your plots will be harder to read without glasses.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick14", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step8(can_back: bool):
    return ui.div(
        ui.h3(
            "8) To examine correlation analysis you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumber_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Calculate t-student test.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick15", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Calculate Spearman correlation.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick16", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step9(can_back: bool):
    return ui.div(
        ui.h3(
            "9) You obtained negative correlation - what do you do:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumb_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Discard the results - negative p-value is a mathematical error",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick17", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Accept the results - negative p-value suggests potential epigenetic silencing.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick18", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step10(can_back: bool):
    return ui.div(
        ui.h3(
            "10) To show intersections between sets you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),
        ui.div(
            ui.div(
                ui.div(
                    ui.img(src="dumber_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "Use UpSet plot as it is more read-friendly and supports bigger sets of data.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick19", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.div(
                    ui.img(src="dumb_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "Draw Venn diagram - reading from overlapping circles is easier and you can even colour them differently.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick20", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 40px auto;
                max-width: 700px;
            """
        ),
        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step11(can_back: bool):
    return ui.div(
        ui.h3(
            "11) To support the unusual UpSet plot you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),

        ui.div(
            ui.img(src="dumb_cat.jpg", style="max-width: 280px; height: 280px;"),
            style="""
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto 10px auto;
            """
        ),

        ui.div(
            ui.div(
                ui.p(
                    "Rely on the reader’s ability to google new things.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick21", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.p(
                    "Include a supportive interpretation below.",
                    style="""
                        margin: 0;
                        max-width: 300px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick22", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 20px auto 40px auto;
                max-width: 700px;
            """
        ),

        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

def screen_step12(can_back: bool):
    return ui.div(
        ui.h3(
            "12) To finish off your work you:",
            style="max-width: 900px; margin: 0 auto; white-space: pre-line;"
        ),
        ui.div(
            ui.div(
                ui.div(
                    ui.img(src="dumber_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "Present the findings in a table and note the key observations & add biological context.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick23", "a)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            ui.div(
                ui.div(
                    ui.img(src="dumb_cat.jpg", style="max-width: 250px; height: 250px;"),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.p(
                    "Write a two sentence summary, but most importantly include a „thank you for reading” image and attach links to your linked.in and orcid accounts.",
                    style="""
                        margin: 0;
                        max-width: 260px;
                        white-space: pre-line;
                        height: 110px;
                        overflow: auto;
                    """
                ),
                ui.input_action_button("pick24", "b)", style="height: 44px; min-width: 80px;"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    text-align: center;
                """
            ),
            style="""
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                justify-content: center;
                margin: 40px auto;
                max-width: 700px;
            """
        ),
        back_btn(can_back),
        style="text-align: center; min-height: 100vh;"
    )

#success screen
def screen_success(can_back: bool):
    return ui.div(
        ui.h3("SUCCESS"),
        ui.p("You just uploaded your first paper!"),
        ui.img(
            src="yay.jpg",
            style="max-width: 300px; height: auto; margin-top: 10px;",
        ),
        ui.div(
            ui.input_action_button("restart", "Back to main menu"),
            style="text-align: center; margin: 20px 0;"
        ),
        style="text-align: center; margin: 20px 0;",
    )
