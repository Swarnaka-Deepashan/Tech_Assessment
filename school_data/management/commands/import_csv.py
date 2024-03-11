# import_csv.py
import csv
from django.core.management.base import BaseCommand
from school_data.models import School, StudentClass , Student, Subject, AssessmentAreas, Awards, Answers, Summary
from decimal import Decimal


# We create a new command class that inherits from BaseCommand
class Command(BaseCommand):
    help = 'Load data from CSV file into the Database'

    # add_arguments is used to add command line arguments for this command
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import.')

    # handle is the main method that will be run when you execute this command
    def handle(self, *args, **kwargs):
        # Open the CSV file using the argument provided to the command
        with open(kwargs['csv_file'], newline='') as csvfile:
            # Use csv.DictReader to read the CSV file into a dictionary format
            reader = csv.DictReader(csvfile)
            
            # Loop over each row in the CSV file
            for row in reader:
                #school_name = row['school_name']
                #year =row['year']	
                #StudentID = row['StudentID']
                First_Name = row['First Name']	
                Last_Name = row['Last Name']	
                #Year_Level = row['Year Level'] 	
                #StudentClass = row['Class']	
                #Subject = row['Subject']
                
                #Answers = row['Answers']
                #Correct_Answers = row['Correct Answers']
                #Question_Number	 = row['Question Number']
                #Subject_Contents = row['Subject Contents']
                #Assessment_Areas = row['Assessment Areas']
                #sydney_correct_count_percentage= row['sydney_correct_count_percentage']
                ##sydney_average_score = row['sydney_average_score']
                #sydney_participants	= row['sydney_participants']
                #student_score = row['student_score']
                #student_total_assessed = row['student_total_assessed']
                #student_area_assessed_score	= row['student_area_assessed_score']
                #total_area_assessed_score = row['total_area_assessed_score']
                #participant	= row['participant']
                #correct_answer_percentage_per_class	= row['correct_answer_percentage_per_class']
                #average_score	= row['average_score']
                #school_percentile	= row['school_percentile']
                #sydney_percentile	= row['sydney_percentile']
                #strength_status	= row['strength_status']
                #high_distinct_count	= row['high_distinct_count']
                #distinct_count	= row['distinct_count']
                #credit_count	= row['credit_count']
                #participant_count	= row['participant_count']
                #award= row['award']
                

                # Use the row data to create new model instances
                # For example, creating a new School for each row:
                school, created = School.objects.get_or_create(
                    name=row['school_name']  # Match CSV column names to model field names
                )
                
                # Output a message to the console
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))
                #print(row['school_name'],row['StudentID'],row['Answers'])
                    
                
                
                student_instance, created = Student.objects.get_or_create(
                    full_name= First_Name + " " + Last_Name  # Match CSV column names to model field names
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))

                
                studentClass, created = StudentClass.objects.get_or_create(
                    class_name= row['Class']  # Match CSV column names to model field names
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))


                assessment_area_instance, created = AssessmentAreas.objects.get_or_create(
                     name=row['Assessment Areas']  # Match CSV column names to model field names
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))


                
                awards_instance, created = Awards.objects.get_or_create(
                    name = row['award']   # Match CSV column names to model field names
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))




                subject_instance, created = Subject.objects.get_or_create(
                    subject_name= row['Subject'],
                    subject_score= row['student_score']   # Match CSV column names to model field names
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))


            

                answer_text = row['Answers']
                answer_obj, created = Answers.objects.get_or_create(answer_text=answer_text)

                correct_answer_text = row['Correct Answers']
                correct_answer_obj, created = Answers.objects.get_or_create(answer_text=correct_answer_text)



                
                summary, created = Summary.objects.get_or_create(
                    school= row['school_name'],
                    sydney_participant= row['sydney_participants'],
                    sydney_percentile= Decimal(row['sydney_percentile']), 
                    assessment_area=assessment_area_instance, 

                    award= awards_instance, 
                    correct_answer_percentage_per_class= Decimal(row['correct_answer_percentage_per_class']), 
                    #correct_answer= row['Correct Answers']
                    correct_answer= correct_answer_obj,   
                    student= student_instance, 
                    participant_id= Decimal(row['StudentID']), 

                    student_score= Decimal(row['student_score']), 
                    subject= subject_instance, 
                    category_id= Decimal(row['Question Number']), 
                    year_level_name= row['Year Level'], 
                    answer= answer_obj, 
                    
                    #given_answer=answer

                
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created school: {school.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'School already exists: {school.name}'))