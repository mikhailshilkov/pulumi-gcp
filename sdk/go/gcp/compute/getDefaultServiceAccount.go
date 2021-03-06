// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve default service account for this project
func LookupDefaultServiceAccount(ctx *pulumi.Context, args *GetDefaultServiceAccountArgs) (*GetDefaultServiceAccountResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["email"] = args.Email
		inputs["project"] = args.Project
	}
	outputs, err := ctx.Invoke("gcp:compute/getDefaultServiceAccount:getDefaultServiceAccount", inputs)
	if err != nil {
		return nil, err
	}
	return &GetDefaultServiceAccountResult{
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getDefaultServiceAccount.
type GetDefaultServiceAccountArgs struct {
	Email interface{}
	// The project ID. If it is not provided, the provider project is used.
	Project interface{}
}

// A collection of values returned by getDefaultServiceAccount.
type GetDefaultServiceAccountResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
