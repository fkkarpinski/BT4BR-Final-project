from shiny import reactive, ui

def init_state():
    history = reactive.Value(["welcome"])
    chosen_topic = reactive.Value(None)
    return history, chosen_topic

#History helpers
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

def reset(history, chosen_topic):
    history.set(["welcome"])
    chosen_topic.set(None)

#Event handlers
def bind_events(input, history, chosen_topic):

    @reactive.effect
    @reactive.event(input.next0)
    def to_topic():
        push(history, "topic")

    @reactive.effect
    @reactive.event(input.back)
    def back():
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
                easy_close=True,
            )
        )

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
        reset(history, chosen_topic)