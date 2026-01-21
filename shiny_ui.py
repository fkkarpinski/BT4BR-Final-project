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
                    line-height: 1.1;   /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            ui.h3(
                "Basic Toolkit for Bioinformatics Research course (2025/2026).",
                style="""
                    font-size: 20px;
                    font-weight: 150;
                    line-height: 1.1;   /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            ui.h2(
                "To begin click here:",
                style="""
                    font-size: 25px;
                    font-weight: 170;
                    line-height: 1.1;   /*vertical space between lines of the text*/
                    margin: 13px;  /*Deleting the margin of the header*/
                    margin-top: 16vh;   /*Adjusting the posision vertically*/
                """
            ),
            style="""
                display: flex;
                flex-direction: column; /*So the texts can be under each other*/
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 18vh;   /*Adjusting the posision vertically*/
                color: #010A0F;
            """
        ),

        ui.div(
            ui.input_action_button("next0", "START"),
            style="text-align: center;"
        )
    )
    
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
            ui.input_action_button("go_topic", "Start a new paper"),
            style="text-align: center;"
        )
    )

#You are a scientist
def screen_intro1():
    return ui.div(
        ui.div(
            ui.h1(
                "YOU ARE A\nSCIENTIST",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 200px;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 30vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: white;    /*bacround*/
            color: #010A0F;   /*color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#Science never sleeps
def screen_intro2():
    return ui.div(
        ui.div(
            ui.h1(
                "SCIENCE NEVER SLEEPS",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 200px;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 30vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #010A0F;    /*background*/
            color: white;   /*color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#And neither do you
def screen_intro3():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;  /*To have the squeres in rows and columns*/
                grid-template-columns: 1fr 1fr;     /*two identical columns*/
                grid-template-rows: 1fr 1fr;        /*two identical rows*/
                gap: 30px;                 /*the window "frame"*/
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;  /*top right bottom left*/
            """
        ),
        ui.div(
            ui.h1(
                "AND NEITHER DO YOU...",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 1vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #021824;    /*bacround*/
            color: #F5EB47;   /*color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#After a whole night of thinking
def screen_intro4():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;  /*To have the squeres in rows and columns*/
                grid-template-columns: 1fr 1fr;     /*two identical columns*/
                grid-template-rows: 1fr 1fr;        /*two identical rows*/
                gap: 30px;                 /*the window "frame"*/
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;  /*top right bottom left*/
            """
        ),
        ui.div(
            ui.h1(
                "AFTER A WHOLE NIGHT OF THINKING...",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 1vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #032F44;    /*bacround*/
            color: #F5EB47;   /*color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#You came up with an idea for your next research
def screen_intro5():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;  /*To have the squeres in rows and columns*/
                grid-template-columns: 1fr 1fr;     /*two identical columns*/
                grid-template-rows: 1fr 1fr;        /*two identical rows*/
                gap: 30px;                 /*the window "frame"*/
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;  /*top right bottom left*/
            """
        ),
        ui.div(
            ui.h1(
                "...YOU CAME UP WITH AN IDEA FOR YOUR NEXT RESEARCH",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 1vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #054C70;    /*bacround*/
            color: #F5EB47;   /*Color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#A new day is rising
def screen_intro6():
    return ui.div(
        ui.div(
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            ui.div(style="background: #F5EB47;"),
            style="""
                display: grid;  /*To have the squeres in rows and columns*/
                grid-template-columns: 1fr 1fr;     /*two identical columns*/
                grid-template-rows: 1fr 1fr;        /*two identical rows*/
                gap: 30px;                 /*the window "frame"*/
                width: 200px;
                height: 200px;
                margin: 20vh auto 10vh auto;  /*top right bottom left*/
            """
        ),
        ui.div(
            ui.h1(
                "A NEW DAY IS RISING",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 1vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #076A9C;    /*bacround*/
            color: #F5EB47;   /*Color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

#It's time to start working
def screen_intro7():
    return ui.div(
        ui.div(
            ui.h1(
                "IT'S TIME TO START WORKING",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 200px;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 30vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #AFD3E6;    /*bacround*/
            color: #023A52;   /*color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )
    
#On your next publication
def screen_intro8():
    return ui.div(
        ui.div(
            ui.h1(
                "ON YOUR NEXT\n",
                style="""
                    font-size: 40px;
                    font-weight: 200;
                    line-height: 1.1;  /*vertical space between lines of the text*/
                    margin: 0;
                    color: #023A52;
                """
            ),
            ui.h1(
                "PUBLICATION",
                style="""
                    font-size: 80px;
                    font-weight: 900;
                    line-height: 1.1;   /*vertical space between lines of the text*/
                    margin: 0;  /*Deleting the margin of the header*/
                """
            ),
            style="""
                display: flex;
                flex-direction: column; /*So the texts to be under each other*/
                justify-content: center;    /*Centering the header horizontally*/
                text-align: center;
                margin-top: 50vh;   /*Adjusting the posision vertically*/
            """
        ),
        ui.div(
            ui.input_action_button("next0", "Next"),
            #The button is supposed to stay at bottom right
            style="""
                position: fixed;
                bottom: 20px;
                right: 20px;
            """
        ),
        style="""
            position: fixed;    /*It covers the WHOLE page */
            top: 0;     /*from hight top */
            left: 0;    /*from far left */
            width: 100%;    /*full width */
            height: 100%;   /*full height */
            background-color: #E7F6FE;    /*bacround*/
            color: #031F2B;   /*Color of the writing */
            overflow: hidden;   /*Removes scroll bars even if something goes off screen.*/
        """
    )

def screen_topic(can_back: bool):
    return ui.div(
        ui.div(
            ui.h3("Choose the topic of your interest:"),
            ui.img(
                src="dumb_cat.jpg",
                style="max-width: 300px; height: auto;"
            ),
            
            ui.div(
                ui.input_select(
                    "topic_select",
                    "",
                    choices=["a", "b", "c"],
                ),
                style="max-width: 300px; margin: 20px auto;"
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
        ui.h3("Step 1"),
        ui.p(f"Chosen topic: {chosen_topic}"),
        ui.p("Choose between option 1 and option 2."),

        ui.div(
            ui.div(
                ui.div(
                    ui.img(
                        src="dumb_cat.jpg",
                        style="max-width: 250px; height: 250px;"
                    ),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.input_action_button("pick1", "1"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 25px;
                """
            ),
            ui.div(
                ui.div(
                    ui.img(
                        src="dumber_cat.jpg",
                        style="max-width: 250px; height: 250px;"
                    ),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.input_action_button("pick2", "2"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 25px;
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

def screen_step2(can_back: bool, chosen_topic: str | None):
    return ui.div(
        ui.h3("Step 2"),
        ui.p(f"Chosen topic: {chosen_topic}"),
        ui.p("Choose between option 3 and option 4."),

        ui.div(
            ui.div(
                ui.div(
                    ui.img(
                        src="dumber_cat.jpg",
                        style="max-width: 250px; height: 250px;"
                    ),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.input_action_button("pick3", "3"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 25px;
                """
            ),
            ui.div(
                ui.div(
                    ui.img(
                        src="dumb_cat.jpg",
                        style="max-width: 250px; height: 250px;"
                    ),
                    style="""
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    """
                ),
                ui.input_action_button("pick4", "4"),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 25px;
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

def screen_success(can_back: bool, chosen_topic: str | None):
    return ui.div(
        ui.h3("SUCCESS"),
        ui.p(f"You just uploaded your first paper on {chosen_topic}"),
        ui.img(
            src="yay.jpg",
            style="max-width: 300px; height: auto; margin-top: 10px;",
        ),        
        ui.div(
            ui.input_action_button("restart", "Start again"),
            style="text-align: center; margin: 20px 0;"
        ),
        style="text-align: center; margin: 20px 0;",
    )
