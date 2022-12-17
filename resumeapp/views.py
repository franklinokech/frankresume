from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Testimonial,
    Certificate,
    Portfolio,
    SocialMedia,
)

from django.views import generic
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'resumeapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        socialmedias = SocialMedia.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio
        context['socialmedias'] = socialmedias

        return context


class ContactView(generic.FormView):
    template_name = 'resumeapp/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'THank you. We will get in touch with you soon')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'resumeapp/portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'resumeapp/portfolio-detail.html'


class BlogView(generic.ListView):
    model = Blog
    template_name = 'resumeapp/blog.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'resumeapp/blog-detail.html'


class SocialMediaView(generic.ListView):
    model = SocialMedia
    template_name = 'resumeapp/partials/footer.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
