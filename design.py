# Copyright (c) 2024, [Tymofii Dubovyi]
# Licensed under the MIT License.
# See LICENSE file for details.
from manager import SaveStruct


def apply_style(style: SaveStruct, font):
    main_style = f"""
                QWidget {{
                    background-color: {style.background_color};
                    color: {style.text_color};
                    font-family : {font};
                    font-size: 18pt;
                    line-height: 20px;
                }}
                QPushButton {{
                    background-color: {style.background_color};
                    color: {style.text_color};
                    border: 1px solid {style.button_color};
                    border-radius: 5px;
                    padding: 5px;
                }}
                QPushButton:disabled {{
                    background-color: {style.background_color};
                    color: gray;
                    border: 1px solid gray;
                    border-radius: 5px;
                    padding: 5px;
                }}
                QLineEdit {{
                    background: {style.background_color};
                    color: {style.text_color};
                    border: 1px solid {style.button_color};
                    border-radius: 5px;
                    padding: 5px;
                }}
                QComboBox {{
                    background-color: {style.background_color};
                    color: {style.text_color};
                    border: 1px solid {style.button_color};
                    border-radius: 5px;
                }}
                QCheckBox {{
                    color: {style.text_color};
                }}
                QTabWidget::pane {{
                    border: 1px solid {style.button_color};
                }}
                QTabBar::tab {{
                    background: {style.background_color};
                    color: {style.text_color};
                    border: 1px solid {style.button_color};
                    border-top-left-radius: 5px;
                    border-top-right-radius: 5px;
                    padding: 5px;
                }}
                QProgressBar {{
                color: {style.progress_bar_text_color};
                text-align: center;
                font-family : {font};
                font-size : 28px;
                background: {style.background_color};
                border-radius: 5px;
                }}
                QProgressBar::chunk{{
                    border-radius: 5px;
                    background: {style.progress_bar_color};
                }}

                QComboBox QAbstractItemView {{
                    background-color: {style.background_color};
                    selection-background-color: {style.text_color};
                    selection-color: {style.background_color};
                    color: {style.text_color};
                }}
                """
    tab_style = f"""
                        QTabBar::tab:selected {{
                            background: {style.selected_tab_background_color};
                            font-family : {font};
                            line-height: 20px;
                            font-size : 18px;
                            color: {style.selected_tab_color}
                        }}
                    """
    return main_style, tab_style

