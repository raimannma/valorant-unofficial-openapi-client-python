# ValorantApi

All URIs are relative to *https://api.henrikdev.xyz*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**crosshair**](ValorantApi.md#crosshair) | **GET** /valorant/v1/crosshair/generate | Generate crosshair image (v1) |
| [**esportsEventV2**](ValorantApi.md#esportsEventV2) | **GET** /valorant/v2/esports/vlr/events/{event_id}/matches | Get VLR event matches (v2) |
| [**esportsEventsV2**](ValorantApi.md#esportsEventsV2) | **GET** /valorant/v2/esports/vlr/events | Get VLR esports events (v2) |
| [**esportsMatchV2**](ValorantApi.md#esportsMatchV2) | **GET** /valorant/v2/esports/vlr/matches/{match_id} | Get VLR match details (v2) |
| [**esportsPlayerMatchesV2**](ValorantApi.md#esportsPlayerMatchesV2) | **GET** /valorant/v2/esports/vlr/players/{player}/matches | Get VLR player matches (v2) |
| [**esportsPlayerV2**](ValorantApi.md#esportsPlayerV2) | **GET** /valorant/v2/esports/vlr/players/{player_id} | Get VLR player (v2) |
| [**esportsSchedulesV1**](ValorantApi.md#esportsSchedulesV1) | **GET** /valorant/v1/esports/schedule | Get esports schedule (v1) |
| [**esportsTeamMatchesV2**](ValorantApi.md#esportsTeamMatchesV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/matches | Get VLR team matches (v2) |
| [**esportsTeamTransactionsV2**](ValorantApi.md#esportsTeamTransactionsV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/transactions | Get VLR team transactions (v2) |
| [**esportsTeamV2**](ValorantApi.md#esportsTeamV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id} | Get VLR team (v2) |
| [**getAccountByIdV1**](ValorantApi.md#getAccountByIdV1) | **GET** /valorant/v1/by-puuid/account/{puuid} | Get account by PUUID (v1) |
| [**getAccountByIdV2**](ValorantApi.md#getAccountByIdV2) | **GET** /valorant/v2/by-puuid/account/{puuid} | Get account by PUUID (v2) |
| [**getAccountV1**](ValorantApi.md#getAccountV1) | **GET** /valorant/v1/account/{name}/{tag} | Get account (v1) |
| [**getAccountV2**](ValorantApi.md#getAccountV2) | **GET** /valorant/v2/account/{name}/{tag} | Get account (v2) |
| [**getContentV1**](ValorantApi.md#getContentV1) | **GET** /valorant/v1/content | Get content (v1) |
| [**getMatchesV3ById**](ValorantApi.md#getMatchesV3ById) | **GET** /valorant/v3/by-puuid/matches/{affinity}/{puuid} | Get matches by PUUID (v3) |
| [**getMatchesV3ByName**](ValorantApi.md#getMatchesV3ByName) | **GET** /valorant/v3/matches/{affinity}/{name}/{tag} | Get matches by name (v3) |
| [**getMatchesV4ById**](ValorantApi.md#getMatchesV4ById) | **GET** /valorant/v4/by-puuid/matches/{affinity}/{platform}/{puuid} | Get matches by PUUID (v4) |
| [**getMatchesV4ByName**](ValorantApi.md#getMatchesV4ByName) | **GET** /valorant/v4/matches/{affinity}/{platform}/{name}/{tag} | Get matches by name (v4) |
| [**getMmrHistoryById**](ValorantApi.md#getMmrHistoryById) | **GET** /valorant/v1/by-puuid/mmr-history/{affinity}/{puuid} | Get MMR history by PUUID (v1) |
| [**getMmrHistoryByName**](ValorantApi.md#getMmrHistoryByName) | **GET** /valorant/v1/mmr-history/{affinity}/{name}/{tag} | Get MMR history by name (v1) |
| [**getMmrHistoryV2ById**](ValorantApi.md#getMmrHistoryV2ById) | **GET** /valorant/v2/by-puuid/mmr-history/{affinity}/{platform}/{puuid} | Get MMR history by PUUID (v2) |
| [**getMmrHistoryV2ByName**](ValorantApi.md#getMmrHistoryV2ByName) | **GET** /valorant/v2/mmr-history/{affinity}/{platform}/{name}/{tag} | Get MMR history by name (v2) |
| [**getMmrV1ById**](ValorantApi.md#getMmrV1ById) | **GET** /valorant/v1/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v1) |
| [**getMmrV1ByName**](ValorantApi.md#getMmrV1ByName) | **GET** /valorant/v1/mmr/{affinity}/{name}/{tag} | Get MMR by name (v1) |
| [**getMmrV2ById**](ValorantApi.md#getMmrV2ById) | **GET** /valorant/v2/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v2) |
| [**getMmrV2ByName**](ValorantApi.md#getMmrV2ByName) | **GET** /valorant/v2/mmr/{affinity}/{name}/{tag} | Get MMR by name (v2) |
| [**getMmrV3ById**](ValorantApi.md#getMmrV3ById) | **GET** /valorant/v3/by-puuid/mmr/{affinity}/{platform}/{puuid} | Get MMR by PUUID (v3) |
| [**getMmrV3ByName**](ValorantApi.md#getMmrV3ByName) | **GET** /valorant/v3/mmr/{affinity}/{platform}/{name}/{tag} | Get MMR by name (v3) |
| [**leaderboardV1**](ValorantApi.md#leaderboardV1) | **GET** /valorant/v1/leaderboard/{affinity} | Get leaderboard (v1) |
| [**leaderboardV2**](ValorantApi.md#leaderboardV2) | **GET** /valorant/v2/leaderboard/{affinity} | Get leaderboard (v2) |
| [**leaderboardV3**](ValorantApi.md#leaderboardV3) | **GET** /valorant/v3/leaderboard/{affinity}/{platform} | Get leaderboard (v3) |
| [**matchV2**](ValorantApi.md#matchV2) | **GET** /valorant/v2/match/{match_id} | Get match details (v2) |
| [**matchV4**](ValorantApi.md#matchV4) | **GET** /valorant/v4/match/{affinity}/{match_id} | Get match details (v4) |
| [**premierById**](ValorantApi.md#premierById) | **GET** /valorant/v1/premier/{id} | Get Premier team by ID (v1) |
| [**premierByIdHistory**](ValorantApi.md#premierByIdHistory) | **GET** /valorant/v1/premier/{id}/history | Get Premier team history by ID (v1) |
| [**premierByName**](ValorantApi.md#premierByName) | **GET** /valorant/v1/premier/{name}/{tag} | Get Premier team by name (v1) |
| [**premierByNameHistory**](ValorantApi.md#premierByNameHistory) | **GET** /valorant/v1/premier/{name}/{tag}/history | Get Premier team history by name (v1) |
| [**premierLeaderboard**](ValorantApi.md#premierLeaderboard) | **GET** /valorant/v1/premier/leaderboard/{affinity} | Get Premier leaderboard (v1) |
| [**premierSearch**](ValorantApi.md#premierSearch) | **GET** /valorant/v1/premier/search | Search Premier teams (v1) |
| [**queueStatus**](ValorantApi.md#queueStatus) | **GET** /valorant/v1/queue-status/{affinity} | Get queue status (v1) |
| [**raw**](ValorantApi.md#raw) | **POST** /valorant/v1/raw | Get raw Riot API data (v1) |
| [**status**](ValorantApi.md#status) | **GET** /valorant/v1/status/{affinity} | Get status (v1) |
| [**storeFeatured**](ValorantApi.md#storeFeatured) | **GET** /valorant/{version}/store-featured | Get featured store items |
| [**storeOffers**](ValorantApi.md#storeOffers) | **GET** /valorant/{version}/store-offers | Get store offers |
| [**storedMatches**](ValorantApi.md#storedMatches) | **GET** /valorant/v1/stored-matches/{affinity}/{name}/{tag} | Get stored matches by name (v1) |
| [**storedMatchesById**](ValorantApi.md#storedMatchesById) | **GET** /valorant/v1/by-puuid/stored-matches/{affinity}/{puuid} | Get stored matches by PUUID (v1) |
| [**storedMmrHistory**](ValorantApi.md#storedMmrHistory) | **GET** /valorant/v1/stored-mmr-history/{affinity}/{name}/{tag} | Get stored MMR history by name (v1) |
| [**storedMmrHistoryById**](ValorantApi.md#storedMmrHistoryById) | **GET** /valorant/v1/by-puuid/stored-mmr-history/{affinity}/{puuid} | Get stored MMR history by PUUID (v1) |
| [**storedMmrHistoryV2**](ValorantApi.md#storedMmrHistoryV2) | **GET** /valorant/v2/stored-mmr-history/{affinity}/{platform}/{name}/{tag} | Get stored MMR history by name (v2) |
| [**storedMmrHistoryV2ById**](ValorantApi.md#storedMmrHistoryV2ById) | **GET** /valorant/v2/by-puuid/stored-mmr-history/{affinity}/{platform}/{puuid} | Get stored MMR history by PUUID (v2) |
| [**version**](ValorantApi.md#version) | **GET** /valorant/v1/version/{affinity} | Get game version (v1) |
| [**website**](ValorantApi.md#website) | **GET** /valorant/v1/website/{country_code} | Get website content (v1) |
| [**websiteById**](ValorantApi.md#websiteById) | **GET** /valorant/v1/website/{country_code}/{db_id} | Get website entry by ID (v1) |


<a id="crosshair"></a>
# **crosshair**
> crosshair(id)

Generate crosshair image (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val id : kotlin.String = id_example // kotlin.String | Crosshair code
try {
    apiInstance.crosshair(id)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#crosshair")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#crosshair")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **kotlin.String**| Crosshair code | [optional] |

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

<a id="esportsEventV2"></a>
# **esportsEventV2**
> EsportsV2EventResponse esportsEventV2(eventId)

Get VLR event matches (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val eventId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2EventResponse = apiInstance.esportsEventV2(eventId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsEventV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsEventV2")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **eventId** | **kotlin.Int**|  | |

### Return type

[**EsportsV2EventResponse**](EsportsV2EventResponse.md)

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

<a id="esportsEventsV2"></a>
# **esportsEventsV2**
> EsportsV2EventsResponse esportsEventsV2(region, type, page)

Get VLR esports events (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val region : EsportsV2Region =  // EsportsV2Region | 
val type : EsportsV2EventType =  // EsportsV2EventType | 
val page : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2EventsResponse = apiInstance.esportsEventsV2(region, type, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsEventsV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsEventsV2")
    e.printStackTrace()
}
```

### Parameters
| **region** | [**EsportsV2Region**](.md)|  | [optional] [enum: north_america, europe, brazil, asia_pacific, korea, japan, latin_america, oceania, mena, gc, collegiate] |
| **type** | [**EsportsV2EventType**](.md)|  | [optional] [enum: completed, upcoming] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **kotlin.Int**|  | [optional] |

### Return type

[**EsportsV2EventsResponse**](EsportsV2EventsResponse.md)

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

<a id="esportsMatchV2"></a>
# **esportsMatchV2**
> EsportsV2MatchesResponse esportsMatchV2(matchId)

Get VLR match details (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val matchId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2MatchesResponse = apiInstance.esportsMatchV2(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsMatchV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsMatchV2")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Int**|  | |

### Return type

[**EsportsV2MatchesResponse**](EsportsV2MatchesResponse.md)

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

<a id="esportsPlayerMatchesV2"></a>
# **esportsPlayerMatchesV2**
> EsportsV2PlayerMatchesResponse esportsPlayerMatchesV2(player, page)

Get VLR player matches (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val player : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2PlayerMatchesResponse = apiInstance.esportsPlayerMatchesV2(player, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsPlayerMatchesV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsPlayerMatchesV2")
    e.printStackTrace()
}
```

### Parameters
| **player** | **kotlin.Int**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **kotlin.Int**|  | [optional] |

### Return type

[**EsportsV2PlayerMatchesResponse**](EsportsV2PlayerMatchesResponse.md)

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

<a id="esportsPlayerV2"></a>
# **esportsPlayerV2**
> EsportsV2PlayerResponse esportsPlayerV2(player, timespan)

Get VLR player (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val player : kotlin.Int = 56 // kotlin.Int | 
val timespan : EsportsV2PlayerTimespan =  // EsportsV2PlayerTimespan | 
try {
    val result : EsportsV2PlayerResponse = apiInstance.esportsPlayerV2(player, timespan)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsPlayerV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsPlayerV2")
    e.printStackTrace()
}
```

### Parameters
| **player** | **kotlin.Int**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **timespan** | [**EsportsV2PlayerTimespan**](.md)|  | [optional] [enum: 30d, 60d, 90d, all] |

### Return type

[**EsportsV2PlayerResponse**](EsportsV2PlayerResponse.md)

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

<a id="esportsSchedulesV1"></a>
# **esportsSchedulesV1**
> EsportsV1Response esportsSchedulesV1(region, league)

Get esports schedule (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val region : kotlin.String = region_example // kotlin.String | 
val league : kotlin.String = league_example // kotlin.String | 
try {
    val result : EsportsV1Response = apiInstance.esportsSchedulesV1(region, league)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsSchedulesV1")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsSchedulesV1")
    e.printStackTrace()
}
```

### Parameters
| **region** | **kotlin.String**|  | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **league** | **kotlin.String**|  | [optional] |

### Return type

[**EsportsV1Response**](EsportsV1Response.md)

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

<a id="esportsTeamMatchesV2"></a>
# **esportsTeamMatchesV2**
> EsportsV2TeamMatchListResponse esportsTeamMatchesV2(teamId, page)

Get VLR team matches (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val teamId : kotlin.Int = 56 // kotlin.Int | 
val page : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2TeamMatchListResponse = apiInstance.esportsTeamMatchesV2(teamId, page)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsTeamMatchesV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsTeamMatchesV2")
    e.printStackTrace()
}
```

### Parameters
| **teamId** | **kotlin.Int**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **kotlin.Int**|  | [optional] |

### Return type

[**EsportsV2TeamMatchListResponse**](EsportsV2TeamMatchListResponse.md)

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

<a id="esportsTeamTransactionsV2"></a>
# **esportsTeamTransactionsV2**
> EsportsV2TeamTransactionsResponse esportsTeamTransactionsV2(teamId)

Get VLR team transactions (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val teamId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2TeamTransactionsResponse = apiInstance.esportsTeamTransactionsV2(teamId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsTeamTransactionsV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsTeamTransactionsV2")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **teamId** | **kotlin.Int**|  | |

### Return type

[**EsportsV2TeamTransactionsResponse**](EsportsV2TeamTransactionsResponse.md)

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

<a id="esportsTeamV2"></a>
# **esportsTeamV2**
> EsportsV2TeamResponse esportsTeamV2(teamId)

Get VLR team (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val teamId : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : EsportsV2TeamResponse = apiInstance.esportsTeamV2(teamId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#esportsTeamV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#esportsTeamV2")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **teamId** | **kotlin.Int**|  | |

### Return type

[**EsportsV2TeamResponse**](EsportsV2TeamResponse.md)

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

<a id="getAccountByIdV1"></a>
# **getAccountByIdV1**
> AccountV1Response getAccountByIdV1(puuid, force)

Get account by PUUID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val force : kotlin.Boolean = true // kotlin.Boolean | Bypass cache and refresh (optional)
try {
    val result : AccountV1Response = apiInstance.getAccountByIdV1(puuid, force)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getAccountByIdV1")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getAccountByIdV1")
    e.printStackTrace()
}
```

### Parameters
| **puuid** | **kotlin.String**| Player UUID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **force** | **kotlin.Boolean**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**AccountV1Response**](AccountV1Response.md)

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

<a id="getAccountByIdV2"></a>
# **getAccountByIdV2**
> AccountV2Response getAccountByIdV2(puuid, force)

Get account by PUUID (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val force : kotlin.Boolean = true // kotlin.Boolean | Bypass cache and refresh (optional)
try {
    val result : AccountV2Response = apiInstance.getAccountByIdV2(puuid, force)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getAccountByIdV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getAccountByIdV2")
    e.printStackTrace()
}
```

### Parameters
| **puuid** | **kotlin.String**| Player UUID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **force** | **kotlin.Boolean**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**AccountV2Response**](AccountV2Response.md)

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

<a id="getAccountV1"></a>
# **getAccountV1**
> AccountV1Response getAccountV1(name, tag, force)

Get account (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val force : kotlin.Boolean = true // kotlin.Boolean | Bypass cache and refresh (optional)
try {
    val result : AccountV1Response = apiInstance.getAccountV1(name, tag, force)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getAccountV1")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getAccountV1")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **force** | **kotlin.Boolean**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**AccountV1Response**](AccountV1Response.md)

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

<a id="getAccountV2"></a>
# **getAccountV2**
> AccountV2Response getAccountV2(name, tag, force)

Get account (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val force : kotlin.Boolean = true // kotlin.Boolean | Bypass cache and refresh (optional)
try {
    val result : AccountV2Response = apiInstance.getAccountV2(name, tag, force)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getAccountV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getAccountV2")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **force** | **kotlin.Boolean**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**AccountV2Response**](AccountV2Response.md)

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

<a id="getContentV1"></a>
# **getContentV1**
> ContentV1Response getContentV1(locale)

Get content (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val locale : kotlin.String = locale_example // kotlin.String | Locale code (e.g., en-US, de-DE) - optional
try {
    val result : ContentV1Response = apiInstance.getContentV1(locale)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getContentV1")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getContentV1")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **kotlin.String**| Locale code (e.g., en-US, de-DE) - optional | [optional] |

### Return type

[**ContentV1Response**](ContentV1Response.md)

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

<a id="getMatchesV3ById"></a>
# **getMatchesV3ById**
> MatchesV3ListResponse getMatchesV3ById(affinity, puuid, mode, map, size)

Get matches by PUUID (v3)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val mode : kotlin.String = mode_example // kotlin.String | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : MatchesV3ListResponse = apiInstance.getMatchesV3ById(affinity, puuid, mode, map, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMatchesV3ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMatchesV3ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **kotlin.String**| Player UUID | |
| **mode** | **kotlin.String**| Game mode filter (optional) | [optional] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**MatchesV3ListResponse**](MatchesV3ListResponse.md)

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

<a id="getMatchesV3ByName"></a>
# **getMatchesV3ByName**
> MatchesV3ListResponse getMatchesV3ByName(affinity, name, tag, mode, map, size)

Get matches by name (v3)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val mode : MatchMode =  // MatchMode | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : MatchesV3ListResponse = apiInstance.getMatchesV3ByName(affinity, name, tag, mode, map, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMatchesV3ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMatchesV3ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| **mode** | [**MatchMode**](.md)| Game mode filter (optional) | [optional] [enum: Competitive, Unrated, Custom, Practice, Unknown] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**MatchesV3ListResponse**](MatchesV3ListResponse.md)

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

<a id="getMatchesV4ById"></a>
# **getMatchesV4ById**
> MatchesV4HistoryResponse getMatchesV4ById(affinity, platform, puuid, mode, map, size, start)

Get matches by PUUID (v4)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val mode : kotlin.String = mode_example // kotlin.String | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
val start : kotlin.Int = 56 // kotlin.Int | Start index for pagination (optional)
try {
    val result : MatchesV4HistoryResponse = apiInstance.getMatchesV4ById(affinity, platform, puuid, mode, map, size, start)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMatchesV4ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMatchesV4ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **puuid** | **kotlin.String**| Player UUID | |
| **mode** | **kotlin.String**| Game mode filter (optional) | [optional] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **start** | **kotlin.Int**| Start index for pagination (optional) | [optional] |

### Return type

[**MatchesV4HistoryResponse**](MatchesV4HistoryResponse.md)

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

<a id="getMatchesV4ByName"></a>
# **getMatchesV4ByName**
> MatchesV4HistoryResponse getMatchesV4ByName(affinity, platform, name, tag, mode, map, size, start)

Get matches by name (v4)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val mode : kotlin.String = mode_example // kotlin.String | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
val start : kotlin.Int = 56 // kotlin.Int | Start index for pagination (optional)
try {
    val result : MatchesV4HistoryResponse = apiInstance.getMatchesV4ByName(affinity, platform, name, tag, mode, map, size, start)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMatchesV4ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMatchesV4ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| **mode** | **kotlin.String**| Game mode filter (optional) | [optional] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **start** | **kotlin.Int**| Start index for pagination (optional) | [optional] |

### Return type

[**MatchesV4HistoryResponse**](MatchesV4HistoryResponse.md)

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

<a id="getMmrHistoryById"></a>
# **getMmrHistoryById**
> MMRHistoryV1Response getMmrHistoryById(affinity, puuid)

Get MMR history by PUUID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
try {
    val result : MMRHistoryV1Response = apiInstance.getMmrHistoryById(affinity, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrHistoryById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrHistoryById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID | |

### Return type

[**MMRHistoryV1Response**](MMRHistoryV1Response.md)

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

<a id="getMmrHistoryByName"></a>
# **getMmrHistoryByName**
> MMRHistoryV1Response getMmrHistoryByName(affinity, name, tag)

Get MMR history by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
try {
    val result : MMRHistoryV1Response = apiInstance.getMmrHistoryByName(affinity, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrHistoryByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrHistoryByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Riot ID tag | |

### Return type

[**MMRHistoryV1Response**](MMRHistoryV1Response.md)

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

<a id="getMmrHistoryV2ById"></a>
# **getMmrHistoryV2ById**
> MMRHistoryV2Response getMmrHistoryV2ById(affinity, platform, puuid)

Get MMR history by PUUID (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
try {
    val result : MMRHistoryV2Response = apiInstance.getMmrHistoryV2ById(affinity, platform, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrHistoryV2ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrHistoryV2ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID | |

### Return type

[**MMRHistoryV2Response**](MMRHistoryV2Response.md)

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

<a id="getMmrHistoryV2ByName"></a>
# **getMmrHistoryV2ByName**
> MMRHistoryV2Response getMmrHistoryV2ByName(affinity, platform, name, tag)

Get MMR history by name (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
try {
    val result : MMRHistoryV2Response = apiInstance.getMmrHistoryV2ByName(affinity, platform, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrHistoryV2ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrHistoryV2ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **name** | **kotlin.String**| Riot ID name | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Riot ID tag | |

### Return type

[**MMRHistoryV2Response**](MMRHistoryV2Response.md)

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

<a id="getMmrV1ById"></a>
# **getMmrV1ById**
> MMRV1Response getMmrV1ById(affinity, puuid)

Get MMR by PUUID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
try {
    val result : MMRV1Response = apiInstance.getMmrV1ById(affinity, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV1ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV1ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID | |

### Return type

[**MMRV1Response**](MMRV1Response.md)

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

<a id="getMmrV1ByName"></a>
# **getMmrV1ByName**
> MMRV1Response getMmrV1ByName(affinity, name, tag)

Get MMR by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
try {
    val result : MMRV1Response = apiInstance.getMmrV1ByName(affinity, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV1ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV1ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Riot ID tag | |

### Return type

[**MMRV1Response**](MMRV1Response.md)

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

<a id="getMmrV2ById"></a>
# **getMmrV2ById**
> MMRV2Response getMmrV2ById(affinity, puuid)

Get MMR by PUUID (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
try {
    val result : MMRV2Response = apiInstance.getMmrV2ById(affinity, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV2ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV2ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID | |

### Return type

[**MMRV2Response**](MMRV2Response.md)

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

<a id="getMmrV2ByName"></a>
# **getMmrV2ByName**
> MMRV2Response getMmrV2ByName(affinity, name, tag)

Get MMR by name (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
try {
    val result : MMRV2Response = apiInstance.getMmrV2ByName(affinity, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV2ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV2ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Riot ID tag | |

### Return type

[**MMRV2Response**](MMRV2Response.md)

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

<a id="getMmrV3ById"></a>
# **getMmrV3ById**
> MMRV3Response getMmrV3ById(affinity, platform, puuid)

Get MMR by PUUID (v3)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
try {
    val result : MMRV3Response = apiInstance.getMmrV3ById(affinity, platform, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV3ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV3ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID | |

### Return type

[**MMRV3Response**](MMRV3Response.md)

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

<a id="getMmrV3ByName"></a>
# **getMmrV3ByName**
> MMRV3Response getMmrV3ByName(affinity, platform, name, tag)

Get MMR by name (v3)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
try {
    val result : MMRV3Response = apiInstance.getMmrV3ByName(affinity, platform, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#getMmrV3ByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#getMmrV3ByName")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **name** | **kotlin.String**| Riot ID name | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Riot ID tag | |

### Return type

[**MMRV3Response**](MMRV3Response.md)

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

<a id="leaderboardV1"></a>
# **leaderboardV1**
> kotlin.Any leaderboardV1(affinity, season, name, tag)

Get leaderboard (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val season : kotlin.String = season_example // kotlin.String | Season ID (optional)
val name : kotlin.String = name_example // kotlin.String | Player name to search for (optional)
val tag : kotlin.String = tag_example // kotlin.String | Player tag to search for (optional)
try {
    val result : kotlin.Any = apiInstance.leaderboardV1(affinity, season, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#leaderboardV1")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#leaderboardV1")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **season** | **kotlin.String**| Season ID (optional) | [optional] |
| **name** | **kotlin.String**| Player name to search for (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Player tag to search for (optional) | [optional] |

### Return type

[**kotlin.Any**](kotlin.Any.md)

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

<a id="leaderboardV2"></a>
# **leaderboardV2**
> LeaderboardV2Response leaderboardV2(affinity, season, name, tag, puuid)

Get leaderboard (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val season : kotlin.String = season_example // kotlin.String | Season ID (optional)
val name : kotlin.String = name_example // kotlin.String | Player name to search for (optional)
val tag : kotlin.String = tag_example // kotlin.String | Player tag to search for (optional)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID to search for (optional)
try {
    val result : LeaderboardV2Response = apiInstance.leaderboardV2(affinity, season, name, tag, puuid)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#leaderboardV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#leaderboardV2")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **season** | **kotlin.String**| Season ID (optional) | [optional] |
| **name** | **kotlin.String**| Player name to search for (optional) | [optional] |
| **tag** | **kotlin.String**| Player tag to search for (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **kotlin.String**| Player UUID to search for (optional) | [optional] |

### Return type

[**LeaderboardV2Response**](LeaderboardV2Response.md)

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

<a id="leaderboardV3"></a>
# **leaderboardV3**
> LeaderboardV3Response leaderboardV3(affinity, platform, season, size, page, name, tag)

Get leaderboard (v3)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val season : kotlin.String = season_example // kotlin.String | Season ID (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results per page (optional)
val page : kotlin.Int = 56 // kotlin.Int | Page number (optional)
val name : kotlin.String = name_example // kotlin.String | Player name to search for (optional)
val tag : kotlin.String = tag_example // kotlin.String | Player tag to search for (optional)
try {
    val result : LeaderboardV3Response = apiInstance.leaderboardV3(affinity, platform, season, size, page, name, tag)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#leaderboardV3")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#leaderboardV3")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **season** | **kotlin.String**| Season ID (optional) | [optional] |
| **size** | **kotlin.Int**| Number of results per page (optional) | [optional] |
| **page** | **kotlin.Int**| Page number (optional) | [optional] |
| **name** | **kotlin.String**| Player name to search for (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **tag** | **kotlin.String**| Player tag to search for (optional) | [optional] |

### Return type

[**LeaderboardV3Response**](LeaderboardV3Response.md)

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

<a id="matchV2"></a>
# **matchV2**
> MatchesV2Response matchV2(matchId)

Get match details (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val matchId : kotlin.String = matchId_example // kotlin.String | Match UUID
try {
    val result : MatchesV2Response = apiInstance.matchV2(matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#matchV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#matchV2")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.String**| Match UUID | |

### Return type

[**MatchesV2Response**](MatchesV2Response.md)

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

<a id="matchV4"></a>
# **matchV4**
> MatchesV4Response matchV4(affinity, matchId)

Get match details (v4)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val matchId : kotlin.String = matchId_example // kotlin.String | Match UUID
try {
    val result : MatchesV4Response = apiInstance.matchV4(affinity, matchId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#matchV4")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#matchV4")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.String**| Match UUID | |

### Return type

[**MatchesV4Response**](MatchesV4Response.md)

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

<a id="premierById"></a>
# **premierById**
> PremierTeamV1Response premierById(id, season, affinity)

Get Premier team by ID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val id : kotlin.String = id_example // kotlin.String | Team UUID
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity for fallback resolution (optional)
try {
    val result : PremierTeamV1Response = apiInstance.premierById(id, season, affinity)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierById")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.String**| Team UUID | |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **kotlin.String**| Region/affinity for fallback resolution (optional) | [optional] |

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

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

<a id="premierByIdHistory"></a>
# **premierByIdHistory**
> PremierTeamV1Response premierByIdHistory(id, season)

Get Premier team history by ID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val id : kotlin.String = id_example // kotlin.String | Team UUID
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
try {
    val result : PremierTeamV1Response = apiInstance.premierByIdHistory(id, season)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierByIdHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierByIdHistory")
    e.printStackTrace()
}
```

### Parameters
| **id** | **kotlin.String**| Team UUID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

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

<a id="premierByName"></a>
# **premierByName**
> PremierTeamV1Response premierByName(name, tag, season, affinity)

Get Premier team by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val name : kotlin.String = name_example // kotlin.String | Team name
val tag : kotlin.String = tag_example // kotlin.String | Team tag
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity for fallback resolution (optional)
try {
    val result : PremierTeamV1Response = apiInstance.premierByName(name, tag, season, affinity)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierByName")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Team name | |
| **tag** | **kotlin.String**| Team tag | |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **kotlin.String**| Region/affinity for fallback resolution (optional) | [optional] |

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

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

<a id="premierByNameHistory"></a>
# **premierByNameHistory**
> PremierTeamHistoryV1Response premierByNameHistory(name, tag, season)

Get Premier team history by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val name : kotlin.String = name_example // kotlin.String | Team name
val tag : kotlin.String = tag_example // kotlin.String | Team tag
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
try {
    val result : PremierTeamHistoryV1Response = apiInstance.premierByNameHistory(name, tag, season)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierByNameHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierByNameHistory")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Team name | |
| **tag** | **kotlin.String**| Team tag | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |

### Return type

[**PremierTeamHistoryV1Response**](PremierTeamHistoryV1Response.md)

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

<a id="premierLeaderboard"></a>
# **premierLeaderboard**
> PremierSearchResponse premierLeaderboard(affinity, conference, division, season)

Get Premier leaderboard (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val conference : kotlin.String = conference_example // kotlin.String | Conference filter (optional)
val division : kotlin.String = division_example // kotlin.String | Division filter (optional)
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
try {
    val result : PremierSearchResponse = apiInstance.premierLeaderboard(affinity, conference, division, season)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierLeaderboard")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierLeaderboard")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **conference** | **kotlin.String**| Conference filter (optional) | [optional] |
| **division** | **kotlin.String**| Division filter (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |

### Return type

[**PremierSearchResponse**](PremierSearchResponse.md)

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

<a id="premierSearch"></a>
# **premierSearch**
> PremierSearchResponse premierSearch(name, tag, id, season)

Search Premier teams (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val name : kotlin.String = name_example // kotlin.String | Team name to search for (optional)
val tag : kotlin.String = tag_example // kotlin.String | Team tag to search for (optional)
val id : kotlin.String = id_example // kotlin.String | Team UUID to search for (optional)
val season : kotlin.String = season_example // kotlin.String | Premier season id (optional)
try {
    val result : PremierSearchResponse = apiInstance.premierSearch(name, tag, id, season)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#premierSearch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#premierSearch")
    e.printStackTrace()
}
```

### Parameters
| **name** | **kotlin.String**| Team name to search for (optional) | [optional] |
| **tag** | **kotlin.String**| Team tag to search for (optional) | [optional] |
| **id** | **kotlin.String**| Team UUID to search for (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **season** | **kotlin.String**| Premier season id (optional) | [optional] |

### Return type

[**PremierSearchResponse**](PremierSearchResponse.md)

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

<a id="queueStatus"></a>
# **queueStatus**
> QueueStatusV1 queueStatus(affinity)

Get queue status (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
try {
    val result : QueueStatusV1 = apiInstance.queueStatus(affinity)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#queueStatus")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#queueStatus")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**QueueStatusV1**](QueueStatusV1.md)

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

<a id="raw"></a>
# **raw**
> RawV1Response raw(rawV1Payload)

Get raw Riot API data (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val rawV1Payload : RawV1Payload =  // RawV1Payload | 
try {
    val result : RawV1Response = apiInstance.raw(rawV1Payload)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#raw")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#raw")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rawV1Payload** | [**RawV1Payload**](RawV1Payload.md)|  | |

### Return type

[**RawV1Response**](RawV1Response.md)

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

<a id="status"></a>
# **status**
> StatusV1 status(affinity)

Get status (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
try {
    val result : StatusV1 = apiInstance.status(affinity)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#status")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#status")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**StatusV1**](StatusV1.md)

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

<a id="storeFeatured"></a>
# **storeFeatured**
> StoreFeaturedV1 storeFeatured(version)

Get featured store items

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val version : kotlin.String = version_example // kotlin.String | API version (v1, v2)
try {
    val result : StoreFeaturedV1 = apiInstance.storeFeatured(version)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storeFeatured")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storeFeatured")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **version** | **kotlin.String**| API version (v1, v2) | |

### Return type

[**StoreFeaturedV1**](StoreFeaturedV1.md)

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

<a id="storeOffers"></a>
# **storeOffers**
> StoreOffersV1Response storeOffers(version)

Get store offers

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val version : kotlin.String = version_example // kotlin.String | API version (v1, v2)
try {
    val result : StoreOffersV1Response = apiInstance.storeOffers(version)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storeOffers")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storeOffers")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **version** | **kotlin.String**| API version (v1, v2) | |

### Return type

[**StoreOffersV1Response**](StoreOffersV1Response.md)

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

<a id="storedMatches"></a>
# **storedMatches**
> StoredMatchesResponse storedMatches(affinity, name, tag, mode, map, size)

Get stored matches by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val mode : kotlin.String = mode_example // kotlin.String | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMatchesResponse = apiInstance.storedMatches(affinity, name, tag, mode, map, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMatches")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMatches")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| **mode** | **kotlin.String**| Game mode filter (optional) | [optional] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMatchesResponse**](StoredMatchesResponse.md)

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

<a id="storedMatchesById"></a>
# **storedMatchesById**
> StoredMatchesResponse storedMatchesById(affinity, puuid, mode, map, size)

Get stored matches by PUUID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val mode : kotlin.String = mode_example // kotlin.String | Game mode filter (optional)
val map : kotlin.String = map_example // kotlin.String | Map filter (optional)
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMatchesResponse = apiInstance.storedMatchesById(affinity, puuid, mode, map, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMatchesById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMatchesById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **kotlin.String**| Player UUID | |
| **mode** | **kotlin.String**| Game mode filter (optional) | [optional] |
| **map** | **kotlin.String**| Map filter (optional) | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMatchesResponse**](StoredMatchesResponse.md)

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

<a id="storedMmrHistory"></a>
# **storedMmrHistory**
> StoredMMRResponse storedMmrHistory(affinity, name, tag, size)

Get stored MMR history by name (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMMRResponse = apiInstance.storedMmrHistory(affinity, name, tag, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMmrHistory")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMmrHistory")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMMRResponse**](StoredMMRResponse.md)

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

<a id="storedMmrHistoryById"></a>
# **storedMmrHistoryById**
> StoredMMRResponse storedMmrHistoryById(affinity, puuid, size)

Get stored MMR history by PUUID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMMRResponse = apiInstance.storedMmrHistoryById(affinity, puuid, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMmrHistoryById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMmrHistoryById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **kotlin.String**| Player UUID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMMRResponse**](StoredMMRResponse.md)

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

<a id="storedMmrHistoryV2"></a>
# **storedMmrHistoryV2**
> StoredMMRV2Response storedMmrHistoryV2(affinity, platform, name, tag, size)

Get stored MMR history by name (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val name : kotlin.String = name_example // kotlin.String | Riot ID name
val tag : kotlin.String = tag_example // kotlin.String | Riot ID tag
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMMRV2Response = apiInstance.storedMmrHistoryV2(affinity, platform, name, tag, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMmrHistoryV2")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMmrHistoryV2")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **name** | **kotlin.String**| Riot ID name | |
| **tag** | **kotlin.String**| Riot ID tag | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMMRV2Response**](StoredMMRV2Response.md)

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

<a id="storedMmrHistoryV2ById"></a>
# **storedMmrHistoryV2ById**
> StoredMMRV2Response storedMmrHistoryV2ById(affinity, platform, puuid, size)

Get stored MMR history by PUUID (v2)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
val platform : kotlin.String = platform_example // kotlin.String | Platform (pc, console)
val puuid : kotlin.String = puuid_example // kotlin.String | Player UUID
val size : kotlin.Int = 56 // kotlin.Int | Number of results (optional)
try {
    val result : StoredMMRV2Response = apiInstance.storedMmrHistoryV2ById(affinity, platform, puuid, size)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#storedMmrHistoryV2ById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#storedMmrHistoryV2ById")
    e.printStackTrace()
}
```

### Parameters
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **kotlin.String**| Platform (pc, console) | |
| **puuid** | **kotlin.String**| Player UUID | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **size** | **kotlin.Int**| Number of results (optional) | [optional] |

### Return type

[**StoredMMRV2Response**](StoredMMRV2Response.md)

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

<a id="version"></a>
# **version**
> VersionV1Response version(affinity)

Get game version (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val affinity : kotlin.String = affinity_example // kotlin.String | Region/affinity (e.g., na, eu, ap, kr)
try {
    val result : VersionV1Response = apiInstance.version(affinity)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#version")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#version")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **kotlin.String**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**VersionV1Response**](VersionV1Response.md)

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

<a id="website"></a>
# **website**
> WebsiteV1Response website(countryCode, category)

Get website content (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val countryCode : kotlin.String = countryCode_example // kotlin.String | Country code (e.g., en-us, de-de)
val category : kotlin.String = category_example // kotlin.String | Category filter (optional)
try {
    val result : WebsiteV1Response = apiInstance.website(countryCode, category)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#website")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#website")
    e.printStackTrace()
}
```

### Parameters
| **countryCode** | **kotlin.String**| Country code (e.g., en-us, de-de) | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category** | **kotlin.String**| Category filter (optional) | [optional] |

### Return type

[**WebsiteV1Response**](WebsiteV1Response.md)

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

<a id="websiteById"></a>
# **websiteById**
> WebsiteByIdV1Response websiteById(dbId, countryCode)

Get website entry by ID (v1)

### Example
```kotlin
// Import classes:
//import henrikdevApiClient.infrastructure.*
//import henrikdevApiClient.models.*

val apiInstance = ValorantApi()
val dbId : kotlin.String = dbId_example // kotlin.String | Database ID of the website entry
val countryCode : kotlin.String = countryCode_example // kotlin.String | Country code (e.g., en-us, de-de)
try {
    val result : WebsiteByIdV1Response = apiInstance.websiteById(dbId, countryCode)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ValorantApi#websiteById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ValorantApi#websiteById")
    e.printStackTrace()
}
```

### Parameters
| **dbId** | **kotlin.String**| Database ID of the website entry | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **countryCode** | **kotlin.String**| Country code (e.g., en-us, de-de) | |

### Return type

[**WebsiteByIdV1Response**](WebsiteByIdV1Response.md)

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

