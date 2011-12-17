"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'mccard.admin_tools_dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'mccard.admin_tools_dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db.models import Q

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


from datetime import datetime

class BirthdayModule(modules.DashboardModule):
    def is_empty(self):
        return self.message == ''

    def __init__(self, **kwargs):
        super(BirthdayModule, self).__init__(**kwargs)
        self.template = 'birthday.html'
        self.message = kwargs.get('message', '')
    
    def init_with_context(self, context):
        request = context['request']
        from card.models import UserCard
        now = datetime.today()
        today = UserCard.objects.filter(Q(birthday__month=now.month)).filter(Q(birthday__day=now.day))
        request.today = today


class SearchPatientModule(modules.DashboardModule):
    def is_empty(self):
        return self.message == ''

    def __init__(self, **kwargs):
        super(SearchPatientModule, self).__init__(**kwargs)
        self.template = 'search-patients.html'
        self.message = kwargs.get('message', '')


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for mccard.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('List of patiens'), '/cards/card/usercard/'],
                [_('Add patient'), '/cards/card/usercard/add/'],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
        
        # Birthday module 
        self.children.append(BirthdayModule(title=_("Birday"), message = u' '))
        
        # Search patients module
        self.children.append(SearchPatientModule(title=_("Find patient"), message = u' '))
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for mccard.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
