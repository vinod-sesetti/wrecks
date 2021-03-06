# -*- coding: utf-8 -*-

#from ..cache import get_cache_key, get_hexdigest, get_hashed_mtime
#from ..settings import COFFEESCRIPT_EXECUTABLE, COFFEESCRIPT_USE_CACHE,\
#    COFFEESCRIPT_CACHE_TIMEOUT, COFFEESCRIPT_OUTPUT_DIR]

from django.conf import settings
#from django.core.cache import cache
from django.template.base import Library, Node

from django.utils.safestring import mark_safe

import logging
import shlex
import subprocess
#import os

try:
    from shpaml import convert_text
except:
    from shpaml.shpaml import convert_text


#### globals

trace = 0
logger = logging.getLogger("django_stylus")
register = Library()


#### functions

def compileit (source):
    args = shlex.split("%s " % getattr (settings, 'STYLUS_EXECUTABLE', 'stylus'))

    p = subprocess.Popen (args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, errors = p.communicate(source.encode("utf-8"))

    print out, errors

    if out:
        return out.decode("utf-8")
    elif errors:
        return errors.decode("utf-8")  # maybe raise an exception here?

    return u""


#### templatetags

@register.filter
def minaml (value):
    if trace:
        print
        print 'BEFORE:', value

    result = convert_text (value)

    if trace:
        print
        print 'AFTER:', result

    #if settings.DEBUG:
    #    result += '<!-- \n\nBEFORE:\n%s\n\nAFTER:\n%s\n\n -->' % (value, result)

    return result


@register.filter
def stylus_filter (value):
    #print value
    return compileit (value)
    return mark_safe ('xyz' + value + 'abc')

    '''

    OK this is a test - here's the django request var: {{ request }}!


    OK that didn't work, let's try it again:

    {% firstof request var2 var3 "fallback value" %}

    so there.
    '''


'''
class InlineCoffeescriptNode(Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)

        if COFFEESCRIPT_USE_CACHE:
            cache_key = get_cache_key(get_hexdigest(output))
            cached = cache.get(cache_key, None)
            if cached is not None:
                return cached
            output = self.compile(output)
            cache.set(cache_key, output, COFFEESCRIPT_CACHE_TIMEOUT)
            return output
        else:
            return self.compile(output)


@register.tag(name="inlinecoffeescript")
def do_inlinecoffeescript(parser, token):
    nodelist = parser.parse(("endinlinecoffeescript",))
    parser.delete_first_token()
    return InlineCoffeescriptNode(nodelist)


@register.simple_tag
def coffeescript(path):

    try:
        STATIC_ROOT = settings.STATIC_ROOT
    except AttributeError:
        STATIC_ROOT = settings.MEDIA_ROOT

    full_path = os.path.join(STATIC_ROOT, path)
    filename = os.path.split(path)[-1]

    output_directory = os.path.join(STATIC_ROOT, COFFEESCRIPT_OUTPUT_DIR, os.path.dirname(path))

    hashed_mtime = get_hashed_mtime(full_path)

    if filename.endswith(".coffee"):
        base_filename = filename[:-7]
    else:
        base_filename = filename

    output_path = os.path.join(output_directory, "%s-%s.js" % (base_filename, hashed_mtime))

    if not os.path.exists(output_path):
        source_file = open(full_path)
        source = source_file.read()
        source_file.close()

        args = shlex.split("%s -c -s -p" % COFFEESCRIPT_EXECUTABLE)
        p = subprocess.Popen(args, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, errors = p.communicate(source)
        if out:
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            compiled_file = open(output_path, "w+")
            compiled_file.write(out)
            compiled_file.close()

            # Remove old files
            compiled_filename = os.path.split(output_path)[-1]
            for filename in os.listdir(output_directory):
                if filename.startswith(base_filename) and filename != compiled_filename:
                    os.remove(os.path.join(output_directory, filename))
        elif errors:
            logger.error(errors)
            return path

    return output_path[len(STATIC_ROOT):].replace(os.sep, '/').lstrip("/")
'''