import unittest
from troposphere.config import SourceDetails, ONE_HOUR


def eadf_SourceDetails(self):
    SourceDetails(
        EventSource="esource",
        MaximumExecutionFrequency=ONE_HOUR,
        MessageType="mtype",
    ).to_dict()

def new_source_DetailsMaximumExecutionFrequency(self):
    with self.assertRaises(ValueError):
        SourceDetails(
            EventSource="esource",
            MaximumExecutionFrequency="foo",
            MessageType="mtype",
        ).to_dict()


if __name__ == '__main__':
    unittest.main()

