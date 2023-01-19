from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.html import escape, format_html
from django import template

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, current_user=None) -> str:
  if not isinstance(author, user_model):
    return ""

  if author == current_user:
    return format_html("<strong>me</strong>")
  
  if author.first_name and author.last_name:
    name = escape(f"{author.first_name} {author.last_name}")
  else:
    name = escape(author.username) 

  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html("</a>") 
  else:
    prefix = ''; suffix = ''
  
  return format_html('{}{}{}', prefix, name, suffix)