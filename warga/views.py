from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from warga.forms import KTPForm, KkForm, KkktpForm
from warga.models import Ktp, Ktpkk, Kk


class KtpCreate(CreateView):
    def get(self, request, *args, **kwargs):
        form = KTPForm()
        return render(request, 'ktp/ktp_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = KTPForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('warga:list_ktp', args=[Ktp.pk]))
        return render(request, 'ktp/ktp_create.html', {'form': form})


class KtpList(ListView):
    model = Ktp
    template_name = "ktp/ktp_list.html"
    context_object_name = 'ktp_list'


class KtpDetail(DetailView):
    model = Ktp
    template_name = "ktp/ktp_detail.html"
    context_object_name = 'ktp_detail'


class KtpUpdate(UpdateView):
        form_class = KTPForm
        model = Ktp
        template_name = "ktp/ktp_create.html"

        def form_valid(self, form):
            form.save()
            return redirect(reverse("warga:list_ktp"))


class KtpDelete(DeleteView):
    model = Ktp
    template_name = "ktp/ktp_confirm_delete.html"
    success_url = reverse_lazy("warga:list_ktp")


class KkCreate(CreateView):
    def get(self, request, *args, **kwargs):
        form = KkForm
        return render(request, 'kk/kk_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = KkForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('warga:list_kk'))
        return render(request, 'kk/kk_create.html', {'form': form})


class KkList(ListView):
    model = Kk
    template_name = "kk/kk_list.html"
    context_object_name = 'kk_list'

#
# class KkDetail(DetailView):
#     model = Kk
#     template_name = "kk/kk_detail.html"
#     context_object_name = 'kk_detail'


class KkUpdate(UpdateView):
    form_class = KkForm
    model = Ktp
    template_name = "kk/kk_create.html"

    def form_valid(self, form):
        form.save()
        return redirect(reverse("list_kk"))


class KkDelete(DeleteView):
    model = Kk
    template_name = "kk/kk_delete.html"
    success_url = reverse_lazy("warga:list_kk")
