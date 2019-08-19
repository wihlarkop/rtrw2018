from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.shortcuts import HttpResponseRedirect, redirect, reverse, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from suratpengantar.models import Suratpengantar
from suratpengantar.forms import SuratpengantarForm


class SuratCreate(LoginRequiredMixin, CreateView):
    login_url = '/akun/login'

    def get(self, request, *args, **kwargs):
        form = SuratpengantarForm()
        return render(request, 'suratpengantar/surat_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SuratpengantarForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('suratpengantar:list_surat'))
        return render(request, 'suratpengantar/surat_create.html', {'form': form})


class SuratList(LoginRequiredMixin, ListView):
    login_url = '/akun/login'
    model = Suratpengantar
    template_name = "suratpengantar/surat_list.html"
    context_object_name = 'surat_list'


class SuratUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/akun/login'
    form_class = SuratpengantarForm
    model = Suratpengantar
    template_name = "suratpengantar/surat_create.html"

    def form_valid(self, form):
        form.save()
        return redirect(reverse("suratpengantar:list_surat"))


class SuratDelete(LoginRequiredMixin, DeleteView):
    login_url = '/akun/login'
    model = Suratpengantar
    template_name = "suratpengantar/surat_confirm_delete.html"
    success_url = reverse_lazy("suratpengantar:list_surat")
