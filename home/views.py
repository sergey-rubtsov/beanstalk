from django.views.generic import DetailView
from django.http import Http404
from home.models import About, Cv

class AboutView(DetailView):
    model = About
    template_name = "about.html"
    context_object_name = 'about'

    def get_object(self):
        try:
            queryset = self.model.objects.latest('post_date')
        except self.model.DoesNotExist:
            return self.get_empty_about
        except self.model.MultipleObjectsReturned:
            raise Http404
        return queryset

    def get_empty_about(self):
        result = self.model
        result.topic = "Empty"
        result.message = "Empty"
        return result

class CVView(AboutView):
    model = Cv
    template_name = "cv.html"
    context_object_name = 'cv'

    def get_empty_about(self):
        result = self.model
        result.title = "Empty"
        result.info = "Empty"
        return result