from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        hbox = Gtk.HBox()
        self.add(hbox)
        
        clone = Gtk.Button("Clone")
        hbox.add(clone)
        
        push = Gtk.Button("Push")
        hbox.add(push)

        pull = Gtk.Button("Pull")
        hbox.add(pull)

        status = Gtk.Button("Status")
        hbox.add(status)
        
        add = Gtk.Button("Add")
        hbox.add(add)
        
        
        

        self.show_all()
