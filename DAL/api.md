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
``` GET /deputy/?bill_id=83718&faction_id=72100005&nameContains=Игорь ```

### Example Response
```json
[
  {
    "deputy_id": 99111780,
    "faction_id": 72100005,
    "faction_title": "ЛДПР",
    "name": "Ананских Игорь Александрович"
  },
  {
    "deputy_id": 99100750,
    "faction_id": 72100005,
    "faction_title": "ЛДПР",
    "name": "Лебедев Игорь Владимирович"
  }
]
```
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
``` GET /deputy/99111860 ```

### Example Response
```json
{
  "deputy_id": 99111860,
  "faction_id": 72100024,
  "faction_title": "ЕР",
  "name": "Кожевникова Мария Александровна"
}
```
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

### Example Response
```json
[
  {
    "faction_id": 72100004,
    "faction_title": "КПРФ"
  },
  {
    "faction_id": 72100005,
    "faction_title": "ЛДПР"
  },
  {
    "faction_id": 72100024,
    "faction_title": "ЕР"
  },
  {
    "faction_id": 72100027,
    "faction_title": "СР"
  }
]
```
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
``` GET /faction/72100004 ```

### Example Response
```json
{
  "faction_id": 72100004,
  "faction_title": "КПРФ"
}
```
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
|offset|Optional|chronological order offset of bills block returned|0|280|
|count|Optional|count of bills returned|100|1200|
|from|Optional|datetime less than datetime of any bill returned|None|20151231235959|
|to|Optional|datetime greater than datetime of any bill returned|None|20151231235959|

### Example Request
``` GET /bill/?from=20160315164956&count=2 ```

### Example Response
```json
[
  {
    "bill_id": 93809,
    "datetime": "20160315170400",
    "title": "О проекте постановления Государственной Думы № 1014500-6 \"О поручении Счетной палате Российской Федерации\" (о проверке в 2016 году финансово-хозяйственной деятельности Центрального банка Российской Федерации за 2013-2015 годы в части формирования и использования фондов, создаваемых из прибыли Банка России, а также использования сметы расходов Банка России, его структурных подразделений и учреждений) – Система анализа результатов голосований на заседаниях Государственной Думы"
  },
  {
    "bill_id": 93810,
    "datetime": "20160315170428",
    "title": "(2 чтение) О проекте федерального закона № 895685-6 \"О внесении изменений в отдельные законодательные акты Российской Федерации\" (уточнение правил наследования коммориентами) – Система анализа результатов голосований на заседаниях Государственной Думы"
  }
]
```
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

### Example Respone
```json
{
  "bill_id": 76179,
  "datetime": "Tue, 28 Feb 2012 17:11:46 GMT",
  "title": "(первое чтение) О проекте федерального закона № 1471-6 \"О внесении изменений в Федеральный закон \"О политических партиях\" (в части либерализации требований к созданию и деятельности политических партий) – Система анализа результатов голосований на заседаниях Государственной Думы"
}
```
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
|faction_title||
- - -

## ```bill``` object

### Structure

|Field|Description|
|-----|-----------|
|bill_id||
|title||
|datetime||
- - -
