"""
TO-DO: Write a description of what this XBlock is.
"""

import pkg_resources
from django.template import Context
from django.template.loader import get_template
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment


class {{cookiecutter.class_name}}(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def build_fragment(
            self,
            template,
            context_dict,
            initialize_js_func,
            additional_css=[],
            additional_js=[],
    ):
        #  pylint: disable=dangerous-default-value, too-many-arguments
        """
        Creates a fragment for display.
        """
        context = Context(context_dict)
        fragment = Fragment(template.render(context))
        for item in additional_css:
            url = self.runtime.local_resource_url(self, item)
            fragment.add_css_url(url)
        for item in additional_js:
            url = self.runtime.local_resource_url(self, item)
            fragment.add_javascript_url(url)
        fragment.initialize_js(initialize_js_func)
        return fragment

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the {{cookiecutter.class_name}}, shown to students
        when viewing courses.
        """
        context = context or {}
        context.update(
            {
                'count': count,
            }
        )
        template = get_template('{{cookiecutter.short_name|lower}}.html')
        fragment = self.build_fragment(
            template,
            context
            initialize_js_fun='{{cookiecutter.class_name}}',
            additional_css=[
                'static/css/{{cookiecutter.short_name|lower}}.css',
            ],
            additional_js=[
                'static/js/{{cookiecutter.short_name|lower}}.js',
            ],
        )
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """
        A canned scenario for display in the workbench.
        """
        return [
            ("{{cookiecutter.class_name}}",
             """<{{cookiecutter.short_name|lower}}/>
             """),
            ("Multiple {{cookiecutter.class_name}}",
             """<vertical_demo>
                <{{cookiecutter.short_name|lower}}/>
                <{{cookiecutter.short_name|lower}}/>
                <{{cookiecutter.short_name|lower}}/>
                </vertical_demo>
             """),
        ]
