

### TopographicPlace

```
# NeTEx annotation: 
***A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | created |  |  | 
| Attribute | modification |  |  | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Attribute | changed |  |  | 
| Element | gis:Polygon |  |  | 
| Element | IsoCode |  |  | 
| Element | TopographicPlaceType |  |  | 
| Reference | [CountryRef](Country.md) |  | ***Reference to a country ISO 3166-1 Note that GB is used for UK . May be qualified with a 3166-2 subdivision e.g. gb +m ENG, GB + SCT, GB See www.iso.org/iso/country_codes/iso_3166_code_lists.htm.*** | 
| Reference | [ParentTopographicPlaceRef](ParentTopographicPlace.md) |  |  | 
| List | ValidBetween | FromDate | ***OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT.*** | 
| List | Descriptor | Name |  | 
