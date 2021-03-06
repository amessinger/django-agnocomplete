"""
Agnocomplete Widgets
"""
from django.forms import widgets
from django.core.urlresolvers import reverse
from django.utils.encoding import force_text as text

__all__ = ['AgnocompleteInput']


class AgnocompleteWidgetMixin(object):
    def build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(AgnocompleteWidgetMixin, self).build_attrs(
            extra_attrs, **kwargs)
        attrs.update({
            'data-url': reverse(
                # FIXME: the namespace should be a setting variable.
                'agnocomplete:agnocomplete', args=[self.agnocomplete.name])
        })
        return attrs

    def render_options(self, choices, selected_choices):
        selected_choices = set(text(v) for v in selected_choices)
        selected_choices_tuples = self.agnocomplete.selected(selected_choices)
        output = []
        for option_value, option_label in selected_choices_tuples:
            output.append(self.render_option(selected_choices, option_value, option_label))  # noqa
        return '\n'.join(output)


class AgnocompleteInput(AgnocompleteWidgetMixin, widgets.Select):
    pass
