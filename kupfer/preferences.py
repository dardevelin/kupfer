import gtk

from kupfer import config

class PreferencesWindowController (object):
	def __init__(self):
		"""Load ui from data file"""
		builder = gtk.Builder()
		ui_file = config.get_data_file("preferences.ui")
		print ui_file
		if ui_file:
			builder.add_from_file(ui_file)
		else:
			self.window = None
			return
		builder.connect_signals(self)
		self.window = builder.get_object("preferenceswindow")
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.connect("delete-event", self._close_window)
	def on_checkstatusicon_toggled(self, widget):
		pass
	def on_checkautostart_toggled(self, widget):
		pass
	def on_entrykeybinding_changed(self, widget):
		pass
	def on_closebutton_clicked(self, widget):
		self.hide()
	def show(self):
		self.window.show()
	def hide(self):
		self.window.hide()
	def _close_window(self, *ignored):
		self.hide()
		return True

_preferences_window = None

def GetPreferencesWindowController():
	global _preferences_window
	if _preferences_window is None:
		_preferences_window = PreferencesWindowController()
	return _preferences_window
