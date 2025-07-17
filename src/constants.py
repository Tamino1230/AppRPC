
import json
import os
from rich import print

default_data = {
    "client_id": 1334932480066715769,
    "show_discord_chats": False,
    "show_websites": False,
    "your_browsers": [
        "Chrome",
        "Firefox",
        "Safari",
        "Edge",
        "Brave",
        "Opera"
    ],
    "state": "Get on github.com/Tamino1230/AppRPC"
}

def create_config_file_with_default_settings(folder_path = "config", file = "config.json"):
    try:
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        with open(f"{folder_path}/{file}", "w") as f:
            f.write(json.dumps(default_data, indent=4))
        print("[green]Created new File successfully[/green]")
    except Exception as e:
        print(e)
        print(f"[red]An error accured while creating the new config file.[/red]")
        exit(1)

def load_config(path=r"./config/config.json"):
    # to avoid errors
    data = default_data
    #* Open JSON File
    try:
        with open(path, "r") as file:
            data = json.load(file)
            # print(data)
    except FileNotFoundError:
        print(f"[red]Config file was not found in path: {path}[/red]")
        print("Using default settings.")
        create_config_file_with_default_settings()
    except Exception as e:
        print("[red]An exception appeared:", e, "[/red]")
        print("Using default settings.")
        exit(1)
    finally:
        return data
    
def reset_config(path=r"./config/config.json"):
    data = default_data
    try:
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"[red]Config file was not found in path: {path}[/red]")
        create_config_file_with_default_settings()
    except Exception as e:
        print("[red]An exception appeared:", e, "[/red]")
        exit(1)

def save_config(data, path=r"./config/config.json"):
    try:
        with open(path, "w") as file:
            file.write(data)
    except FileNotFoundError:
        print(f"[red]Config file was not found in path: {path}[/red]")
        create_config_file_with_default_settings()
    except Exception as e:
        print("[red]An exception appeared:", e, "[/red]")
        exit(1)