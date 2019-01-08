#!/usr/bin/env python

"""
This python script is used to build out the schemas for AUD based on the schemas provided
in the source code for Pixar's USD

This allows aud to stay up to date with changes in Pixar's schema without requiring
code changes or without requiring manual implementations for everything.
"""

from aud import __build__