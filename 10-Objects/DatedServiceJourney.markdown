# DatedServiceJourney
  
>[!NOTE]
>A particular ServiceJourney of a vehicle on a particular OperatingDay.
>
>Operational details of the DatedServiceJourney is derived from a referenced generic ServiceJourney. The generic Journey cannot specify dayTypes when this is defined by the OperatingDay of the DatedServiceJourney.
>
>See definition under General information
>
>Defined in TimetableFrame
>
>Examples in the GitHub-repository
>
>NB:
>This data type is under Nordic revision, where its core structure is currently operational but supplementary data / improvements may be introduced in the NeTEx profile at a later stage.

<br>

<details open>
<summary>
  <b>Full overview</b>
</summary>

| XML-type | Name | Type | Cardinality 
|-|-|-|:-:|
| Attribute |<b><a name="dated-service-journey-id"></a>Id | ObjectIdType |<font color="red"> 1:1|
| Element |<b>BlockRef | Reference |<font color="red"> 0:1| 
| Element |<b>ServiceJourneyRef | ServiceJourneyRef |<font color="red"> 1:1|
| Element |<b>DatedServiceJourneyRef|DatedServiceJourneyRef|<font color="red">0:*|
| List |<b>OperatingDayRef|OperatingDayRef|<font color="red">1:1|

</details>
<details>
<summary>
  <b>Minimum overview</b>
</summary>

| Name | Type | Cardinality | Description |
|-|-|:-:|-|
|<b>ServiceJourneyRef | ServiceJourneyRef |<font color="red"> 1:1| Reference to the generic ServiceJourney from which journey details e.g. JourneyPatternRef and passingTimes is derived |
|<b>OperatingDayRef|OperatingDayRef|<font color="red">1:1||

</details>
<details>
<summary>
  <b>Reservation overview</b>
</summary>
<h1>Test Header</h1>

| Name | Type | Cardinality | Description |
|-|-|:-:|-|
|<b>BlockRef | Reference |<font color="red"> 0:1| |
|<b>ServiceJourneyRef | ServiceJourneyRef |<font color="red"> 1:1| Reference to the generic ServiceJourney from which journey details e.g. JourneyPatternRef and passingTimes is derived |
|<b>OperatingDayRef|OperatingDayRef|<font color="red">1:1||

</details>
<details>
<summary>
  <b>Sales overview</b>
</summary>
<br>
  
| Name | Type | Cardinality | Description |
|-|-|:-:|-|
|<b>ServiceJourneyRef | ServiceJourneyRef |<font color="red"> 1:1| Reference to the generic ServiceJourney from which journey details e.g. JourneyPatternRef and passingTimes is derived |
|<b>OperatingDayRef|OperatingDayRef|<font color="red">1:1||
|<b>replacedJourneys|DatedVehicleJourneyRef|<font color="red">0:*|List of DatedServiceJourneys replaced|

<br>
  Something something sales related
</details>

<br>

>[!TIP]
>[DatedServiceJourney](#dated-service-journey-id)
