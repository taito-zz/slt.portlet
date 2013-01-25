from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from slt.portlet import _
from zope.i18nmessageid import MessageFactory
from zope.interface import implements


PloneMessageFactory = MessageFactory("plone")
SLTPolicyMessageFactory = MessageFactory("slt.policy")


class IMemberPortlet(IPortletDataProvider):
    '''A portlet which can render cart content.
    '''


class Assignment(base.Assignment):
    implements(IMemberPortlet)

    @property
    def title(self):
        """Title shown in @@manage-portlets"""
        return _(u"Member")


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('member.pt')

    @property
    def available(self):
        return self.items()

    def items(self):
        portal_state = self.context.restrictedTraverse('plone_portal_state')
        root_url = portal_state.navigation_root_url()
        membership = getToolByName(self.context, 'portal_membership')
        home_url = membership.getHomeUrl()
        return [
            {
                'available': not home_url,
                'title': PloneMessageFactory(u'Log in'),
                'url': '{}/login'.format(root_url),
            },
            # {
            #     'available': home_url,
            #     'title': SLTPolicyMessageFactory(u'Addresses'),
            #     'url': '{}/@@addresses'.format(home_url),
            # },
            {
                'available': home_url,
                'title': SLTPolicyMessageFactory(u'Orders'),
                'url': home_url,
            }
        ]


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
