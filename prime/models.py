from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
#RichTextField(blank=True, null=True)
class hero_section(models.Model): #1 views-hero
    main_title = models.CharField(max_length=100)
    main_subtitle_1 = models.CharField(max_length=100)
    main_subtitle_2 = models.CharField(max_length=100)
    main_subtitle_3 = models.CharField(max_length=100)
    main_img = models.ImageField(upload_to='media')
    about_img = models.ImageField(upload_to='media')
    about_title = models.CharField(max_length=100)
    about_subtitle_1 = models.CharField(max_length=100)
    about_subtitle_2 = models.CharField(max_length=100)
    about_subtitle_3 = models.CharField(max_length=100)
    about_text = models.TextField()
    resume_link = models.CharField(max_length=100)
    def __str__(self):
        return self.main_title


class skill_section(models.Model): #2 views-skill
    skill_title = models.CharField(max_length=100)
    skill_description = models.TextField()
    skill_link = models.CharField(max_length=200)
    def __str__(self):
        return self.skill_title

class skill_icon(models.Model): #for skills icon
    skill_section_image = models.ImageField(upload_to='media')
    skill_section_title = models.CharField(max_length=100)



class project_list(models.Model): #4 project
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='media')
    project_subtitle = models.CharField(max_length=100)
    project_duration = models.CharField(max_length=300)
    project_link = models.CharField(max_length=200)
    is_key_active = models.BooleanField(default=False)
    def __str__(self):
        return self.project_title


class course_list(models.Model): #3  views-course
    course_title_1 = models.CharField(max_length=100)
    course_image_1 = models.ImageField(upload_to='media')
    course_subtitle_1 = models.CharField(max_length=100)
    course_duration_1 = models.CharField(max_length=100)
    def __str__(self):
        return self.course_title_1

class acadamics_details(models.Model): #5 acadamics
    acadamics_id = models.CharField(max_length=100)
    acadamics_title = models.CharField(max_length=100)
    acadamics_subtitle = models.CharField(max_length=100)
    acadamics_duration = models.CharField(max_length=100)
    acadamics_id_1 = models.CharField(max_length=100)
    acadamics_title_1 = models.CharField(max_length=100)
    acadamics_subtitle_1 = models.CharField(max_length=100)
    acadamics_duration_1 = models.CharField(max_length=100)
    acadamics_id_2 = models.CharField(max_length=100)
    acadamics_title_2 = models.CharField(max_length=100)
    acadamics_subtitle_2 = models.CharField(max_length=100)
    acadamics_duration_2 = models.CharField(max_length=100)
    def __str__(self):
        return self.acadamics_title

class get_touch(models.Model): #6 touch
    get_name = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    get_email = models.CharField(max_length=100)
    def __str__(self):
        return self.get_name

class contact_us(models.Model): #7 contact
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.CharField(max_length=350)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Table"

class footer(models.Model): #8 foot
    created_by_name = models.CharField(max_length=100)
    created_by_link = models.CharField(max_length=100)
    created_by_terms = models.CharField(max_length=100)
    created_by_terms_link = models.CharField(max_length=100)
    created_b_year = models.CharField(max_length=100)
    def __str__(self):
        return self.created_by_name
    
