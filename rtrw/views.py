from django.views.generic import CreateView
from django.shortcuts import HttpResponseRedirect, reverse, render
from django.views.generic.base import TemplateView


from suratpengantar.forms import UserForm

# class UserView(CreateView):
#     class SuratCreate(CreateView):
#         def get(self, request, *args, **kwargs):
#             form = UserForm()
#             return render(request, 'templates/index.html', {'form': form})
#
#         def post(self, request, *args, **kwargs):
#             form = UserForm(request.POST)
#             print(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('suratpengantar:list_surat'))
#             return render(request, 'templates/index.html', {'form': form})
class HomePageView(TemplateView):
    template_name = "index.html"