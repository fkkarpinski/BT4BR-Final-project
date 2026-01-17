from shiny import reactive, ui

def init_state():
    #Inicjalizacja stanu gry
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
    def _to_topic():
        push(history, "topic")

    @reactive.effect
    @reactive.event(input.back)
    def _back():
        pop(history)

    @reactive.effect
    @reactive.event(input.topic_ok)
    def _topic_ok():
        chosen_topic.set(input.topic_select())
        push(history, "step1")

    @reactive.effect
    @reactive.event(input.pick1)
    def _pick1_ok():
        push(history, "step2")

    @reactive.effect
    @reactive.event(input.pick2)
    def _pick2_bad():
        ui.notification_show(
            "Peer review: rejected (zła opcja). Spróbuj ponownie.",
            type="error",
            duration=3,
        )

    @reactive.effect
    @reactive.event(input.pick4)
    def _pick4_ok():
        push(history, "success")

    @reactive.effect
    @reactive.event(input.pick3)
    def _pick3_bad():
        ui.notification_show(
            "Peer review: rejected (zła opcja). Spróbuj ponownie.",
            type="error",
            duration=3,
        )

    @reactive.effect
    @reactive.event(input.restart)
    def _restart():
        reset(history, chosen_topic)