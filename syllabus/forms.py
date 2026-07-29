from django import forms

from .models import Course, Lesson


class Create(forms.ModelForm):
    pass
    # class Meta:
    #     model = Message
    #     fields = [
    #         "subject",
    #         "content",
    #         "attached_file",
    #     ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["subject"].widget.attrs.update(
    #         {
    #             "class": "form-control-M",
    #             "placeholder": "Тема сообщения",
    #         }
    #     )
    #     self.fields["content"].widget.attrs.update(
    #         {
    #             "class": "form-control-M",
    #             "placeholder": "Содержание сообщения ",
    #         }
    #     )
    #     self.fields["attached_file"].widget.attrs.update(
    #         {
    #             "class": "form-control-M",
    #             "placeholder": "Дополнительны файлы ",
    #         }
    #     )
