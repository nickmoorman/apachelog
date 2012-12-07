from distutils.core import setup

# From inspecting Mark Pilgrims feedparser...
# patch distutils if it can't cope with the "classifiers" or "download_url"
# keywords (prior to python 2.3.0).
from distutils.dist import DistributionMetadata
if not hasattr(DistributionMetadata,'classifiers'):
    DistributionMetadata.classifiers = None
    
setup(
    name = 'apachelog',
    version = '1.1',
    description = 'Access log parser in python, ported from '\
    'Peter Hickman\'s Apache::LogRegex Perl moduleUniversal.',
    long_description = """\
Apache Log Parser
-----------------

Parser for extracting fields from a single line of an Apache
access.log (should work for other servers conforming to the
Common Log Format).

Create the parser with the log format from your server .conf
file, parse lines to get dict corresponding to fields defined
in the log format.


""",
    author='Harry Fuecks',
    author_email = 'hfuecks@gmail.com',
    url = 'http://code.google.com/p/apachelog',
    license = "Artistic License / GPLv2",
    platforms = ['POSIX', 'Windows'],
    keywords = ['apache', 'log', 'parser'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Artistic License",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: System :: Logging",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        ],
    py_modules = ['apachelog',]
    )
