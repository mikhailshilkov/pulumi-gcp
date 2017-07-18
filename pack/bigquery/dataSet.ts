// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class DataSet extends lumi.NamedResource implements DataSetArgs {
    public /*out*/ readonly creationTime: number;
    public readonly datasetId: string;
    public readonly defaultTableExpirationMs?: number;
    public readonly description?: string;
    public /*out*/ readonly etag: string;
    public readonly friendlyName?: string;
    public readonly labels?: {[key: string]: string};
    public /*out*/ readonly lastModifiedTime: number;
    public readonly location?: string;
    public readonly project?: string;
    public /*out*/ readonly selfLink: string;

    constructor(name: string, args: DataSetArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.datasetId, "") === undefined) {
            throw new Error("Property argument 'datasetId' is required, but was missing");
        }
        this.datasetId = args.datasetId;
        this.defaultTableExpirationMs = args.defaultTableExpirationMs;
        this.description = args.description;
        this.friendlyName = args.friendlyName;
        this.labels = args.labels;
        this.location = args.location;
        this.project = args.project;
    }
}

export interface DataSetArgs {
    readonly datasetId: string;
    readonly defaultTableExpirationMs?: number;
    readonly description?: string;
    readonly friendlyName?: string;
    readonly labels?: {[key: string]: string};
    readonly location?: string;
    readonly project?: string;
}

