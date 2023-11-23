# Generated by Django 5.0rc1 on 2023-11-29 18:13

import pgtrigger.compiler
import pgtrigger.migrations
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desecapi", "0035_rename_perm_rrsets_tokendomainpolicy_write"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="tokendomainpolicy",
            name="default_policy_on_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="tokendomainpolicy",
            name="default_policy_on_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="tokendomainpolicy",
            name="default_policy_on_delete",
        ),
        migrations.RemoveConstraint(
            model_name="tokendomainpolicy",
            name="unique_entry",
        ),
        migrations.RemoveConstraint(
            model_name="tokendomainpolicy",
            name="unique_entry_null_domain",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="tokendomainpolicy",
            trigger=pgtrigger.compiler.Trigger(
                name="default_policy_primacy",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    constraint="CONSTRAINT",
                    func="\n                    IF\n                        EXISTS(SELECT * FROM desecapi_tokendomainpolicy WHERE token_id = COALESCE(NEW.token_id, OLD.token_id)) AND NOT EXISTS(\n                            SELECT * FROM desecapi_tokendomainpolicy WHERE token_id = COALESCE(NEW.token_id, OLD.token_id) AND domain_id IS NULL AND subname IS NULL AND type IS NULL\n                        )\n                    THEN\n                        RAISE EXCEPTION 'Token policies without a default policy are not allowed.';\n                    END IF;\n                    RETURN NULL;\n                ",
                    hash="5bac9e99f4e2fe1ba1cb410fb5ffd74a2e023a46",
                    operation="INSERT OR UPDATE OR DELETE",
                    pgid="pgtrigger_default_policy_primacy_9f1b1",
                    table="desecapi_tokendomainpolicy",
                    timing="DEFERRABLE INITIALLY DEFERRED",
                    when="AFTER",
                ),
            ),
        ),
        migrations.AddConstraint(
            model_name="tokendomainpolicy",
            constraint=models.UniqueConstraint(
                fields=("token", "domain", "subname", "type"),
                name="unique_policy",
                nulls_distinct=False,
            ),
        ),
    ]
