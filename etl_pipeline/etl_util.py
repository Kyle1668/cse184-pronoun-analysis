"""Utilities for the Spark ETL pipeline
"""

from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import StringType, NullType
import string

__state_ids = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

__inverted_state_ids = dict((v, k) for k, v in __state_ids.items())


def __match_location_to_state(raw_location):
    """Takes in a string and returns the included US state ID.
       Return None if no state can be matched.

    Args:
        raw_location (str): The unformated state location. EX: "PAlo Alto, CA"

    Returns:
        str or None: The string state or None if no state can be matched
    """
    if raw_location is None or raw_location == "":
        return None

    formatted_location = raw_location
    state = None

    # Remove puncuation
    for char in string.punctuation:
        formatted_location = formatted_location.replace(char, ' ')

    formatted_location = formatted_location.split(" ")

    # Check if the element is a state code
    for element in formatted_location:
        if element in __state_ids and state is None:
            state = element
        elif element in __inverted_state_ids and state is None:
            state = __inverted_state_ids[element]

    return state


# The Pyspark function. Necessary tto be able to perform operations on a Pyspark data frame column.
__column_state_lambda_func = lambda x: __match_location_to_state(x)
match_location_to_state = UserDefinedFunction(__column_state_lambda_func,
                                              StringType())
