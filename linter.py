"""This module exports the erlc util."""

from cuda_lint import Linter, util

class Erlc(Linter):

    """Provides an interface to erlc"""
    cmd = None
    executable = 'erlc'
    multiline = False
    syntax = ('Erlang')
    regex = (
        r".+:(?P<line>\d+):"
        r"(?:(?P<warning>\sWarning:\s)|(?P<error>\s))"
        r"+(?P<message>.+)"
    )
    base_cmd = ('')
    tempfile_suffix = 'erl'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(Erlc, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
