f=KeyError
X=None
W='username'
V=Exception
Q='vanila'
M='quilt'
L='fabric'
K='forge'
J=True
I='loaders_dict'
H=str
C=False
B=''
from os import getenv as g
from sys import argv,exit as h
from time import perf_counter as Y
from PyQt6.QtCore import QThread as i,pyqtSignal as R,QSize,Qt,QUrl
from PyQt6.QtGui import QIcon,QFontDatabase as N,QFont as Z,QPixmap as j,QDesktopServices as k
from PyQt6.QtWidgets import QMainWindow as l,QLabel as a,QWidget as D,QLineEdit as b,QTabWidget as m,QVBoxLayout as E,QComboBox as F,QProgressBar as n,QPushButton as o,QApplication as p,QSpacerItem as S,QSizePolicy as G,QMessageBox as A
from minecraft_launcher_lib.quilt import get_stable_minecraft_versions as q
from minecraft_launcher_lib.command import get_minecraft_command as O
from minecraft_launcher_lib.fabric import get_stable_minecraft_versions as r
from minecraft_launcher_lib.forge import supports_automatic_install as s,install_forge_version as t,run_forge_installer as u,forge_to_installed_version as v,find_forge_version as c
from minecraft_launcher_lib.install import install_minecraft_version as w
from minecraft_launcher_lib.utils import get_version_list as x,get_installed_versions as y,get_java_executable as z
import fabric_install as A0,quilt_install as A1
from generate_username_r import generate_username as T
from uuid import uuid1
from minecraft_launcher_lib.types import MinecraftOptions as A2
from subprocess import call as P
from design import apply_style as d
from manager import Manager
class U(i):
	launch_setup_signal=R(H,H,H,H);progress_update_signal=R(int,int,H);state_update_signal=R(bool);manager=Manager();username=B;version_id=B;loader_version=B;loader=B;loader_dict:dict=B;progress=0;progress_max=0;progress_label=B;fabric_minecraft_version=B;quilt_minecraft_version=B
	def __init__(A):super().__init__();A.launch_setup_signal.connect(A.launch_setup);A.manager.log(['Starting Thread'])
	def launch_setup(A,version_id,username,loader,loader_version):A.version_id=version_id;A.username=username;A.loader=loader;A.loader_version=loader_version
	def update_progress_label(A,value):A.progress_label=value;A.progress_update_signal.emit(A.progress,A.progress_max,A.progress_label)
	def update_progress(A,value):A.progress=value;A.progress_update_signal.emit(A.progress,A.progress_max,A.progress_label)
	def update_progress_max(A,value):A.progress_max=value;A.progress_update_signal.emit(A.progress,A.progress_max,A.progress_label)
	def run(A):
		S='jvmArguments';R='disableMultiplayer';Q='token';N='uuid';L='setMax';K='setProgress';G='setStatus';M:0;M=z().lower()in['javaw','java'];A.manager.log(['Java not installed or not found ! Install Java version >= 17.0'if M else'Found Java !']);A.manager.mod(A.version_id,A.loader)
		if M:A.manager.log(['Java not Found !!!'])
		A.manager.log(['Username: '+A.username]);A.manager.save(username=A.username);A.manager.save(version=A.version_id);A.manager.save(loader=A.loader)
		try:A.loader_dict=A.manager.load(I);A.loader_dict.update({A.loader:A.version_id});A.manager.save(loaders_dict=A.loader_dict)
		except:A.manager.save();A.loader_dict=A.manager.load(I)or{};A.loader_dict.update({A.loader:A.version_id});A.manager.save(loaders_dict=A.loader_dict)
		A.state_update_signal.emit(J);D={W:A.username,N:H(uuid1()),Q:B,R:C,S:['-Xmx16G','-Xms2G']};F=A2(username=D[W],uuid=D[N],token=D[Q],disableMultiplayer=D[R],jvmArguments=D[S]);A.manager.log([f"Installing and running: {A.loader} version: {A.version_id} {A.loader_version}"])
		match A.loader:
			case'vanila':w(versionid=A.version_id,minecraft_directory=A.manager.minecraft_directory,callback={G:A.update_progress_label,K:A.update_progress,L:A.update_progress_max});P(O(version=A.version_id,minecraft_directory=A.manager.minecraft_directory,options=F))
			case'forge':
				if A.loader_version!=B:A.version_id=f"{A.version_id}-{A.loader_version}"
				else:A.version_id=c(A.version_id)
				if s(A.version_id):t(versionid=A.version_id,path=A.manager.minecraft_directory,callback={G:A.update_progress_label,K:A.update_progress,L:A.update_progress_max})
				else:
					try:u(A.version_id)
					except V as E:A.manager.log([E])
				P(O(version=v(A.version_id),minecraft_directory=A.manager.minecraft_directory,options=F))
			case'fabric':
				try:A.fabric_minecraft_version=A0.install_fabric(minecraft_version=A.version_id,minecraft_directory=A.manager.minecraft_directory,callback={G:A.update_progress_label,K:A.update_progress,L:A.update_progress_max},loader_version=A.loader_version)
				except V as E:A.manager.log(E)
				P(O(version=A.fabric_minecraft_version,minecraft_directory=A.manager.minecraft_directory,options=F))
			case'quilt':
				try:A.quilt_minecraft_version=A1.install_quilt(minecraft_version=A.version_id,minecraft_directory=A.manager.minecraft_directory,callback={G:A.update_progress_label,K:A.update_progress,L:A.update_progress_max},loader_version=A.loader_version)
				except V as E:A.manager.log(E)
				P(O(version=A.quilt_minecraft_version,minecraft_directory=A.manager.minecraft_directory,options=F))
		A.state_update_signal.emit(C)
class A3(l):
	def __init__(A):
		V=' | ';R='Pit Launcher';super().__init__();A.manager=U.manager;A.setFixedSize(A.manager.window_size[0],A.manager.window_size[1]);A.central_widget=D(A);A.logo=a(A.central_widget);A.logo.setMaximumSize(QSize(256,92));A.logo.setText(R);A.setWindowTitle(R);A.setWindowIcon(QIcon(A.manager.main_icon_path))
		if g('WAYLAND_DISPLAY'):e.setDesktopFileName('pit_launcher')
		A.logo.setPixmap(j(A.manager.logo_path));A.logo.setScaledContents(J);A.main_font_id=N.addApplicationFont(A.manager.main_font_path);A.main_font_family=N.applicationFontFamilies(A.main_font_id)[0];A.main_font=Z(A.main_font_family);A.main_font.setPointSize(A.manager.main_font_size);A.sub_font_id=N.addApplicationFont(A.manager.sub_font_path);A.sub_font_family=N.applicationFontFamilies(A.sub_font_id)[0];A.sub_font=Z(A.sub_font_family);A.sub_font.setPointSize(A.manager.sub_font_size);A.title_spacer=S(20,40,G.Policy.Minimum,G.Policy.Expanding);A.play_spacer=S(0,0,G.Policy.Minimum,G.Policy.Expanding);A.username=b(A.central_widget);A.username.setPlaceholderText('Username');A.logo.mousePressEvent=A.open_folder
		try:
			H=A.manager.load(W)
			if H is X or H==B:H=T()[0];A.manager.save(username=H)
			A.username.setText(H)
		except f:A.username.setText(T()[0])
		def Y():A.manager.save(username=A.username.text())
		A.username.setFont(A.main_font);A.username.textChanged.connect(Y);A.tab_widget=m();A.current_loader={0:Q,1:K,2:L,3:M};A.current_tab={Q:0,K:1,L:2,M:3};A.vanila_tab=D();A.vanila_layout=E(A.vanila_tab);A.vanilla_combobox=F();A.vanila_list=[A['id']for A in x()if A['type']=='release'];A.vanila_layout.addWidget(A.vanilla_combobox);A.vanilla_combobox.setFont(A.main_font);A.vanilla_combobox.addItems(A.vanila_list);A.vanila_tab.setMinimumWidth(200);A.forge_tab=D();A.forge_layout=E(A.forge_tab);A.forge_combobox=F();A.forge_list=[A for A in A.vanila_list if c(A)is not X];A.forge_combobox.addItems(A.forge_list);A.forge_layout.addWidget(A.forge_combobox);A.forge_combobox.setFont(A.main_font);A.fabric_tab=D();A.fabric_layout=E(A.fabric_tab);A.fabric_combobox=F();A.fabric_list=r();A.fabric_combobox.addItems(A.fabric_list);A.fabric_layout.addWidget(A.fabric_combobox);A.fabric_combobox.setFont(A.main_font);A.quilt_tab=D();A.quilt_layout=E(A.quilt_tab);A.quilt_combobox=F();A.quilt_list=q();A.quilt_combobox.addItems(A.quilt_list);A.quilt_layout.addWidget(A.quilt_combobox);A.quilt_combobox.setFont(A.main_font)
		try:A.manager.log(['Adding Vanila versions']);A.vanilla_combobox.setCurrentText(A.manager.load(I)[Q]);A.manager.log(['Adding Forge versions']);A.forge_combobox.setCurrentText(A.manager.load(I)[K]);A.manager.log(['Adding Fabric versions']);A.fabric_combobox.setCurrentText(A.manager.load(I)[L]);A.manager.log(['Adding Quilt versions']);A.quilt_combobox.setCurrentText(A.manager.load(I)[M])
		except:A.manager.log(['Error ! {','Failed adding versions !','} Skipping !'])
		A.settings_tab=D();A.theme_combobox=F();A.tab_widget.addTab(A.vanila_tab,'Vanilla');A.tab_widget.addTab(A.forge_tab,'Forge');A.tab_widget.addTab(A.fabric_tab,'Fabric');A.tab_widget.addTab(A.quilt_tab,'Quilt');A.settings_layout=E(A.settings_tab);A.settings_layout.addWidget(A.theme_combobox);A.theme_combobox.addItems([A.name.capitalize()for A in A.manager.load_styles()]);A.theme_combobox.currentIndexChanged.connect(A.apply_current_style);A.theme_combobox.setFont(A.main_font);O=D();P=D();A.tab_widget.addTab(O,V);A.tab_widget.tabBar().setTabEnabled(A.tab_widget.indexOf(O),C);A.tab_widget.tabBar().setUsesScrollButtons(C);A.tab_widget.tabBar().setStyleSheet('QTabBar::tab:disabled {background: transparent;border: none;}');A.installed_tab=D();A.installed_combobox=F();A.installed_versions_list=[A['id']for A in y(minecraft_directory=A.manager.minecraft_directory)];A.installed_combobox.addItems(A.installed_versions_list);A.installed_search=b();A.installed_search.setPlaceholderText('Search for version');A.installed_search.setFont(A.main_font);A.installed_search.textChanged.connect(A.filter_items);A.installed_layout=E(A.installed_tab);A.installed_layout.addWidget(A.installed_search);A.installed_layout.addWidget(A.installed_combobox);A.installed_combobox.setFont(A.main_font);A.tab_widget.addTab(A.installed_tab,'Installed');A.tab_widget.addTab(P,V);A.tab_widget.tabBar().setTabEnabled(A.tab_widget.indexOf(P),C);A.tab_widget.addTab(A.settings_tab,'Theme');A.tab_widget.setFont(A.main_font)
		try:A.tab_widget.setCurrentIndex(A.current_tab[A.manager.load('loader')])
		except:A.manager.log(['Error !','No tab index found !','Skipping !'])
		A.progress_spacer=S(20,20,G.Policy.Minimum,G.Policy.Minimum);A.start_progress_label=a(A.central_widget);A.start_progress_label.setText(B);A.start_progress_label.setVisible(C);A.start_progress=n(A.central_widget);A.start_progress.setProperty('value',24);A.start_progress.setVisible(C);A.start_button=o(A.central_widget);A.start_button.setFont(A.sub_font);A.start_button.setText('Play');A.start_button.clicked.connect(A.launch_game);A.current_tab_index=A.tab_widget.currentIndex()
		def d():
			A.current_tab_index=A.tab_widget.currentIndex()
			match A.current_tab_index:
				case 7:A.start_button.setDisabled(J)
				case 5:
					if len(A.installed_versions_list)==0:A.start_button.setDisabled(J)
					else:A.start_button.setDisabled(C)
				case _:A.start_button.setDisabled(C)
		A.tab_widget.currentChanged.connect(d);A.vertical_layout=E(A.central_widget);A.vertical_layout.setContentsMargins(15,15,15,15);A.vertical_layout.addWidget(A.logo,0,Qt.AlignmentFlag.AlignHCenter);A.vertical_layout.addItem(A.title_spacer);A.vertical_layout.addWidget(A.username);A.vertical_layout.addItem(A.progress_spacer);A.vertical_layout.addWidget(A.start_progress_label);A.vertical_layout.addWidget(A.start_progress);A.vertical_layout.addWidget(A.start_button);A.vertical_layout.addItem(A.play_spacer);A.vertical_layout.addWidget(A.tab_widget);A.launch_thread=U();A.launch_thread.state_update_signal.connect(A.state_update);A.launch_thread.progress_update_signal.connect(A.update_progress);A.setCentralWidget(A.central_widget);A.apply_loaded_style()
	def open_folder(A,event=X):B=A.manager.get_minecraft_dir();k.openUrl(QUrl.fromLocalFile(B))
	def filter_items(A):
		D=A.installed_search.text().lower();A.installed_combobox.clear();B=[A for A in A.installed_versions_list if D in A.lower()];A.installed_combobox.addItems(B)
		if len(B)==0:A.start_button.setDisabled(J)
		else:A.start_button.setDisabled(C)
	def closeEvent(B,event):
		C=event;D=A.question(B,'Выход','Вы уверены, что хотите выйти?',A.StandardButton.Yes|A.StandardButton.No,A.StandardButton.No)
		if D==A.StandardButton.Yes:C.accept();B.manager.mod_rollback()
		else:C.ignore()
	def state_update(A,value):B=value;A.start_button.setDisabled(B);A.start_progress_label.setVisible(B);A.start_progress.setVisible(B)
	def update_progress(A,progress,max_progress,label):A.start_progress.setValue(progress);A.start_progress.setMaximum(max_progress);A.start_progress_label.setText(label)
	def apply_current_style(A):B=A.theme_combobox.currentText().lower();C=d([A for A in A.manager.load_styles()if A.name==B][0],A.sub_font_family);A.setStyleSheet(C[0]);A.tab_widget.setStyleSheet(C[1]);A.manager.save(current_style=B)
	def apply_loaded_style(A):
		B=A.manager.load('current_style')or'dark'
		try:C=d([A for A in A.manager.load_styles()if A.name==B][0],A.sub_font_family);A.setStyleSheet(C[0]);A.tab_widget.setStyleSheet(C[1]);A.theme_combobox.setCurrentText(B.capitalize())
		except f:A.manager.log([f"No style {B} found !"])
	def launch_game(C):
		D='-';G={0:C.vanilla_combobox.currentText(),1:C.forge_combobox.currentText(),2:C.fabric_combobox.currentText(),3:C.quilt_combobox.currentText()}
		match C.current_tab_index:
			case 5:
				A=C.installed_combobox.currentText();E=Q;F=B
				if L in A:A,F=A.split(D)[-1],A.split(D)[2];E=L
				elif M in A:A,F=A.split(D)[-1],A.split(D)[2];E=M
				elif K in A:A,F=A.split(D)[0],A.split(D)[-1];E=K
			case _:A=G[C.current_tab_index];F=B;E=C.current_loader[C.current_tab_index]
		C.launch_thread.launch_setup_signal.emit(A,C.username.text()if C.username.text()!=B else T()[0],E,F);C.launch_thread.start()
if __name__=='__main__':A4=Y();e=p(argv);A5=A3();A5.show();U.manager.log([f"App loaded in {Y()-A4}/sec"]);h(e.exec())