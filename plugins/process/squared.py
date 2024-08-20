import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'squared',
    'title': {
        'en': 'Squared processor'
    },
    'description': {
        'en': 'An example process that takes a number or integer and returns '
              'the squared result'
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['squared'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'number-or-integer': {
            'title': 'Number',
            'description': 'number or integer',
            'schema': {
                'oneOf': ['number', 'integer'],
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,  # TODO how to use?
            'keywords': ['number']
        }
    },
    'outputs': {
        'squared': {
            'title': 'Squared',
            'description': 'An example process that takes a number or '
                           'integer and returns the squared result',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'number-or-integer': 3
        }
    }
}


class SquaredProcessor(BaseProcessor):
    """Squared Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.squared.SquaredProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        value = None
        mimetype = 'application/json'
        number_or_integer = data.get('number-or-integer')

        if number_or_integer is None:
            raise ProcessorExecuteError('Cannot process without input')

        # EXERCISE 8: fill in code to calculate the number or integer squared
        # and save to the "value" variable (that is defined as "None" at the
        # top of this function)
        # tip: ensure the input is indeed a number or integer!

        outputs = {
            'id': 'squared',
            'value': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<SquaredProcessor> {self.name}'
