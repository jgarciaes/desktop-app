import tkinter as tk

from .settings import settings
from .tracing import configure_tracing

tracer = configure_tracing("desktop-app")


def run_app() -> None:
    with tracer.start_as_current_span("desktop_app_main"):
        root = tk.Tk()
        root.title(f"Sample Desktop App v{settings.desktop_version}")
        label = tk.Label(
            root, text=f"Hello from Python Desktop App! Version: {settings.desktop_version}"
        )
        label.pack(padx=20, pady=20)
        root.mainloop()
