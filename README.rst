httpie-aws-auth
================
Authentication plugin for `HTTPie <https://github.com/jkbrzt/httpie>`_.
The plugin provides authentication signature (version 2) as specified in `AWS guidelines <https://s3.amazonaws.com/doc/s3-developer-guide/RESTAuthentication.html>`_.

The signature includes:

* Method
* Content-MD5
* Content-Type
* Date
* Canonicalized amz headers
* Canonicalized resource

Usage
-----

.. code-block:: bash

    $ http --auth-type=aws --auth='client:secret' example.org


License
-------
Available under the MIT License.