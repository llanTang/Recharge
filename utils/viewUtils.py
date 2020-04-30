class ViewUtils:
    def destroyframe(master=None):
        for widget in master.winfo_children():
            widget.destroy()
