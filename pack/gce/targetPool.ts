// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class TargetPool extends lumi.NamedResource implements TargetPoolArgs {
    public readonly backupPool?: string;
    public readonly description?: string;
    public readonly failoverRatio?: number;
    public readonly healthChecks?: string[];
    public readonly instances: string[];
    public readonly targetPoolName?: string;
    public readonly project: string;
    public readonly region: string;
    public /*out*/ readonly selfLink: string;
    public readonly sessionAffinity?: string;

    constructor(name: string, args: TargetPoolArgs) {
        super(name);
        this.backupPool = args.backupPool;
        this.description = args.description;
        this.failoverRatio = args.failoverRatio;
        this.healthChecks = args.healthChecks;
        this.instances = args.instances;
        this.targetPoolName = args.targetPoolName;
        this.project = args.project;
        this.region = args.region;
        this.sessionAffinity = args.sessionAffinity;
    }
}

export interface TargetPoolArgs {
    readonly backupPool?: string;
    readonly description?: string;
    readonly failoverRatio?: number;
    readonly healthChecks?: string[];
    readonly instances?: string[];
    readonly targetPoolName?: string;
    readonly project?: string;
    readonly region?: string;
    readonly sessionAffinity?: string;
}

