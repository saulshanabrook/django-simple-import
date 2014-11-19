from .test_simple import SimpleTest

from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient


class SimpleTestTenantSchemas(SimpleTest, TenantTestCase):
    def setUp(self):
        self.client = TenantClient(self.tenant)
        self.host = self.tenant.domain_url
        super(SimpleTestTenantSchemas, self).setUp()
