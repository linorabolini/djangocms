# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from distutils.version import LooseVersion
from django.utils.translation import ugettext_lazy as _

from cms import __version__ as cms_version
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models, forms
from .utils import add_prefix_to_path, default_reverse

CMS_GTE_330 = LooseVersion(cms_version) >= LooseVersion('3.3.0')

TEMPLATE_PATH = 'aldryn_newsblog/plugins/{}.html'

class TemplatePrefixMixin(object):

    def get_render_template(self, context, instance, placeholder):
        render_template = instance.custom_template
        if not render_template or render_template == 'default':
            render_template = self.render_template
        if (hasattr(instance, 'app_config') and
                instance.app_config.template_prefix):
            return add_prefix_to_path(
                TEMPLATE_PATH.format(render_template),
                instance.app_config.template_prefix
            )
        return TEMPLATE_PATH.format(render_template)


class NewsBlogPlugin(TemplatePrefixMixin, CMSPluginBase):
    module = 'News & Blog'


class AdjustableCacheMixin(object):
    """
    For django CMS < 3.3.0 installations, we have no choice but to disable the
    cache where there is time-sensitive information. However, in later CMS
    versions, we can configure it with `get_cache_expiration()`.
    """
    if not CMS_GTE_330:
        cache = False

    def get_cache_expiration(self, request, instance, placeholder):
        return getattr(instance, 'cache_duration', 0)

    def get_fieldsets(self, request, obj=None):
        """
        Removes the cache_duration field from the displayed form if we're not
        using django CMS v3.3.0 or later.
        """
        fieldsets = super(AdjustableCacheMixin, self).get_fieldsets(request, obj=None)
        if CMS_GTE_330:
            return fieldsets

        field = 'cache_duration'
        for fieldset in fieldsets:
            new_fieldset = [
                item for item in fieldset[1]['fields'] if item != field]
            fieldset[1]['fields'] = tuple(new_fieldset)
        return fieldsets


@plugin_pool.register_plugin
class NewsBlogArchivePlugin(AdjustableCacheMixin, NewsBlogPlugin):
    render_template = 'archive'
    name = _('Archive')
    model = models.NewsBlogArchivePlugin
    form = forms.NewsBlogArchivePluginForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance

        queryset = models.Article.objects

        context['dates'] = queryset.get_months(
            request,
            namespace=instance.app_config.namespace
        )
        return context


@plugin_pool.register_plugin
class NewsBlogArticleSearchPlugin(NewsBlogPlugin):
    render_template = 'article_search'
    name = _('Article Search')
    model = models.NewsBlogArticleSearchPlugin
    form = forms.NewsBlogArticleSearchPluginForm

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['query_url'] = default_reverse('{0}:article-search'.format(
            instance.app_config.namespace), default=None)
        return context


@plugin_pool.register_plugin
class NewsBlogAuthorsPlugin(NewsBlogPlugin):
    render_template = 'authors'
    name = _('Authors')
    model = models.NewsBlogAuthorsPlugin
    form = forms.NewsBlogAuthorsPluginForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['authors_list'] = instance.get_authors(request)
        context['article_list_url'] = default_reverse(
            '{0}:article-list'.format(instance.app_config.namespace),
            default=None)

        return context


@plugin_pool.register_plugin
class NewsBlogCategoriesPlugin(NewsBlogPlugin):
    render_template = 'categories'
    name = _('Categories')
    model = models.NewsBlogCategoriesPlugin
    form = forms.NewsBlogCategoriesPluginForm
    cache = False

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['categories'] = instance.get_categories(request)
        context['article_list_url'] = default_reverse(
            '{0}:article-list'.format(instance.app_config.namespace),
            default=None)
        return context


@plugin_pool.register_plugin
class NewsBlogFeaturedArticlesPlugin(NewsBlogPlugin):
    render_template = 'featured_articles'
    name = _('Featured Articles')
    model = models.NewsBlogFeaturedArticlesPlugin
    form = forms.NewsBlogFeaturedArticlesPluginForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['article_list'] = instance.get_articles(request)
        return context


@plugin_pool.register_plugin
class NewsBlogLatestArticlesPlugin(AdjustableCacheMixin, NewsBlogPlugin):
    render_template = 'latest_articles'
    name = _('Latest Articles')
    model = models.NewsBlogLatestArticlesPlugin
    form = forms.NewsBlogLatestArticlesPluginForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['article_list'] = instance.get_articles(request)
        return context


@plugin_pool.register_plugin
class NewsBlogRelatedPlugin(AdjustableCacheMixin, NewsBlogPlugin):
    render_template = 'related_articles'
    name = _('Related Articles')
    model = models.NewsBlogRelatedPlugin
    form = forms.NewsBlogRelatedPluginForm

    def get_article(self, request):
        if request and request.resolver_match:
            view_name = request.resolver_match.view_name
            namespace = request.resolver_match.namespace
            if view_name == '{0}:article-detail'.format(namespace):
                article = models.Article.objects.active_translations(
                    slug=request.resolver_match.kwargs['slug'])
                if article.count() == 1:
                    return article[0]
        return None

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        article = self.get_article(request)
        if article:
            context['article'] = article
            context['article_list'] = instance.get_articles(article, request)

        return context


@plugin_pool.register_plugin
class NewsBlogTagsPlugin(NewsBlogPlugin):
    render_template = 'tags'
    name = _('Tags')
    model = models.NewsBlogTagsPlugin
    form = forms.NewsBlogTagsPluginForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['tags'] = instance.get_tags(request)
        context['article_list_url'] = default_reverse(
            '{0}:article-list'.format(instance.app_config.namespace),
            default=None)
        return context
