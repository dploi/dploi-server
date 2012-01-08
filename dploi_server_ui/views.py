from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from dploi_server.models import Realm, Application

class OverviewView(TemplateView):
    template_name = "dploi_server_ui/overview.html"

    def get_context_data(self, **kwargs):
        return {

        }

class RealmList(ListView):
    model = Realm
    template_name = "dploi_server_ui/realm_list.html"

class ApplicationList(ListView):
    model = Application
    template_name = "dploi_server_ui/application_list.html"


class ApplicationDetail(DetailView):
    model = Application
    template_name = "dploi_server_ui/application_detail.html"

class ApplicationUpdate(UpdateView):
    model = Application
    template_name = "dploi_server_ui/application_form.html"