#!/bin/sh

# we need to run the test command with different settings to test different
# DATABASES settings
# can't overide during tests: https://code.djangoproject.com/ticket/19031

if ! [ "$TEST_TYPE" = "tenant" ]; then
    echo
    echo 'RUNNING NOMRAL TESTS'
    echo
    django-admin.py test --noinput --settings=test.settings test.test_simple
fi;
if ! [ "$TEST_TYPE" = "normal" ]; then
    echo
    echo 'RUNNING WITH TENANT SCHEMA TESTS'
    echo
    django-admin.py test --noinput --settings=test.settings_tenant_schemas test.test_simple_tenant_schemas.SimpleTestTenantSchemas
fi;
