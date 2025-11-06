

### ServiceJourney

```
# NeTEx annotation: 
A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.

The VIEW includes derived ancillary data from referenced entities.
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | Name |  |  | 
| Element | PrivateCode |  | A private code that uniquely identifies the element.  May be used for inter-operating with other (legacy) systems. | 
| Element | Description |  |  | 
| Element | TransportMode |  |  | 
| Reference | [JourneyPatternRef](JourneyPattern.md) |  | Reference to a JOURNEY PATTERN. | 
| Reference | [OperatorRef](Operator.md) |  | Reference to an OPERATOR. | 
| Reference | [LineRef](Line.md) |  | Reference to a LINE. | 
| Reference | [FlexibleLineRef](FlexibleLine.md) |  | Reference to a FLEXIBLE LINE. | 
| List | dayTypes | DayTypeRef |  | 
| List | passingTimes | TimetabledPassingTime |  | 
| List | keyList | KeyValue | A list of alternative Key values for an element. | 
| List | TransportSubmode | BusSubmode | A submode of a Public Transport MODE. | 
| List | TransportSubmode | RailSubmode | A submode of a Public Transport MODE. | 
