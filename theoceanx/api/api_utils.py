import os
import re
import traceback

from _sre import SRE_Pattern


def get_endpoint(service: str) -> str:
    return '{}{}'.format(os.environ['BASE_URL'], service)


pattern: SRE_Pattern = re.compile(r'[\W+\w+]*get_variable_name\((\w+)\)')


def get_variable_name(x: str) -> SRE_Pattern:
    return pattern.match(traceback.extract_stack(limit=2)[0][3]).group(1)
