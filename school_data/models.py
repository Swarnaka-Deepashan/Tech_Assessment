from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class AssessmentAreas(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Awards(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    #subject_score = models.IntegerField()
    subject_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.subject_name

class Answers(models.Model):
    answer_text = models.TextField()  # Assuming 'Answers' would contain textual answers

    def __str__(self):
        return self.answer_text[:50]  # Returns the first 50 characters of the answer

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.CharField(max_length=255)
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_id = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='correct_answer')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant_id = models.CharField(max_length=255)
    student_score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.CharField(max_length=255)
    year_level_name = models.CharField(max_length=255)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='given_answer')
    given_answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='summary_given_answers')


    def __str__(self):
        return f"{self.school.name} - {self.student.full_name} Summary"
