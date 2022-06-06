class PageTitleViewMixin:
    title = ""

    def get_title(self):
        """
        Return the class title attr by default,
        but you can override this method to further customize
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class DisplayTypeViewMixin:
    display_type = ""

    def get_display_type(self):
        return self.display_type

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_type"] = self.get_display_type()
        return context
