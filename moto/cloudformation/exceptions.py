from __future__ import unicode_literals
from werkzeug.exceptions import BadRequest
from jinja2 import Template


class UnformattedGetAttTemplateException(Exception):
    description = 'Template error: resource {0} does not support attribute type {1} in Fn::GetAtt'
    status_code = 400


class ValidationError(BadRequest):
    def __init__(self, name_or_id):
        template = Template(ERROR_RESPONSE)
        super(ValidationError, self).__init__()
        self.description = template.render(
            code="ValidationError",
            messgae="Stack:{0} does not exist".format(name_or_id),
        )


class MissingParameterError(BadRequest):
    def __init__(self, parameter_name):
        template = Template(ERROR_RESPONSE)
        super(MissingParameterError, self).__init__()
        self.description = template.render(
            code="Missing Parameter",
            messgae="Missing parameter {0}".format(parameter_name),
        )


ERROR_RESPONSE = """<ErrorResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <Error>
    <Type>Sender</Type>
    <Code>{{ code }}</Code>
    <Message>{{ message }}</Message>
  </Error>
  <RequestId>cf4c737e-5ae2-11e4-a7c9-ad44eEXAMPLE</RequestId>
</ErrorResponse>
"""