# PremiumApi

All URIs are relative to *https://api.henrikdev.xyz*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addWebhookUser**](PremiumApi.md#addWebhookUser) | **POST** /public/v1/premium/webhook/users | Add premium webhook user |
| [**deleteWebhookUser**](PremiumApi.md#deleteWebhookUser) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user |
| [**getWebhookSettings**](PremiumApi.md#getWebhookSettings) | **GET** /public/v1/premium/webhook | Get premium webhook settings |
| [**updateWebhookUser**](PremiumApi.md#updateWebhookUser) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user |


<a id="addWebhookUser"></a>
# **addWebhookUser**
> PremiumWebhookUserMutationResponse addWebhookUser(premiumWebhookUserAddRequest)

Add premium webhook user

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = PremiumApi()
val premiumWebhookUserAddRequest : PremiumWebhookUserAddRequest =  // PremiumWebhookUserAddRequest | 
try {
    val result : PremiumWebhookUserMutationResponse = apiInstance.addWebhookUser(premiumWebhookUserAddRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PremiumApi#addWebhookUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PremiumApi#addWebhookUser")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **premiumWebhookUserAddRequest** | [**PremiumWebhookUserAddRequest**](PremiumWebhookUserAddRequest.md)|  | |

### Return type

[**PremiumWebhookUserMutationResponse**](PremiumWebhookUserMutationResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["Authorization"] = ""
    ApiClient.apiKeyPrefix["Authorization"] = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="deleteWebhookUser"></a>
# **deleteWebhookUser**
> PremiumWebhookDeleteResponse deleteWebhookUser(id)

Delete premium webhook user

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = PremiumApi()
val id : kotlin.String = id_example // kotlin.String | Tracked user id
try {
    val result : PremiumWebhookDeleteResponse = apiInstance.deleteWebhookUser(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling PremiumApi#deleteWebhookUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PremiumApi#deleteWebhookUser")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **kotlin.String**| Tracked user id | |

### Return type

[**PremiumWebhookDeleteResponse**](PremiumWebhookDeleteResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["Authorization"] = ""
    ApiClient.apiKeyPrefix["Authorization"] = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="getWebhookSettings"></a>
# **getWebhookSettings**
> getWebhookSettings()

Get premium webhook settings

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = PremiumApi()
try {
    apiInstance.getWebhookSettings()
} catch (e: ClientException) {
    println("4xx response calling PremiumApi#getWebhookSettings")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PremiumApi#getWebhookSettings")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["Authorization"] = ""
    ApiClient.apiKeyPrefix["Authorization"] = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="updateWebhookUser"></a>
# **updateWebhookUser**
> updateWebhookUser(id, premiumWebhookUserUpdateRequest)

Update premium webhook user

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = PremiumApi()
val id : kotlin.String = id_example // kotlin.String | Tracked user id
val premiumWebhookUserUpdateRequest : PremiumWebhookUserUpdateRequest =  // PremiumWebhookUserUpdateRequest | 
try {
    apiInstance.updateWebhookUser(id, premiumWebhookUserUpdateRequest)
} catch (e: ClientException) {
    println("4xx response calling PremiumApi#updateWebhookUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PremiumApi#updateWebhookUser")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **kotlin.String**| Tracked user id | |
| **premiumWebhookUserUpdateRequest** | [**PremiumWebhookUserUpdateRequest**](PremiumWebhookUserUpdateRequest.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["Authorization"] = ""
    ApiClient.apiKeyPrefix["Authorization"] = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

