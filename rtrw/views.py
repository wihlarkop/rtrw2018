from django.views.generic import CreateView
from django.shortcuts import HttpResponseRedirect, reverse, render
from django.views.generic.base import TemplateView
from suratpengantar.forms import SuratpengantarForm
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "index.html"


class SuratUserCreate(CreateView):
    def get(self, request, *args, **kwargs):
        form = SuratpengantarForm()
        return render(request, 'surat_user_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SuratpengantarForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Surat Pengantar Berhasil Diajukan")
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'surat_user_create.html', {'form': form})