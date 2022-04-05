from django.forms import ModelForm

from .models import *



# class CkEditorForm(forms.Form):
#     ckeditor_standard_example = RichTextFormField()
#     ckeditor_upload_example = RichTextUploadingFormField(
#         config_name="my-custom-toolbar"
#     )

    
class post_article_forms (ModelForm):
    class Meta: 
        model = Articles
        fields = ["title",
        "thumbnail", "content",
        "category",
        "hashtag",]

  # "image2", "content_part2",
        # "image3", "content_part3",
        # "image4", "content_part4",
        # "image5", "content_part5",
        # "image6", "content_part6",