

### Route

```
# NeTEx annotation: 
***An ordered list of located POINTs defining one single path through the Road (or rail) network. A ROUTE may pass through the same POINT more than once.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | Name |  |  | 
| Element | ShortName |  |  | 
| Reference | [LineRef](Line.md) |  | ***Reference to a LINE.*** | 
| Reference | [FlexibleLineRef](FlexibleLine.md) |  | ***Reference to a FLEXIBLE LINE.*** | 
| Reference | [InverseRouteRef](InverseRoute.md) |  |  | 
| List | pointsInSequence | PointOnRoute |  | 
