# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ProjectSink(pulumi.CustomResource):
    """
    Manages a project-level logging sink. For more information see
    [the official documentation](https://cloud.google.com/logging/docs/),
    [Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs)
    and
    [API](https://cloud.google.com/logging/docs/reference/v2/rest/).
    
    Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
    granted to the credentials used with terraform.
    """
    def __init__(__self__, __name__, __opts__=None, destination=None, filter=None, name=None, project=None, unique_writer_identity=None):
        """Create a ProjectSink resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not destination:
            raise TypeError('Missing required property destination')
        elif not isinstance(destination, basestring):
            raise TypeError('Expected property destination to be a basestring')
        __self__.destination = destination
        """
        The destination of the sink (or, in other words, where logs are written to). Can be a
        Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
        ```
        "storage.googleapis.com/[GCS_BUCKET]"
        "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
        "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
        ```
        The writer associated with the sink must have access to write to the above resource.
        """
        __props__['destination'] = destination

        if filter and not isinstance(filter, basestring):
            raise TypeError('Expected property filter to be a basestring')
        __self__.filter = filter
        """
        The filter to apply when exporting logs. Only log entries that match the filter are exported.
        See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
        write a filter.
        """
        __props__['filter'] = filter

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the logging sink.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project to create the sink in. If omitted, the project associated with the provider is
        used.
        """
        __props__['project'] = project

        if unique_writer_identity and not isinstance(unique_writer_identity, bool):
            raise TypeError('Expected property unique_writer_identity to be a bool')
        __self__.unique_writer_identity = unique_writer_identity
        """
        Whether or not to create a unique identity associated with this sink. If `false`
        (the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
        then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
        must set `unique_writer_identity` to true.
        """
        __props__['uniqueWriterIdentity'] = unique_writer_identity

        __self__.writer_identity = pulumi.runtime.UNKNOWN
        """
        The identity associated with this sink. This identity must be granted write access to the
        configured `destination`.
        """

        super(ProjectSink, __self__).__init__(
            'gcp:logging/projectSink:ProjectSink',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'destination' in outs:
            self.destination = outs['destination']
        if 'filter' in outs:
            self.filter = outs['filter']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'uniqueWriterIdentity' in outs:
            self.unique_writer_identity = outs['uniqueWriterIdentity']
        if 'writerIdentity' in outs:
            self.writer_identity = outs['writerIdentity']
