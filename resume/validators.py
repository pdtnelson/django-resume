from django.core.exceptions import ValidationError
from django.core.files import File
import json
import os
from jsonschema import validate as jsonschema_validate, ValidationError as JsonSchemaValidationError

##
# Validator to ensure the uploaded file is a valid JSON Resume
# and complies with the JSON Resume specification.
##
def validate_resume_is_vaild_json(value: File):
    if not value.name.endswith('.json'):
        raise ValidationError("File must be a JSON file.")
    try:
        data = json.load(value)
    except json.JSONDecodeError:
        raise ValidationError("JSON Formatting is invalid.")

    # Load the JSON schema from file
    schema_path = os.path.join(os.path.dirname(__file__), "json_schemas/resume_schema.json")
    with open(schema_path, 'r') as schema_file:
        schema = json.load(schema_file)

    try:
        jsonschema_validate(instance=data, schema=schema)
    except JsonSchemaValidationError as ex:
        raise ValidationError(f"The provided JSON does not comply with the resume schema: {ex.message}")

    # Reset the file pointer to the beginning after reading
    value.seek(0)
  