# swagger-client
Web Application Scanning Configuration API Documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Dynamic Analysis identifier.
scans = [swagger_client.ScanRequest()] # list[ScanRequest] | scans

try:
    # Adds one or more new URLs to the Dynamic Analysis. You can also add URLs by updating the analysis.
    api_instance.add_scans_to_analysis_using_post(analysis_id, scans)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->add_scans_to_analysis_using_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.veracode.com/was/configservice/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V1AnalysisApiApi* | [**add_scans_to_analysis_using_post**](docs/V1AnalysisApiApi.md#add_scans_to_analysis_using_post) | **POST** /analyses/{analysis_id}/scans | Adds one or more new URLs to the Dynamic Analysis. You can also add URLs by updating the analysis.
*V1AnalysisApiApi* | [**create_analysis_using_post**](docs/V1AnalysisApiApi.md#create_analysis_using_post) | **POST** /analyses | Creates a new Dynamic Analysis for the account, if the user has access to the account. Returns the URL of the  new analysis in the HTTP response header. 
*V1AnalysisApiApi* | [**delete_analysis_using_delete**](docs/V1AnalysisApiApi.md#delete_analysis_using_delete) | **DELETE** /analyses/{analysis_id} | Deletes the Dynamic Analysis for the provided identifier. You can only hard-delete an analysis if it has never run.
*V1AnalysisApiApi* | [**delete_scan_using_delete**](docs/V1AnalysisApiApi.md#delete_scan_using_delete) | **DELETE** /scans/{scan_id} | Deletes the URL scan with the specified dentifier. You can only delete scans that have never run.
*V1AnalysisApiApi* | [**find_all_scans_for_analysis_using_get**](docs/V1AnalysisApiApi.md#find_all_scans_for_analysis_using_get) | **GET** /analyses/{analysis_id}/scans | Returns a list of all occurrences of the Dynamic Analysis.
*V1AnalysisApiApi* | [**find_analysis_audits_by_id_using_get**](docs/V1AnalysisApiApi.md#find_analysis_audits_by_id_using_get) | **GET** /analyses/{analysis_id}/audits | Returns a list of audit logs for the specified Dynamic Analysis.
*V1AnalysisApiApi* | [**find_analysis_by_id_using_get**](docs/V1AnalysisApiApi.md#find_analysis_by_id_using_get) | **GET** /analyses/{analysis_id} | Returns the Dynamic Analysis for the provided identifier.
*V1AnalysisApiApi* | [**find_analysis_summaries_using_get**](docs/V1AnalysisApiApi.md#find_analysis_summaries_using_get) | **GET** /analyses | Returns a list of Dynamic Analyses for the current organization or a specified, alternate organization.
*V1AnalysisApiApi* | [**find_platform_applications_using_get**](docs/V1AnalysisApiApi.md#find_platform_applications_using_get) | **GET** /platform_applications | Returns a list of applications in the Veracode Platform.
*V1AnalysisApiApi* | [**find_scan_audits_by_id_using_get**](docs/V1AnalysisApiApi.md#find_scan_audits_by_id_using_get) | **GET** /scans/{scan_id}/audits | Returns a list of audits (activity logs) for the provided URL scan identifier.
*V1AnalysisApiApi* | [**find_scan_by_id_using_get**](docs/V1AnalysisApiApi.md#find_scan_by_id_using_get) | **GET** /scans/{scan_id} | Returns a URL scan.
*V1AnalysisApiApi* | [**get_scan_configuration_using_get**](docs/V1AnalysisApiApi.md#get_scan_configuration_using_get) | **GET** /scans/{scan_id}/configuration | Returns the configuration for the specified URL scan.
*V1AnalysisApiApi* | [**update_analysis_using_put**](docs/V1AnalysisApiApi.md#update_analysis_using_put) | **PUT** /analyses/{analysis_id} | Updates a Dynamic Analysis for the provided identifier.
*V1AnalysisApiApi* | [**update_scan_configuration_using_put**](docs/V1AnalysisApiApi.md#update_scan_configuration_using_put) | **PUT** /scans/{scan_id}/configuration | Updates the configuration for the specified URL scan.
*V1AnalysisApiApi* | [**update_scan_using_put**](docs/V1AnalysisApiApi.md#update_scan_using_put) | **PUT** /scans/{scan_id} | Updates the URL scan request.
*V1ConfigurationApiApi* | [**find_code_group_by_id_using_get**](docs/V1ConfigurationApiApi.md#find_code_group_by_id_using_get) | **GET** /code_groups/{name} | Returns the details of a code group.
*V1ConfigurationApiApi* | [**get_account_scan_capacity_summary_using_get**](docs/V1ConfigurationApiApi.md#get_account_scan_capacity_summary_using_get) | **GET** /scan_capacity_summary | Returns the scan capacity summary for the organization.
*V1ConfigurationApiApi* | [**get_code_groups_using_get**](docs/V1ConfigurationApiApi.md#get_code_groups_using_get) | **GET** /code_groups | Returns a list of code groups
*V1ConfigurationApiApi* | [**get_default_configuration_using_get**](docs/V1ConfigurationApiApi.md#get_default_configuration_using_get) | **GET** /configuration | Returns the default Dynamic Analysis configuration for the organization.
*V1OccurrenceApiApi* | [**find_analysis_occurrence_by_analysis_occurrence_id_using_get**](docs/V1OccurrenceApiApi.md#find_analysis_occurrence_by_analysis_occurrence_id_using_get) | **GET** /analysis_occurrences/{analysis_occurrence_id} | Returns the Dynamic Analysis occurrence for the specified identifier.
*V1OccurrenceApiApi* | [**find_analysis_occurrences_by_analysis_id_using_get**](docs/V1OccurrenceApiApi.md#find_analysis_occurrences_by_analysis_id_using_get) | **GET** /analysis_occurrences | Returns a list of occurrences of the Dynamic Analysis. By default, Veracode only returns the occurrences that  started earlier than todays date. Optionally, you can use the status parameter to only return a list of  occurrences of the provided Dynamic Analysis identifier with the specified status(es). 
*V1OccurrenceApiApi* | [**find_scan_occurence_by_occurrence_id_using_get**](docs/V1OccurrenceApiApi.md#find_scan_occurence_by_occurrence_id_using_get) | **GET** /scan_occurrences/{scan_occurrence_id} | Returns the URL scan occurrence for the provided URL scan occurrence identifier.
*V1OccurrenceApiApi* | [**find_scan_occurrences_by_analysis_occurrence_id_using_get**](docs/V1OccurrenceApiApi.md#find_scan_occurrences_by_analysis_occurrence_id_using_get) | **GET** /analysis_occurrences/{analysis_occurrence_id}/scan_occurrences | Returns a list of completed URL scan occurrences for the specified Dynamic Analysis occurrence.
*V1OccurrenceApiApi* | [**find_verification_report_using_get**](docs/V1OccurrenceApiApi.md#find_verification_report_using_get) | **GET** /scan_occurrences/{scan_occurrence_id}/verification_report | Returns the Verification Report, which contains connection and authentication details for the specified scan occurrence ID.
*V1OccurrenceApiApi* | [**get_runtime_scan_configuration_using_get**](docs/V1OccurrenceApiApi.md#get_runtime_scan_configuration_using_get) | **GET** /scan_occurrences/{scan_occurrence_id}/configuration | Returns the configuration for the specified URL scan occurrence.
*V1OccurrenceApiApi* | [**perform_analysis_occurrence_action_using_put**](docs/V1OccurrenceApiApi.md#perform_analysis_occurrence_action_using_put) | **PUT** /analysis_occurrences/{analysis_occurrence_id} | Performs the specified action on the specified occurrence.
*V1OccurrenceApiApi* | [**perform_scan_occurrence_action_using_put**](docs/V1OccurrenceApiApi.md#perform_scan_occurrence_action_using_put) | **PUT** /scan_occurrences/{scan_occurrence_id} | Performs the specified action on the URL scan occurrence.


## Documentation For Models

 - [Analysis](docs/Analysis.md)
 - [AnalysisOccurrence](docs/AnalysisOccurrence.md)
 - [AnalysisOccurrenceStatus](docs/AnalysisOccurrenceStatus.md)
 - [AnalysisRequest](docs/AnalysisRequest.md)
 - [AnalysisSummary](docs/AnalysisSummary.md)
 - [AuditData](docs/AuditData.md)
 - [Authentication](docs/Authentication.md)
 - [AuthenticationConfiguration](docs/AuthenticationConfiguration.md)
 - [AuthenticationConfigurationAuthentications](docs/AuthenticationConfigurationAuthentications.md)
 - [AuthenticationScriptFailureData](docs/AuthenticationScriptFailureData.md)
 - [AuthenticationVerificationData](docs/AuthenticationVerificationData.md)
 - [AutoAuthentication](docs/AutoAuthentication.md)
 - [BasicAuthentication](docs/BasicAuthentication.md)
 - [BlacklistConfiguration](docs/BlacklistConfiguration.md)
 - [ClientCertAuthentication](docs/ClientCertAuthentication.md)
 - [Code](docs/Code.md)
 - [ConnectionAttemptData](docs/ConnectionAttemptData.md)
 - [ConnectionVerificationData](docs/ConnectionVerificationData.md)
 - [ContactInformation](docs/ContactInformation.md)
 - [CrawlConfiguration](docs/CrawlConfiguration.md)
 - [CrawlScript](docs/CrawlScript.md)
 - [DetailedScan](docs/DetailedScan.md)
 - [DetailedScanOccurrence](docs/DetailedScanOccurrence.md)
 - [EmbeddedAnalysisOccurrence](docs/EmbeddedAnalysisOccurrence.md)
 - [EmbeddedAnalysisSummary](docs/EmbeddedAnalysisSummary.md)
 - [EmbeddedAuditData](docs/EmbeddedAuditData.md)
 - [EmbeddedCode](docs/EmbeddedCode.md)
 - [EmbeddedDetailedScan](docs/EmbeddedDetailedScan.md)
 - [EmbeddedDetailedScanOccurrence](docs/EmbeddedDetailedScanOccurrence.md)
 - [EmbeddedErrorData](docs/EmbeddedErrorData.md)
 - [EmbeddedPlatformApplication](docs/EmbeddedPlatformApplication.md)
 - [Errors](docs/Errors.md)
 - [FormAuthentication](docs/FormAuthentication.md)
 - [HttpRequestData](docs/HttpRequestData.md)
 - [HttpResponseData](docs/HttpResponseData.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InternalScanConfiguration](docs/InternalScanConfiguration.md)
 - [Link](docs/Link.md)
 - [LinkedAppInfo](docs/LinkedAppInfo.md)
 - [ListedCode](docs/ListedCode.md)
 - [LoginVerification](docs/LoginVerification.md)
 - [LogoutDetection](docs/LogoutDetection.md)
 - [OrgInformation](docs/OrgInformation.md)
 - [PageMeta](docs/PageMeta.md)
 - [PagedAnalysisOccurrence](docs/PagedAnalysisOccurrence.md)
 - [PagedAnalysisSummary](docs/PagedAnalysisSummary.md)
 - [PagedAuditData](docs/PagedAuditData.md)
 - [PagedDetailedScan](docs/PagedDetailedScan.md)
 - [PagedDetailedScanOccurrence](docs/PagedDetailedScanOccurrence.md)
 - [PagedPlatformApplication](docs/PagedPlatformApplication.md)
 - [PlatformApplication](docs/PlatformApplication.md)
 - [ScanBlackoutSchedule](docs/ScanBlackoutSchedule.md)
 - [ScanCapacitySummary](docs/ScanCapacitySummary.md)
 - [ScanConfiguration](docs/ScanConfiguration.md)
 - [ScanConfigurationRequest](docs/ScanConfigurationRequest.md)
 - [ScanDuration](docs/ScanDuration.md)
 - [ScanOccurrenceRuntimeSummary](docs/ScanOccurrenceRuntimeSummary.md)
 - [ScanOccurrenceStatus](docs/ScanOccurrenceStatus.md)
 - [ScanRecurrenceSchedule](docs/ScanRecurrenceSchedule.md)
 - [ScanRequest](docs/ScanRequest.md)
 - [ScanSchedule](docs/ScanSchedule.md)
 - [ScanSetting](docs/ScanSetting.md)
 - [ScanURL](docs/ScanURL.md)
 - [ScanVerification](docs/ScanVerification.md)
 - [Script](docs/Script.md)
 - [ScriptFailureData](docs/ScriptFailureData.md)
 - [SeleniumCommandFailureData](docs/SeleniumCommandFailureData.md)
 - [SeleniumCommandInfo](docs/SeleniumCommandInfo.md)
 - [ServiceError](docs/ServiceError.md)
 - [Source](docs/Source.md)
 - [TargetListData](docs/TargetListData.md)
 - [UserAgent](docs/UserAgent.md)
 - [UserConfiguration](docs/UserConfiguration.md)
 - [VerificationData](docs/VerificationData.md)
 - [VerificationReport](docs/VerificationReport.md)
 - [VisibilitySetup](docs/VisibilitySetup.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

veracode@veracode.com

