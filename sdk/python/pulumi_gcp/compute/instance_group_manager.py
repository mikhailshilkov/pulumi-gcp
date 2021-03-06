# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class InstanceGroupManager(pulumi.CustomResource):
    """
    The Google Compute Engine Instance Group Manager API creates and manages pools
    of homogeneous Compute Engine virtual machine instances from a common instance
    template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/manager)
    and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)
    
    ~> **Note:** Use [google_compute_region_instance_group_manager](/docs/providers/google/r/compute_region_instance_group_manager.html) to create a regional (multi-zone) instance group manager.
    """
    def __init__(__self__, __name__, __opts__=None, auto_healing_policies=None, base_instance_name=None, description=None, instance_template=None, name=None, named_ports=None, project=None, rolling_update_policy=None, target_pools=None, target_size=None, update_strategy=None, wait_for_instances=None, zone=None):
        """Create a InstanceGroupManager resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if auto_healing_policies and not isinstance(auto_healing_policies, dict):
            raise TypeError('Expected property auto_healing_policies to be a dict')
        __self__.auto_healing_policies = auto_healing_policies
        """
        ) The autohealing policies for this managed instance
        group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
        """
        __props__['autoHealingPolicies'] = auto_healing_policies

        if not base_instance_name:
            raise TypeError('Missing required property base_instance_name')
        elif not isinstance(base_instance_name, basestring):
            raise TypeError('Expected property base_instance_name to be a basestring')
        __self__.base_instance_name = base_instance_name
        """
        The base instance name to use for
        instances in this group. The value must be a valid
        [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
        are lowercase letters, numbers, and hyphens (-). Instances are named by
        appending a hyphen and a random four-character string to the base instance
        name.
        """
        __props__['baseInstanceName'] = base_instance_name

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        An optional textual description of the instance
        group manager.
        """
        __props__['description'] = description

        if not instance_template:
            raise TypeError('Missing required property instance_template')
        elif not isinstance(instance_template, basestring):
            raise TypeError('Expected property instance_template to be a basestring')
        __self__.instance_template = instance_template
        """
        The full URL to an instance template from
        which all new instances will be created.
        """
        __props__['instanceTemplate'] = instance_template

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the port.
        """
        __props__['name'] = name

        if named_ports and not isinstance(named_ports, list):
            raise TypeError('Expected property named_ports to be a list')
        __self__.named_ports = named_ports
        """
        The named port configuration. See the section below
        for details on configuration.
        """
        __props__['namedPorts'] = named_ports

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        __props__['project'] = project

        if rolling_update_policy and not isinstance(rolling_update_policy, dict):
            raise TypeError('Expected property rolling_update_policy to be a dict')
        __self__.rolling_update_policy = rolling_update_policy
        """
        ) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
        - - -
        """
        __props__['rollingUpdatePolicy'] = rolling_update_policy

        if target_pools and not isinstance(target_pools, list):
            raise TypeError('Expected property target_pools to be a list')
        __self__.target_pools = target_pools
        """
        The full URL of all target pools to which new
        instances in the group are added. Updating the target pools attribute does
        not affect existing instances.
        """
        __props__['targetPools'] = target_pools

        if target_size and not isinstance(target_size, int):
            raise TypeError('Expected property target_size to be a int')
        __self__.target_size = target_size
        """
        The target number of running instances for this managed
        instance group. This value should always be explicitly set unless this resource is attached to
        an autoscaler, in which case it should never be set. Defaults to `0`.
        """
        __props__['targetSize'] = target_size

        if update_strategy and not isinstance(update_strategy, basestring):
            raise TypeError('Expected property update_strategy to be a basestring')
        __self__.update_strategy = update_strategy
        """
        If the `instance_template`
        resource is modified, a value of `"NONE"` will prevent any of the managed
        instances from being restarted by Terraform. A value of `"RESTART"` will
        restart all of the instances at once. `"ROLLING_UPDATE"` is supported as [Beta feature].
        A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set
        """
        __props__['updateStrategy'] = update_strategy

        if wait_for_instances and not isinstance(wait_for_instances, bool):
            raise TypeError('Expected property wait_for_instances to be a bool')
        __self__.wait_for_instances = wait_for_instances
        """
        Whether to wait for all instances to be created/updated before
        returning. Note that if this is set to true and the operation does not succeed, Terraform will
        continue trying until it times out.
        """
        __props__['waitForInstances'] = wait_for_instances

        if zone and not isinstance(zone, basestring):
            raise TypeError('Expected property zone to be a basestring')
        __self__.zone = zone
        """
        The zone that instances in this group should be created
        in.
        """
        __props__['zone'] = zone

        __self__.fingerprint = pulumi.runtime.UNKNOWN
        """
        The fingerprint of the instance group manager.
        """
        __self__.instance_group = pulumi.runtime.UNKNOWN
        """
        The full URL of the instance group created by the manager.
        """
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URL of the created resource.
        """

        super(InstanceGroupManager, __self__).__init__(
            'gcp:compute/instanceGroupManager:InstanceGroupManager',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'autoHealingPolicies' in outs:
            self.auto_healing_policies = outs['autoHealingPolicies']
        if 'baseInstanceName' in outs:
            self.base_instance_name = outs['baseInstanceName']
        if 'description' in outs:
            self.description = outs['description']
        if 'fingerprint' in outs:
            self.fingerprint = outs['fingerprint']
        if 'instanceGroup' in outs:
            self.instance_group = outs['instanceGroup']
        if 'instanceTemplate' in outs:
            self.instance_template = outs['instanceTemplate']
        if 'name' in outs:
            self.name = outs['name']
        if 'namedPorts' in outs:
            self.named_ports = outs['namedPorts']
        if 'project' in outs:
            self.project = outs['project']
        if 'rollingUpdatePolicy' in outs:
            self.rolling_update_policy = outs['rollingUpdatePolicy']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
        if 'targetPools' in outs:
            self.target_pools = outs['targetPools']
        if 'targetSize' in outs:
            self.target_size = outs['targetSize']
        if 'updateStrategy' in outs:
            self.update_strategy = outs['updateStrategy']
        if 'waitForInstances' in outs:
            self.wait_for_instances = outs['waitForInstances']
        if 'zone' in outs:
            self.zone = outs['zone']
