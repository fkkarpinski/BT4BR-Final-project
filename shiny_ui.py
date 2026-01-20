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
            background-color: #010A0F;    /*bacround*/
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
