import os
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label
from textual.binding import Binding


MUSIC_DIR = "/run/media/nakazain/ES CAMPUR"
SUPPORTED_EXTENSIONS = (
    ".mp3",
    ".flac",
    ".wav",
    ".ogg",
    ".aac",
)

class MusicBrowser(App):

    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]


    def load_tracks(self) -> list[str]:
        tracks: list[str] = []

        if not os.path.exists(MUSIC_DIR):
            return tracks

        for dirpath, dirnames, filenames in os.walk(MUSIC_DIR):
            for filenames in os.listdir(dirpath):
                if filenames.endswith(SUPPORTED_EXTENSIONS):
                    tracks.append(filenames)

        tracks.sort()
        return tracks

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        self.tracks = self.load_tracks()

        self.list_view = ListView()
        yield self.list_view

        yield Footer()

    def on_mount(self) -> None:
        for track in self.tracks:
            label = Label(track)
            item = ListItem(label)
            self.list_view.append(item)

        if self.tracks:
            self.list_view.index = 0


if __name__ == "__main__":
    MusicBrowser().run()
