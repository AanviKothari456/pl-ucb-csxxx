import xml.etree.ElementTree as ET

class SkyColorQuestion:
    @staticmethod
    def generate(data):
        # This function is called to generate the parameters for the question
        # You could set up any initial data or select which version of the question to show
        pass

    @staticmethod
    def grade(data):
        # This function is called to grade the student's submission
        # The path to the uploaded file is in data['submitted_answers']['_files']['mean.xml'][0]
        file_info = data['submitted_answers']['_files']['mean.xml'][0]
        file_path = file_info['path']

        # Initialize variables
        is_correct = False
        total_score = 0
        student_count = 0

        try:
            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Assuming the XML structure is <scores><score>value</score></scores>
            scores = root.findall('score')
            student_count = len(scores)
            total_score = sum(float(score.text) for score in scores)

            # Calculate the mean score
            if student_count > 0:
                mean_score = total_score / student_count
                # You will need to determine the correct mean score from the Snap! activity
                # For demonstration, let's assume that the correct mean score is stored in a variable `correct_mean`
                correct_mean = 87.5  # This would be set by the question logic
                # Check if the student's calculated mean is correct
                is_correct = abs(mean_score - correct_mean) < 0.01  # Allowing some small margin for floating-point comparison

        except ET.ParseError as e:
            data['feedback'] = 'There was an error parsing the XML file: ' + str(e)
            data['score'] = 0.0
            return

        except Exception as e:
            data['feedback'] = 'An error occurred: ' + str(e)
            data['score'] = 0.0
            return

        # Set feedback and score
        if is_correct:
            data['feedback'] = 'Correct! The mean score was calculated accurately.'
            data['score'] = 1.0
        else:
            if student_count == 0:
                data['feedback'] = 'The list of scores provided was empty.'
            else:
                data['feedback'] = f'Incorrect. The calculated mean score was not accurate. Your mean score: {mean_score:.2f}'
            data['score'] = 0.0

        # Note: Ensure your grading logic matches the expectations of the question
        # and that the XML structure in `mean.xml` is as assumed in this script.
