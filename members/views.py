# Import necessary modules and classes
from django.shortcuts import render
from django.views import View
from serpapi import GoogleSearch
from .forms import SearchForm  # Import your search form and the new form

# Define a class-based view that inherits from django.views.View
class SearchProfileView(View):
    # Set the template name for this view
    template_name = 'profiles/profile.html'

    # Define the get method to handle GET requests
    def get(self, request, *args, **kwargs):
        # Create an instance of the SearchForm class and bind the request GET data to it
        form = SearchForm(request.GET)

        # Initialize an empty list to store the profiles
        profiles = []

        # Check if the form is valid
        if form.is_valid():
            # Get the value of the 'person_to_search' field from the form's cleaned data
            person_to_search = form.cleaned_data.get('person_to_search')

            # Construct a dictionary of parameters for the Google Scholar Profiles search API
            params = {
                "api_key": "247fba5c9bb20d401d4619e01fa6d83af72a705c3e8c8246bea0efd8172bc8fd",
                "engine": "google_scholar_profiles",
                "hl": "en",
                "mauthors": person_to_search  # Update with the value from the form
            }

            # Create an instance of the GoogleSearch class with the parameters
            search = GoogleSearch(params)

            # Call the get_dict method of the GoogleSearch instance to retrieve the search results
            results = search.get_dict()

            # Extract the profiles from the search results and store them in the 'profiles' list
            profiles = results.get("profiles", [])

        # Render the 'profile.html' template with the profiles and the form as context
        return render(request, self.template_name, {'profiles': profiles, 'form': form})


class ProfileDetailView(View):
    template_name = 'profiles/profile-detail.html'

    def get(self, request, author_id):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": "247fba5c9bb20d401d4619e01fa6d83af72a705c3e8c8246bea0efd8172bc8fd"
        }
        search = GoogleSearch(params)  # Assuming GoogleSearch is your model to interact with the API
        results = search.get_dict()
        author = results.get("author", {})
        articles = results.get("articles", [{}])
        
        return render(request, self.template_name, {'author': author, 'articles': articles})

def home_view(request):
    form = SearchForm()  # Replace 'YourForm' with the name of your form class

    return render(request, 'home.html', {'form': form})
