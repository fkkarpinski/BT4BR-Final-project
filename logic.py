from shiny import reactive, ui

INTRO_ORDER = [f"intro{x}" for x in range(1, 9)]


GAME_FLOW = {
    "step1": ("pick1",  "step2"), 
    "step2": ("pick4",  "step3"),
    "step3": ("pick5",  "step4"),
    "step4": ("pick8",  "step5"),
    "step5": ("pick9",  "step6"),
    "step6": ("pick12", "step7"),
    "step7": ("pick13", "step8"),
    "step8": ("pick16", "success"),
}

BAD_PICKS = [
    "pick2", "pick3",
    "pick6", "pick7",
    "pick10", "pick11",
    "pick14", "pick15",
]

def init_state():
    history = reactive.Value(["intro1"])
    chosen_topic = reactive.Value(None)
    intro_seen = reactive.Value(False)
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
    history.set(["welcome"])

def bind_events(input, history, chosen_topic, intro_seen):
    def reject():
        ui.notification_show(
            "Peer review: rejected (wrong choice). Try again.",
            type="error",
            duration=3,
        )

    @reactive.effect
    @reactive.event(input.next0)
    def next0():
        s = current(history)

        if s in INTRO_ORDER:
            i = INTRO_ORDER.index(s)
            if i < len(INTRO_ORDER) - 1:
                push(history, INTRO_ORDER[i + 1])
            else:
                intro_seen.set(True)
                push(history, "welcome")
            return

        if s == "welcome":
            push(history, "main")
            return

    @reactive.effect
    @reactive.event(input.back)
    def back():
        s = current(history)
        if s in INTRO_ORDER:
            return
        if len(history.get()) <= 1:
            return

        pop(history)

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
    @reactive.event(input.rules_btn)
    def show_rules():
        ui.modal_show(
            ui.modal(
                ui.h3("Game rules"),
                ui.div(
                    ui.p("1. Choose the desired topic of your paper."),
                    ui.p("2. In each step you must make a decision."),
                    ui.p("3. Wrong decisions get rejected by peer review."),
                    ui.p("4. Make the correct choices to publish successfully."),
                )
            )
        )

    for step, (good_pick, next_step) in GAME_FLOW.items():
        btn = getattr(input, good_pick, None)
        if btn is None:
            continue

        @reactive.effect
        @reactive.event(btn)
        def _ok(step=step, next_step=next_step):
            if current(history) == step:
                push(history, next_step)

    for pick in BAD_PICKS:
        btn = getattr(input, pick, None)
        if btn is None:
            continue

        @reactive.effect
        @reactive.event(btn)
        def _bad(pick=pick):
            reject()

    @reactive.effect
    @reactive.event(input.restart)
    def restart():
        reset(history, chosen_topic, intro_seen)