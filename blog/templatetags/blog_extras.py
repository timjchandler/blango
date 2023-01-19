from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.html import escape, format_html
from django import template
from blog.models import Post

register = template.Library()
user_model = get_user_model()

# @register.simple_tag(takes_context=True)
# def author_details_tag(context):
#   request = context["request"]
#   current_user = request.user 
#   post = context["post"]
#   author = post.author 

#   if author == current_user:
#     return format_html("<strong>me</strong>")

#   if author.first_name and authour.last_name:
#     name = f"{author.first_name} {author.last_name}"
#   else:
#     name = f"{author.username}"
  
#   if author.email:
#     prefix = format_html(f'<a href="mailto:{author.email}">')
#     suffix = format_html('</a>')
#   else:
#     prefix = ''; suffix = ''

#   return format_html(f"{prefix}{name}{suffix}")

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

@register.simple_tag
def row(extra_classes: str = "") -> str:
  return format_html(f'<div class="row {extra_classes}">')

@register.simple_tag 
def endrow() -> str:
  return format_html('</div>')

@register.simple_tag
def col(extra_classes: str = "") -> str:
  return format_html(f'<div class="row {extra_classes}">')

@register.simple_tag
def endcol() -> str:
  return format_html('</div>')

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": posts}
