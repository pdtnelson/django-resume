from django.test import TestCase
from .validators import validate_resume_is_vaild_json
from django.core.exceptions import ValidationError
from django.core.files import File
import json

class ResumeValidatorTests(TestCase):
  def test_resume_validator_successful_with_valid_resume(self):
      # Load the valid resume data
      with open('resume/test_resources/valid_resume.json', 'r') as f:
        valid_file =File(f, name="valid_resume.json")
        try:
            validate_resume_is_vaild_json(valid_file)
        except ValidationError:
            self.fail("validate_resume_is_vaild_json raised ValidationError unexpectedly!")

  def test_resume_validator_raises_exception_on_invalid_resume(self):

      # Load the invalid resume data
      # Ensure the data is invalid for the JSON Resume specification
      # Create a SimpleUploadedFile instance with the invalid data
      # Open the invalid JSON file as a Django File object
      with open('resume/test_resources/invalid_resume.json', 'rb') as f:
        invalid_file = File(f, name="invalid_resume.json")
        # Assert that a ValidationError is raised when validating the invalid resume
        with self.assertRaises(ValidationError):
            validate_resume_is_vaild_json(invalid_file)
