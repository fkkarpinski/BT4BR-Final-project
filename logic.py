from shiny import reactive, ui

INTRO_ORDER = ["intro1", "intro2", "intro3", "intro4", "intro5", "intro6", "intro7", "intro8"]

def init_state():
    history = reactive.Value(["intro1"])
    chosen_topic = reactive.Value(None)
    intro_seen = reactive.Value(False) #check for intro
    return history, chosen_topic, intro_seen

def current(history):
    return history.get()[-1]

def can_back(history) -> bool:
    return len(history.get()) > 1

def push(history, screen: str):
    h = history.get().copy()
    h.append(screen)
    history.set(h)

def pop(history):
    h = history.get().copy()
    if len(h) > 1:
        h.pop()
        history.set(h)

def reset(history, chosen_topic, intro_seen):
    chosen_topic.set(None)
    if intro_seen.get():
        history.set(["main"])
    else:
        history.set(["intro1"])

#Event handlers
def bind_events(input, history, chosen_topic, intro_seen):
    #next button
    @reactive.effect
    @reactive.event(input.next0)
    def next0():
        s = current(history)
        #intro flow
        if s in INTRO_ORDER:
            i = INTRO_ORDER.index(s)
            if i < len(INTRO_ORDER) - 1:
                push(history, INTRO_ORDER[i + 1])
            else:
                intro_seen.set(True)
                push(history, "main")
            return
        
    @reactive.effect
    @reactive.event(input.back)
    def back():
        if current(history) in INTRO_ORDER:
            return
        pop(history)

    @reactive.effect
    @reactive.event(input.rules_btn)
    def show_rules():
        ui.modal_show(
            ui.modal(
                ui.h3("Game rules"),
                ui.div(
                    ui.p("1. Choose the desired topic of your paper."),
                    ui.p("2. During each step you will have to make decisions regarding the course of your work."),
                    ui.p("3. Watch out for the evil peer review!"),
                    ui.p("4. Make correct choices to publish successfully."),
                    ui.p("5. Good luck!"),
                ),
            )
        )

    @reactive.effect
    @reactive.event(input.go_topic)
    def go_topic():
        push(history, "topic")

    @reactive.effect
    @reactive.event(input.topic_ok)
    def topic_ok():
        chosen_topic.set(input.topic_select())
        push(history, "step1")

    @reactive.effect
    @reactive.event(input.pick1)
    def pick1_ok():
        push(history, "step2")

    @reactive.effect
    @reactive.event(input.pick2)
    def pick2_bad():
        ui.notification_show(
            "Peer review: rejected (zła opcja). Spróbuj ponownie.",
            type="error",
            duration=3,
        )

    @reactive.effect
    @reactive.event(input.pick4)
    def pick4_ok():
        push(history, "success")

    @reactive.effect
    @reactive.event(input.pick3)
    def pick3_bad():
        ui.notification_show(
            "Peer review: rejected (zła opcja). Spróbuj ponownie.",
            type="error",
            duration=3,
        )

    @reactive.effect
    @reactive.event(input.restart)
    def restart():
        reset(history, chosen_topic, intro_seen)