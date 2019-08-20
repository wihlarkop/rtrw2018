from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from warga.forms import KTPForm, KkForm
from warga.models import Ktp, Kk


class KtpCreate(LoginRequiredMixin, CreateView):
    login_url = '/akun/login'

    def get(self, request, *args, **kwargs):
        form = KTPForm()
        return render(request, 'ktp/ktp_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = KTPForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "KTP Berhasil Ditambahkan")
            return HttpResponseRedirect(reverse_lazy('warga:list_ktp'))
        messages.error(request, "NIK Sudah Terdaftar")
        return render(request, 'ktp/ktp_create.html', {'form': form})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({'task': Ktp.objects.get(id=self.kwargs['pk'])})
    #     return context


class KtpList(LoginRequiredMixin, ListView):
    login_url = '/akun/login'
    model = Ktp
    template_name = "ktp/ktp_list.html"
    context_object_name = 'ktp_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Ktp.objects.filter(Q(nik__icontains=query) | Q(nama__icontains=query))
        else:
            object_list = Ktp.objects.all()
        return object_list


class KtpDetail(LoginRequiredMixin, DetailView):
    login_url = '/akun/login'
    model = Ktp
    template_name = "ktp/ktp_detail.html"
    context_object_name = 'ktp_detail'


class KtpUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/akun/login'
    form_class = KTPForm
    model = Ktp
    template_name = "ktp/ktp_create.html"

    def form_valid(self, form):
        form.save()
        return redirect(reverse("warga:list_ktp"))


class KtpDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Ktp
    template_name = "ktp/ktp_confirm_delete.html"
    success_url = reverse_lazy("warga:list_ktp")
    #
    # def get_success_message(self, cleaned_data):
    #     print(cleaned_data)
    #     return "KTP Berhasil Dihapus"


class KkCreate(LoginRequiredMixin, CreateView):
    login_url = '/akun/login'
    def get(self, request, *args, **kwargs):
        form = KkForm
        return render(request, 'kk/kk_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = KkForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nomor KK Berhasil Ditambahkan")
            return HttpResponseRedirect(reverse('warga:list_kk'))
        messages.error(request, "Nomor KK Sudah Terdaftar")
        return render(request, 'kk/kk_create.html', {'form': form})

    # def form_valid(self, form):
    #     model = form.save(commit=False)
    #     model.save()
    #     return HttpResponseRedirect(reverse('warga:list_kk'))


class KkList(LoginRequiredMixin, ListView):
    login_url = '/akun/login'
    model = Kk
    template_name = "kk/kk_list.html"
    context_object_name = 'kk_list'

    def get_queryset(self):
        query = self.request.GET.get('k')
        if query:
            object_list = Kk.objects.filter(Q(nomor_kk__icontains=query))
        else:
            object_list = Kk.objects.all()
        return object_list

class KkUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/akun/login'
    form_class = KkForm
    model = Kk
    template_name = "kk/kk_create.html"

    def form_valid(self, form):
        form.save()
        return redirect(reverse("warga:list_kk"))


class KkDelete(LoginRequiredMixin,DeleteView):
    login_url = '/akun/login'
    model = Kk
    template_name = "kk/kk_confirm_delete.html"
    success_url = reverse_lazy("warga:list_kk")
