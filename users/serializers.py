import logging
from rest_framework import serializers

from syllabus.serializers import CourseSerializer
from users.models import User

logger_serializers_users = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_serializers_users.addHandler(file_handler)
logger_serializers_users.setLevel(logging.INFO)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "is_active", "groups"]

class UserTrainingSerializer(serializers.ModelSerializer):
    # course = serializers.CharField(source='course_set.all')
    course = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "username", "first_name", "last_name",
            "is_active", "groups", "course"
        ]

    def get_course(self, instance):
        qeryset_courses = instance.course_set.all()
        logger_serializers_users.info(qeryset_courses)
        
        courses_str = ', '.join(obj.title for obj in qeryset_courses)
        return courses_str
