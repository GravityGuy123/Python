from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

guide_text = """
Step-by-step Guide: Adding Image Upload and Display in Django

1. Install Pillow
   pip install Pillow

2. Update your model (models.py)
   from django.db import models
   class Post(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

3. Update your admin (admin.py)
   from django.contrib import admin
   from .models import Post
   from django.utils.html import format_html
   class PostAdmin(admin.ModelAdmin):
       list_display = ("title", "post_image_tag", "created_at", "updated_at")
       def post_image_tag(self, obj):
           if obj.post_image:
               return format_html('<img src="{}" width="100" height="100" />', obj.post_image.url)
           return "-"
       post_image_tag.short_description = 'Image'
   admin.site.register(Post, PostAdmin)

4. Update settings.py
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'

5. Update main urls.py (firstproject/urls.py)
   from django.conf import settings
   from django.conf.urls.static import static
   urlpatterns = [
       # ...your url patterns...
   ]
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

6. Make and apply migrations
   python manage.py makemigrations
   python manage.py migrate

7. Update your template (index.html)
   {% for post in posts %}
       <div>
           <h2>{{ post.title }}</h2>
           {% if post.post_image %}
               <img src="{{ post.post_image.url }}" alt="{{ post.title }}" width="200" height="150">
           {% endif %}
           <p>{{ post.content }}</p>
       </div>
   {% endfor %}

8. Uploading images
   - Go to Django admin, add or edit a post, and upload an image using the file field.

9. Serving images
   - When running python manage.py runserver, Django will serve images from /media/.
"""

def create_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 40
    for line in text.split('\n'):
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()

create_pdf("django_image_upload_guide.pdf", guide_text)
print("PDF guide created: django_image_upload_guide.pdf")