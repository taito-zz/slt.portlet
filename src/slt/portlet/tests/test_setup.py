from Products.CMFCore.utils import getToolByName
from slt.portlet.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('slt.portlet'))

    def test_browserlayer(self):
        from slt.portlet.browser.interfaces import ISltPortletLayer
        from plone.browserlayer import utils
        self.assertIn(ISltPortletLayer, utils.registered_layers())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.portlet'])
        self.assertFalse(installer.isProductInstalled('slt.portlet'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.portlet'])
        from slt.portlet.browser.interfaces import ISltPortletLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISltPortletLayer, utils.registered_layers())
