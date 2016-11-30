# Database Access Layer API

## Reference Documentation

### Requests
- [GET /deputy/](#get-deputy)
- [GET /deputy/:deputy_id](#get-deputydeputy_id)
- [GET /faction/](#get-faction)
- [GET /faction/:faction_id](#get-factionfaction_id)
- [GET /bill/](#get-bill)
- [GET /bill/:bill_id](#get-billbill_id)

### Objects
- [```deputy```](#deputy-object)
- [```faction```](#faction-object)
- [```bill```](#bill-object)
- [```vote```](#vote-object)

- - -

## GET /deputy/
Возвращает список депутатов

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure| list of [```deputy```](#deputy-object) objects|

### Parameters
|Name|Required|Description|Default value|Example|
|----|--------|-----------|-------------|-------|
|nameContains|Optional||None|Антон|
|nameStarts|Optional||None|Ивано|
|faction_id|Optional||None||
|bill_id|Optional||None||
|vote|Can be used only with ```bill_id```|Can be one of: ```accept```, ```abstain```, ```decline```, ```none```|accept|decline|

### Example Request
``` GET /deputy/?faction_id=72100004&bill_id=75702&vote=decline```
- - -

## GET /deputy/:deputy_id
Returns [```deputy```](#deputy-object) object with corresponding ```deputy_id```

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure|[```deputy```](#deputy-object) object|

### Parameters
None

### Example Request
``` GET /deputy/99112035 ```
- - -

## GET /faction/
Возвращает список фракций

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure| list of [```faction```](#faction-object) objects|

### Parameters
None

### Example Request
``` GET /faction/ ```
- - -

## GET /faction/:faction_id
Returns [```faction```](#faction-object) object with corresponding ```faction_id```

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure|[```faction```](#faction-object) object|

### Parameters
None

### Example Request
``` GET /faction/72100024 ```
- - -

## GET /bill/
Возвращает список законопроектов

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure| list of [```bill```](#bill-object) objects|

### Parameters
|Name|Required|Description|Default value|Example|
|----|--------|-----------|-------------|-------|
|offset|Optional, mutually exclusive with ```from```, ```to```|chronological order offset of bills block returned|0|280|
|count|Optional|count of bills returned|100|1200|
|from|Optional|datetime less than datetime of any bill returned|None or ```to``` - 24 hours when ```to``` is stated|20151231235959|
|to|Optional|datetime greater than datetime of any bill returned|None or ```from``` + 24 hours when ```from``` is stated|20151231235959|

### Example Request
``` GET /bill/?from=20150211000000&count=20 ```
- - -

## GET /bill/:bill_id
Returns [```bill```](#bill-object) object with corresponding ```bill_id```

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure|[```bill```](#bill-object) object|

### Parameters
None

### Example Request
``` GET /bill/76179 ```
- - -

## ```deputy``` object

### Structure

|Field|Description|
|-----|-----------|
|deputy_id||
|name||
|faction_id||
|faction_title||
- - -

## ```faction``` object

### Structure

|Field|Description|
|-----|-----------|
|faction_id||
|title||
|deputies|list of ```deputy_id```|
- - -

## ```bill``` object

### Structure

|Field|Description|
|-----|-----------|
|bill_id||
|title||
|datetime||
|votes|list of [```vote```](#vote-object) objects|
- - -

## ```vote``` object

### Structure

|Field|Description|
|-----|-----------|
|deputy_id||
|result|One of ```'abstain'```, ```'accept'```, ```'decline'```, ```'none'```|
- - -
