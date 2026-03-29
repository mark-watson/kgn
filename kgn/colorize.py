from io import StringIO

def blue(s):
    return '{}{}{}'.format('\x1b[94m', s, '\x1b[0m')

def red(s):
    return '{}{}{}'.format('\x1b[91m', s, '\x1b[0m')

def green(s):
    return '{}{}{}'.format('\x1b[92m', s, '\x1b[0m')

def pink(s):
    return '{}{}{}'.format('\x1b[95m', s, '\x1b[0m')

def bold(s):
    return '{}{}{}'.format('\x1b[1m', s, '\x1b[0m')

def tokenize_keep_uris(s):
    return s.split()

def colorize_sparql(s):
    # Only replace dots with spaces if they are not inside <URI> brackets
    # A simple way is to replace dots that have a space before or after, 
    # but that's not perfect. Better to just handle it during tokenization.
    s = s.replace('{', ' { ').replace('}', ' } ')
    # For simplicity, we just won't replace dots here and let the tokens be.
    # The original code's replacement was too aggressive.
    tokens = s.split()
    ret = StringIO()
    for token in tokens:
        # If token ends with a dot, split it (it's a SPARQL triple terminator)
        clean_token = token
        suffix = ''
        if token.endswith('.') and not token.startswith('<'):
            clean_token = token[:-1]
            suffix = ' . '
        
        (ret.write(red(clean_token)) if len(clean_token) > 0 and clean_token[0] == '?' else 
         ret.write(blue(clean_token)) if clean_token.lower() in ['where', 'select', 'distinct', 'option', 'filter', 'bind', 'optional', 'coalesce', 'as', 'limit'] else
         ret.write(bold(clean_token)) if len(clean_token) > 0 and clean_token[0] == '<' else 
         ret.write(clean_token)
        ) if len(clean_token) > 0 else None
        
        if suffix:
            ret.write(suffix)
        else:
            ret.write(' ')
            
    ret.seek(0)
    return ret.read()

