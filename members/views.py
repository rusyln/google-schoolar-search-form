from django.shortcuts import render
from django.views import View
from serpapi import GoogleSearch
from .forms import SearchForm # Import your search form

class SearchProfileView(View):
    template_name = 'profiles/profile.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)  # Bind request.GET data to the form
        profiles = []

        if form.is_valid():
            person_to_search = form.cleaned_data.get('person_to_search')
            params = {
                "api_key": "247fba5c9bb20d401d4619e01fa6d83af72a705c3e8c8246bea0efd8172bc8fd",
                "engine": "google_scholar_profiles",
                "hl": "en",
                "mauthors": person_to_search  # Update with the value from the form
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            profiles = results.get("profiles", [])

        return render(request, self.template_name, {'profiles': profiles, 'form': form})
