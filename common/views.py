class Title_Mixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(Title_Mixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
