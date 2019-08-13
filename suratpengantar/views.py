from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.shortcuts import HttpResponseRedirect, redirect, reverse, render
from django.urls import reverse_lazy

from suratpengantar.models import Suratpengantar
from suratpengantar.forms import SuratpengantarForm

class SuratCreate(CreateView):
    def get(self, request, *args, **kwargs):
        form = SuratpengantarForm()
        return render(request, 'ktp/ktp_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SuratpengantarForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('warga:list_ktp'))
        return render(request, 'ktp/ktp_create.html', {'form': form})


class SuratList(ListView):
    model = Suratpengantar
    template_name = "ktp/ktp_list.html"
    context_object_name = 'ktp_list'


class SuratDetail(DetailView):
    model = Suratpengantar
    template_name = "ktp/ktp_detail.html"
    context_object_name = 'ktp_detail'


class SuratUpdate(UpdateView):
        form_class = SuratpengantarForm
        model = Suratpengantar
        template_name = "ktp/ktp_create.html"

        def form_valid(self, form):
            form.save()
            return redirect(reverse("warga:list_ktp"))


class SuratDelete(DeleteView):
    model = Suratpengantar
    template_name = "ktp/ktp_confirm_delete.html"
    success_url = reverse_lazy("warga:list_ktp")