import customtkinter as ctk # type: ignore
import webbrowser
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class RBLXJoin(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Server Joiner")
        self.geometry("500x270") # U asked for code so i add some stuff :3, i think 500x270 looks best

        self.link_label = ctk.CTkLabel(self, text="Roblox Link:")
        self.link_label.pack(pady=10)

        self.link_entry = ctk.CTkEntry(self, width=450)
        self.link_entry.pack(pady=10)

        self.id_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.id_frame.pack(pady=10)

        self.place_id_label = ctk.CTkLabel(self.id_frame, text="Game ID:")
        self.place_id_label.grid(row=0, column=0, padx=10, pady=(0, 5))

        self.place_id_entry = ctk.CTkEntry(self.id_frame, width=200)
        self.place_id_entry.grid(row=1, column=0, padx=10)

        self.instance_id_label = ctk.CTkLabel(self.id_frame, text="Instance ID:")
        self.instance_id_label.grid(row=0, column=1, padx=10, pady=(0, 5))

        self.instance_id_entry = ctk.CTkEntry(self.id_frame, width=200)
        self.instance_id_entry.grid(row=1, column=1, padx=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear", command=self.clear_entry, width=120)
        self.clear_button.grid(row=0, column=0, padx=5)

        self.start_button = ctk.CTkButton(self.button_frame, text="Join", command=self.join_server, width=120)
        self.start_button.grid(row=0, column=1, padx=5)

        self.save_button = ctk.CTkButton(self.button_frame, text="Save", command=self.save_data, width=120)
        self.save_button.grid(row=0, column=2, padx=5)

        self.error_label = None

        self.load_save() #this shit took forever to do but yea

    def load_save(self): #ngl this temp saving is partly ai gen cause i didnt know how :sob:
        temp_file_path = r'C:\Windows\Temp\Join_data.json'
        if os.path.exists(temp_file_path):
            with open(temp_file_path, 'r') as f:
                data = json.load(f)
                self.link_entry.insert(0, data.get("link", ""))
                self.place_id_entry.insert(0, data.get("place_id", ""))
                self.instance_id_entry.insert(0, data.get("instance_id", ""))

    def save_data(self):
        temp_file_path = r'C:\Windows\Temp\Join_data.json'
        data = {
            "link": self.link_entry.get().strip(),
            "place_id": self.place_id_entry.get().strip(),
            "instance_id": self.instance_id_entry.get().strip(),
        }
        with open(temp_file_path, 'w') as f:
            json.dump(data, f)

    def join_server(self):
        link = self.link_entry.get().strip()

        if link.startswith("roblox://"):
            webbrowser.open(link)
            self.join_message("Joining server")
        else:
            place_id = self.place_id_entry.get().strip()
            instance_id = self.instance_id_entry.get().strip()

            if place_id:
                if instance_id:
                    roblox_link = f"roblox://placeId={place_id}&gameInstanceId={instance_id}"
                else:
                    roblox_link = f"roblox://placeId={place_id}"

                webbrowser.open(roblox_link)
                self.join_message("Joining server")
            else:
                self.error_message("Please use a valid link or Game ID :3")

        self.save_data()

    def clear_entry(self):
        self.link_entry.delete(0, 'end')
        self.place_id_entry.delete(0, 'end')
        self.instance_id_entry.delete(0, 'end')
        self.save_data()

    def error_message(self, message):
        if self.error_label is not None:
            self.error_label.destroy()
        self.error_label = ctk.CTkLabel(self, text=message, text_color="red")
        self.error_label.pack(pady=5)
        self.after(9000, self.remove_error)

    def join_message(self, message):
        if self.error_label is not None:
            self.error_label.destroy()
        self.error_label = ctk.CTkLabel(self, text=message, text_color="green")
        self.error_label.pack(pady=5)
        self.after(9000, self.remove_error) #error message also partly ai lol

    def remove_error(self):
        if self.error_label is not None:
            self.error_label.destroy()
            self.error_label = None

if __name__ == "__main__":
    app = RBLXJoin()
    app.mainloop()
