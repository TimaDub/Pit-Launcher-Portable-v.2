# Copyright (c) 2024, [Tymofii Dubovyi]
# Licensed under the MIT License.
# See LICENSE file for details.

import sys
from os import path, mkdir
from datetime import datetime
from msgspec import json, Struct, DecodeError
from typing import List
from minecraft_launcher_lib.utils import get_minecraft_directory
import resources
from PyQt6.QtCore import QFile, QIODevice


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return path.join(sys._MEIPASS, relative_path)
    return path.join(path.abspath("."), relative_path)


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
        base_style_name: str = "styles.json",
        logo_path: str = "logos/logo.png",
        main_icon_path: str = "logos/icon.png",
        main_font_path: str = "main_font.ttf",
        sub_font_path: str = "sub_font.ttf",
    ):
        self.minecraft_directory = directory
        self.launcher_properties_path = path.join(
            self.minecraft_directory, properties_path
        )
        self.assets_folder = assets_path
        self.logs_path = path.join(self.minecraft_directory, logs_path)
        self.workspace_path = path.join(self.minecraft_directory, app_path)
        self.base_style_path: str = path.join(self.assets_folder, base_style_name)
        self.styles_path = path.join(self.workspace_path, "styles")
        #
        self.logo_path = path.join(self.assets_folder, logo_path)
        self.main_icon_path = path.join(self.assets_folder, main_icon_path)
        self.main_font_path = path.join(self.assets_folder, main_font_path)
        self.sub_font_path = path.join(self.assets_folder, sub_font_path)
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
            print("Json exists")

    def load(self):
        file = QFile(self.base_style_path)
        if not file.open(QIODevice.OpenModeFlag.ReadOnly):
            print("Ошибка: не удалось открыть файл")
            return None

        data = file.readAll().data().decode("utf-8")
        file.close()
        return json.decode(data, type=Saver)

    def load_properties(self, arg):
        try:
            with open(
                self.launcher_properties_path, "r+", encoding="utf-8"
            ) as launcher_properties:
                properties = json.load(launcher_properties)
                return properties[arg]
        except DecodeError:
            self.log(["Error in loading: " + arg])
            return None
        except KeyError:
            self.log(["Error in loading: " + arg])
            return None

    def save_properties(self, **kwargs):
        properties = self._load_existing_data()
        properties.update(kwargs)
        self._write_data(properties)

    def _load_existing_data(self) -> dict:
        if not self.launcher_properties_path.exists():
            return {}

        try:
            with self.launcher_properties_path.open("rb") as file:
                return json.decode(file.read(), type=dict)
        except DecodeError:
            return {}

    def _write_data(self, data: dict):
        with self.launcher_properties_path.open("wb") as file:
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
        for path in paths:
            try:
                mkdir(path)
            except FileExistsError:
                print(f"{path.capitalize()} Folder exists")


if __name__ == "__main__":
    manager1 = Manager()
    print([style.name for style in manager1.load().styles])
