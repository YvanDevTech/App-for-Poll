# Dans votre fichier templatetags de l'application polls, par exemple, polls_tags.py
from django import template
from polls.models_ import Candidate

register = template.Library()

@register.filter
def get_candidate_name(candidates, candidate_id):
    return Candidate.objects.get(id=candidate_id).candidate
