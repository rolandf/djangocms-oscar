===============================
Integrate django CMS with Oscar
===============================

``djangocms-oscar`` eases integration between the content management system
django CMS and the e-commerce framework Oscar.

It is in an early stage, so use at your own risk. In it's current form, it
mainly exists to serve as a central point for collaboration. So keep those
pull requests coming! (:

Features
========

- ``base.html`` template which means that the django CMS toolbar works both on
  CMS pages and Oscar views
- Ships with default CMS templates that share the look with Oscar's sandbox
  pages
- Oscar's "Browse store" dropdown includes CMS pages
- A "Featured product" CMS plugin to be able to add individual products on
  CMS pages
- A "Viewed products" CMS plugin allows to add recently viewed products on
  CMS pages (same as Oscar's ``recently_viewed_products`` do)


Tested with
===========

* django-cms 3.4.2
* django-oscar 1.4
* Django 1.9.12
* Python 3.5.2


Installation
============

Grabbing the integration
------------------------
The latest release will be on PyPi, so you can just 
``pip install djangocms-oscar``. Or grab it from the ``master`` branch if you
prefer the bleeding edge.

Adding django CMS to an Oscar project
-------------------------------------

If you have a working Oscar project and want to add django CMS, follow the
instructions on `integrating django CMS`_.

You should also add at least one plugin to be able to set content. This
probably want to add `djangocms-text-ckeditor`_ to be able to include text.

.. _integrating django CMS: http://django-cms.readthedocs.org/en/latest/getting_started/installation/integrate.html
.. _djangocms-text-ckeditor: https://github.com/divio/djangocms-text-ckeditor

Adding Oscar to a django CMS project
------------------------------------

If you have a working django CMS project and want to integrate Oscar, follow
the instructions on `getting started with Oscar`_.

.. _getting started with Oscar: http://django-oscar.readthedocs.org/en/latest/internals/getting_started.html

URLs
----

There's two options to include Oscar's URLs.

This integration comes with an app hook for django CMS. So you can just let
django CMS take care of URL handling by adding Oscar to a CMS page.

If you prefer to hard-wire Oscar's URLs into your project's ``urls.py``,
make sure that django CMS's URLs come after Oscar's.urls::

     urlplatterns = [
        ...
        (r'^shop/', include(shop.urls)),
        (r'^', include('cms.urls')),
        ...
     ]

Setting up the integration
--------------------------

To get started using ``djangocms-oscar``:

- install it with ``pip``::

    $ pip install djangocms-oscar

- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangocms_oscar',
        ...
    )

- To use the supplied templates, they need to be loaded before Oscar's::

    from oscar import OSCAR_MAIN_TEMPLATE_DIR
    from djangocms_oscar import OSCAR_CMS_TEMPLATE_DIR

    TEMPLATE_DIRS = (
        location('templates'),
        OSCAR_CMS_TEMPLATE_DIR,
        OSCAR_MAIN_TEMPLATE_DIR,
    )

- Plugins allows to add some templates. Place product.html or viewed_products.html
  to the appropriate folder, e.g.
  djangocms_oscar/plugins/featured_product/my_product/
  or
  djangocms_oscar/plugins/viewed_products/index/
  and set variables::

    DJANGOCMS_OSCAR_PRODUCT_TEMPLATES = [('my_product', _('My lovely product'))]
    DJANGOCMS_OSCAR_VIEWED_TEMPLATES = [('index', _('For index page'))]


- Run ``migrate djangocms_oscar``.

Optional settings
-----------------

Besides customised Oscar templates, ``djangocms-oscar`` comes with a set of
CMS templates that are based on Oscar's default templates.
They're a good starting point and can be used like this::

    # settings.py

    CMS_TEMPLATES = (
        ('djangocms_oscar/full_width.html', 'Full width (no sidebars)'),
        ('djangocms_oscar/with_sidebar.html', 'Two column (left-hand sidebar)'),
    )

If you want Oscar's homepage to be controlled by django CMS, set it like this::

    # settings.py

    from django.core.urlresolvers import reverse_lazy
    OSCAR_HOMEPAGE = reverse_lazy('pages-root')

