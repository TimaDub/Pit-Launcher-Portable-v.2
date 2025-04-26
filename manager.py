# Copyright (c) 2024, [Tymofii Dubovyi]
# Licensed under the MIT License.
# See LICENSE file for details.

from os import path, mkdir, rename
from datetime import datetime
from msgspec import json, Struct, DecodeError
from typing import List
from minecraft_launcher_lib.utils import get_minecraft_directory
import resources
from PyQt6.QtCore import QFile, QIODevice


class SaveStruct(Struct):
    name: str
    background_color: str
    text_color: str
    button_color: str
    progress_bar_color: str
    progress_bar_text_color: str
    selected_tab_color: str
    selected_tab_background_color: str


class Saver(Struct):
    styles: List[SaveStruct]


class Manager:
    def __init__(
        self,
        directory: str = get_minecraft_directory().replace("minecraft", "pitLauncher"),
        logs_path: str = ".pit_logs",
        app_path: str = ".pit",
        properties_path: str = "launcher_properties.json",
        assets_path: str = ":/assets/",
        images_path: str = ":/assets/images/",
        fonts_path: str = ":/assets/fonts/",
        base_style_name: str = "styles.json",
        logo_path: str = "logo.png",
        main_icon_path: str = "icon.ico",
        main_font_path: str = "main_font.ttf",
        sub_font_path: str = "sub_font.ttf",
        window_size=(600, 450),
        main_font_size=12,
        sub_font_size=20,
    ):
        self.minecraft_directory = directory
        self.launcher_properties_path = path.join(
            self.minecraft_directory, properties_path
        )
        self.window_size = window_size
        self.images_path = images_path
        self.fonts_path = fonts_path
        self.sub_font_size = sub_font_size
        self.main_font_size = main_font_size
        self.assets_folder = assets_path
        self.logs_path = path.join(self.minecraft_directory, logs_path)
        self.workspace_path = path.join(self.minecraft_directory, app_path)
        self.base_style_path: str = path.join(self.assets_folder, base_style_name)
        self.styles_path = path.join(self.workspace_path, "styles")
        #
        self.logo_path = path.join(self.images_path, logo_path)
        self.main_icon_path = path.join(self.images_path, main_icon_path)
        self.main_font_path = path.join(self.fonts_path, main_font_path)
        self.sub_font_path = path.join(self.fonts_path, sub_font_path)
        #
        self.time_start = datetime.now()
        #
        self.check(
            [
                self.minecraft_directory,
                self.workspace_path,
                self.logs_path,
                self.styles_path,
            ]
        )
        try:
            with open(self.launcher_properties_path, "x"):
                ...
        except FileExistsError:
            self.log(["Json exists"])
            # print("Json exists")

    def load_styles(self):
        file = QFile(self.base_style_path)
        if not file.open(QIODevice.OpenModeFlag.ReadOnly):
            self.log(["Error: can't open the file"])
            # print("Ошибка: не удалось открыть файл")
            return None

        data = file.readAll().data().decode("utf-8")
        file.close()
        return json.decode(data, type=Saver).styles

    def load(self, arg):
        try:
            with open(self.launcher_properties_path, "br") as launcher_properties:
                properties = json.decode(launcher_properties.read())
                return properties[arg]
        except DecodeError:
            self.log(["Error in loading: " + arg])
            return None
        except KeyError:
            self.log(["Error in loading: " + arg])
            return None

    def save(self, **kwargs):
        properties = self._load_existing_data()
        properties.update(kwargs)
        self._write_data(properties)

    def get_minecraft_dir(self):
        return get_minecraft_directory().replace("minecraft", "pitLauncher")

    def _load_existing_data(self) -> dict:
        try:
            with open(self.launcher_properties_path, "rb") as file:
                return json.decode(file.read(), type=dict)
        except DecodeError:
            return {}

    def _write_data(self, data: dict):
        with open(self.launcher_properties_path, "wb") as file:
            file.write(json.encode(data))

    def log(self, logs: list):
        with open(
            path.join(
                self.logs_path,
                str(self.time_start).split(".")[0].replace(":", "-").replace(" ", "_"),
            )
            + ".log",
            "a+",
            encoding="utf-8",
        ) as log:
            for log_ in logs:
                log.write(str(log_) + "\n" + "-" * 20 + "\n")

    def check(self, paths: List[str]):
        for _path in paths:
            try:
                mkdir(_path)
            except FileExistsError:
                self.log([f"{_path.capitalize()} Folder exists"])

    def mod(self, version_id, loader):
        if "vanila" in loader:
            return
        self.version = version_id
        self.loader = loader
        try:
            mkdir(path.join(self.minecraft_directory, f"{loader}_mods_{version_id}"))
        except FileExistsError:
            print("Exists")
            self.log([f"Found mods folder named '{loader}_mods_{version_id}'"])
        rename(
            path.join(
                self.minecraft_directory,
                f"{loader}_mods_{version_id}",
            ),
            path.join(self.minecraft_directory, "mods"),
        )

    def mod_rollback(self):
        try:
            rename(
                path.join(
                    self.minecraft_directory,
                    "mods",
                ),
                path.join(
                    self.minecraft_directory, f"{self.loader}_mods_{self.version}"
                ),
            )
        except AttributeError:
            self.log(["Moded folder not found !"])
        except FileNotFoundError:
            self.log(["Moded folder already saved !"])

