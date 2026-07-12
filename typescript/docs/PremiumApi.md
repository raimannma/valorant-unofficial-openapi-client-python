# PremiumApi

All URIs are relative to *https://api.henrikdev.xyz*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**addWebhookUser**](#addwebhookuser) | **POST** /public/v1/premium/webhook/users | Add premium webhook user|
|[**deleteWebhookUser**](#deletewebhookuser) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user|
|[**getWebhookSettings**](#getwebhooksettings) | **GET** /public/v1/premium/webhook | Get premium webhook settings|
|[**updateWebhookUser**](#updatewebhookuser) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user|

# **addWebhookUser**
> PremiumWebhookUserMutationResponse addWebhookUser(premiumWebhookUserAddRequest)


### Example

```typescript
import {
    PremiumApi,
    Configuration,
    PremiumWebhookUserAddRequest
} from 'henrikdev_api_client';

const configuration = new Configuration();
const apiInstance = new PremiumApi(configuration);

let premiumWebhookUserAddRequest: PremiumWebhookUserAddRequest; //

const { status, data } = await apiInstance.addWebhookUser(
    premiumWebhookUserAddRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **premiumWebhookUserAddRequest** | **PremiumWebhookUserAddRequest**|  | |


### Return type

**PremiumWebhookUserMutationResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Tracked user added successfully |  -  |
|**400** | Bad Request |  -  |
|**401** | Unauthorized |  -  |
|**403** | Premium plan required |  -  |
|**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteWebhookUser**
> PremiumWebhookDeleteResponse deleteWebhookUser()


### Example

```typescript
import {
    PremiumApi,
    Configuration
} from 'henrikdev_api_client';

const configuration = new Configuration();
const apiInstance = new PremiumApi(configuration);

let id: string; //Tracked user id (default to undefined)

const { status, data } = await apiInstance.deleteWebhookUser(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Tracked user id | defaults to undefined|


### Return type

**PremiumWebhookDeleteResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Tracked user removed successfully |  -  |
|**400** | Bad Request |  -  |
|**401** | Unauthorized |  -  |
|**404** | Tracked user not found |  -  |
|**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getWebhookSettings**
> getWebhookSettings()


### Example

```typescript
import {
    PremiumApi,
    Configuration
} from 'henrikdev_api_client';

const configuration = new Configuration();
const apiInstance = new PremiumApi(configuration);

const { status, data } = await apiInstance.getWebhookSettings();
```

### Parameters
This endpoint does not have any parameters.


### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Premium webhook settings and tracked users retrieved successfully |  -  |
|**401** | Unauthorized |  -  |
|**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateWebhookUser**
> updateWebhookUser(premiumWebhookUserUpdateRequest)


### Example

```typescript
import {
    PremiumApi,
    Configuration,
    PremiumWebhookUserUpdateRequest
} from 'henrikdev_api_client';

const configuration = new Configuration();
const apiInstance = new PremiumApi(configuration);

let id: string; //Tracked user id (default to undefined)
let premiumWebhookUserUpdateRequest: PremiumWebhookUserUpdateRequest; //

const { status, data } = await apiInstance.updateWebhookUser(
    id,
    premiumWebhookUserUpdateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **premiumWebhookUserUpdateRequest** | **PremiumWebhookUserUpdateRequest**|  | |
| **id** | [**string**] | Tracked user id | defaults to undefined|


### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Tracked user updated successfully |  -  |
|**400** | Bad Request |  -  |
|**401** | Unauthorized |  -  |
|**404** | Tracked user not found |  -  |
|**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

