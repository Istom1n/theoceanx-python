import os
import re
import traceback


def getEndpoint(service):
    return '{}{}'.format(os.environ['BASE_URL'], service)


pattern = re.compile(r'[\W+\w+]*get_variable_name\((\w+)\)')


def get_variable_name(x):
    return pattern.match(traceback.extract_stack(limit=2)[0][3]).group(1)
