from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from dploi_server.models import Realm, Application, Deployment
from django.contrib import messages

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

    def get_success_url(self):
        messages.success(self.request, "%s was successfully updated" % self.object, "success")
        return reverse("dploi_application_list")

class ApplicationCreate(CreateView):
    model = Application
    template_name = "dploi_server_ui/application_form.html"

    def get_success_url(self):
        messages.success(self.request, "%s was successfully added to the database" % self.object, "success")
        return reverse("dploi_application_list")

class DeploymentUpdate(UpdateView):
    model = Deployment
    template_name = "dploi_server_ui/deployment_form.html"

    def get_success_url(self):
        messages.success(self.request, "%s was successfully updated" % self.object, "success")
        return reverse("dploi_application_list")

class DeploymentCreate(CreateView):
    model = Deployment
    template_name = "dploi_server_ui/deployment_form.html"

    def get_success_url(self):
        messages.success(self.request, "%s was successfully added to the database" % self.object, "success")
        return reverse("dploi_application_list")

class DeploymentDetail(DetailView):
    model = Deployment
    template_name = "dploi_server_ui/deployment_detail.html"