from django import forms

from .models import Course, Lesson


class CreateLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "description", "preview", "video_link"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Название урока",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Описание урока",
            }
        )
        self.fields["preview"].widget.attrs.update(
            {
                "class": "input-group rounded-2 mb-2",
            }
        )
        self.fields["video_link"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Сслыка на видеоурок",
            }
        )


class CreateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "preview", "description", "lessons", "students"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Название курса",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Описание урока",
            }
        )
        self.fields["preview"].widget.attrs.update(
            {
                "class": "input-group rounded-2 mb-2",
            }
        )
        self.fields["lessons"].widget.attrs.update(
            {
                "class": "input-group rounded-2 mb-2",
            }
        )
        self.fields["students"].widget.attrs.update(
            {
                "class": "input-group rounded-2 mb-2",
            }
        )
