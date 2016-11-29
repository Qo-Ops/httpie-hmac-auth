"""
AWS Auth plugin for HTTPie.

"""
import datetime
import base64
import hashlib
import hmac

from httpie.plugins import AuthPlugin

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

__version__ = '0.0.1'
__author__ = 'Ilya Gladyshev'
__licence__ = 'MIT'


class AWSAuth:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key.encode('ascii')

    def __call__(self, r):
        if not self.access_key or not self.secret_key:
            ValueError("Both access key and secret key must be provided")
        method = r.method

        content_type = r.headers.get('content-type')
        if not content_type:
            content_type = ''

        content_md5 = r.headers.get('content-md5')
        if not content_md5:
            if content_type:
                m = hashlib.md5()
                m.update(r.body)
                content_md5 = base64.encodestring(m.digest()).rstrip()
                r.headers['Content-MD5'] = content_md5
            else:
                content_md5 = ''

        httpdate = r.headers.get('date')
        if not httpdate:
            now = datetime.datetime.utcnow()
            httpdate = now.strftime('%a, %d %b %Y %H:%M:%S GMT')
            r.headers['Date'] = httpdate

        url = urlparse(r.url)
        path = url.path
        canonical_headers = [k + ':' + v for k, v in r.headers.items() if k.startswith('x-amz-')]
        signature_args = [method, content_md5, content_type, httpdate]
        signature_args += canonical_headers
        signature_args.append(path)
        string_to_sign = '\n'.join(signature_args).encode('utf-8')
        digest = hmac.new(self.secret_key, string_to_sign, hashlib.sha1).digest()
        signature = base64.encodestring(digest).rstrip().decode('utf-8')
        r.headers['Authorization'] = 'AWS %s:%s' % (self.access_key, signature)
        return r


class AWSAuthPlugin(AuthPlugin):

    name = 'AWS S3 authentication version 2'
    auth_type = 'aws'
    description = 'Adds signature to the request as amazon AWS requires'

    def get_auth(self, access_key, secret_key):
        return AWSAuth(access_key, secret_key)
