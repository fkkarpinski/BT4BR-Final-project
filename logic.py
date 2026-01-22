from shiny import reactive, ui

#collections of long data
INTRO_ORDER = [f"intro{x}" for x in range(1, 9)] #not faster, just shorter

GAME_FLOW = {
    "step1": ("pick1",  "step2"), 
    "step2": ("pick3",  "step3"),
    "step3": ("pick5",  "step4"),
    "step4": ("pick8",  "step5"),
    "step5": ("pick10",  "step6"),
    "step6": ("pick12", "step7"),
    "step7": ("pick13", "step8"),
    "step8": ("pick16", "step9"),
    "step9": ("pick18",  "step10"),
    "step10": ("pick19", "step11"),
    "step11": ("pick22", "step12"),
    "step12": ("pick23", "success"),
}

BAD_PICKS = [
    "pick2", "pick4",
    "pick6", "pick7",
    "pick9", "pick11",
    "pick14", "pick15",
    "pick17", "pick20",
    "pick21", "pick24",
]

def init_state():
    history = reactive.Value(["intro1"])
    intro_seen = reactive.Value(False)
    return history, intro_seen

#History handling to progress through screens
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

def reset(history, intro_seen):
    history.set(["welcome"])

# Event creators, logic handling
def bind_events(input, history, intro_seen):
    def reject():
        ui.notification_show(
            "Are you sure? Try again.",
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
    @reactive.event(input.rules_btn)
    def show_rules():
        ui.modal_show(
            ui.modal(
                ui.h3("Game rules"),
                ui.div(
                    ui.p("1. You are a bioinformatician and your goal is to conduct reproducible research."),
                    ui.p("2. In each step you must make a decision on what to include."),
                    ui.p("3. Wrong decisions get rejected by the supervising Professor."),
                    ui.p("4. Make the correct choices to launch successfully."),
                )
            )
        )

    @reactive.effect
    @reactive.event(input.start_game)
    def start_new_paper():
        if current(history) == "main":
            push(history, "step1")

    for step, (good_pick, next_step) in GAME_FLOW.items():
        btn = getattr(input, good_pick, None)
        if btn is None:
            continue

        @reactive.effect
        @reactive.event(btn)
        def ok(step=step, next_step=next_step):
            if current(history) == step:
                push(history, next_step)

    for pick in BAD_PICKS:
        btn = getattr(input, pick, None)
        if btn is None:
            continue

        @reactive.effect
        @reactive.event(btn)
        def bad(pick=pick):
            reject()

    @reactive.effect
    @reactive.event(input.restart)
    def restart():
        reset(history, intro_seen)