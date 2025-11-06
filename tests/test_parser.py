"""Tests for the parser module."""

import pytest
from nlu_extractor.parser import clean_description, parse_sample

def test_clean_description():
    """Test cleaning description with annotations."""
    input_text = 'hello when i log on using<annotation conceptref="entERROR_TYPE">mygov</annotation>details'
    expected = 'hello when i log on using details'
    assert clean_description(input_text) == expected

def test_parse_sample_simple():
    """Test parsing a simple sample without annotations."""
    input_line = '<sample intentref="INFO_PERSONAL_UPDATE" count="4" excluded="false" fullyVerified="false">i need to update my personal information</sample>'
    intent, desc = parse_sample(input_line)
    assert intent == "INFO_PERSONAL_UPDATE"
    assert desc == "i need to update my personal information"

def test_parse_sample_with_annotation():
    """Test parsing a sample with annotations."""
    input_line = '<sample intentref="TROUBLESHOOT_ERROR" count="1" excluded="false" fullyVerified="true">hello when i log on using<annotation conceptref="entERROR_TYPE">mygov</annotation>details</sample>'
    intent, desc = parse_sample(input_line)
    assert intent == "TROUBLESHOOT_ERROR"
    assert desc == "hello when i log on using details"