import climmob.plugins as plugins
import climmob.plugins.utilities as u


class RTBBranding(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfig)
    plugins.implements(plugins.ISchema)

    def update_config(self, config):
        u.addTemplatesDirectory(config, "templates")
        u.addStaticView(config, "rtb", "static")

    def update_schema(self, config):
        return [u.addFieldToQuestionSchema("co_term_id", "Crop Ontology Term ID")]
