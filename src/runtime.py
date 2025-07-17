
# import online
import os, time, win32gui
from rich import print
from pypresence import Presence, InvalidID, DiscordNotFound

# import local
from src.constants import load_config

class AppRPC:
    def __init__(self):
        print("AppRPC loading..")
        self.first_time = True
        self.config = load_config()
        print(self.config)
        self.RPC = Presence(self.config["client_id"])
        self.start = time.time()

        self.current_window = None

    def check_if_client_id_valid(self, client_id):
        try:
            test_rpc = Presence(client_id)
            test_rpc.connect()
            print(f"[green]Client ID: {client_id} can be connected to.[/green]")
            test_rpc.close()
            return True
        except InvalidID:
            print(f"[red]Client ID {client_id} is not valid.[/red]")
            return False
        except Exception as e:
            print(f"[red]An error occurred: {e}[/red]")
            return False

    def connect(self):
        if not self.check_if_client_id_valid(self.config["client_id"]):
            exit(1)
        print("[blue]Connecting..")
        try:
            self.RPC.connect()
        except DiscordNotFound:
            print("[red]Discord is not open. Exiting..[/red]")
            time.sleep(3)
            exit(1)
        print("[green]Connected.[/green]")

    def get_current_window(self):
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    
    def update(self):
        window_title = self.get_current_window()
        if window_title == "":
            window_title = "Desktop"
        if not self.config["show_discord_chats"] and "discord" in window_title.lower():
            window_title = "Discord"
        if self.config["activate_excluded"] and any(excluded.lower() in window_title.lower() for excluded in self.config["excluded"]):
            for excluded in self.config["excluded"]:
                if excluded.lower() in window_title.lower():
                    window_title = excluded
                    break
        if self.current_window != window_title:
            self.current_window = window_title
        else:
            return
        # print("new window", self.current_window)
        details = f"Currently in {self.current_window}"
        state = self.config["state"]
        if self.first_time:
                self.RPC.update(
                details=details[:128],
                state=state[:128],
                start=self.start
            )
        else:
            self.RPC.update(
                details=details[:128],
                state=state[:128]
            )
        pass

    def run(self):
        self.connect()
        try:
            while True:
                self.update()
                print(f"[green]Connected to {self.config["client_id"]}.[/green]")
                print(f"[green]Current Window Shown:[/green] [yellow]{self.current_window}")
                time.sleep(5)
                os.system("cls")
        finally:
            print("[green]Program closed.[/green]")
            exit(0)