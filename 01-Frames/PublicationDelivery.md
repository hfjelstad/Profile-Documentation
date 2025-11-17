## Exchanging information
Information exchanged in the NeTEx format should be XML files containing only one root tag: PublicationDelivery

The information should be delivered with one XML file per Line, packed as ZIP-file with a flat structure (no subdirectories). It is technically possible to deliver each line separately, packed in separate ZIP-files if all the data objects used by each Line are defined within its PublicationDelivery. However, in order to avoid issues with overwriting and ensure good data update/deletion management, it is strongly recommended that only complete datasets containing all lines are exchanged. Data objects used by multiple Lines can be defined in a separate "common" XML-file (must be prefixed with an underscore, e.g. "_common.xml") to avoid redundancy of unique objects.

Each PublicationDelivery must contain the following two mandatory fields, other fields needed will be documented in each guide:

```xml
<PublicationTimestamp> [data extraction time] </PublicationTimestamp>
<ParticipantRef> [codespace for data submitter] </ParticipantRef>
```

Within a PublicationDelivery, **dataObjects**  are defined, which consist of a set of Frames. Each frame contains all relevant objects in a single group and specifies common validity conditions, e.g. validity and version. This mechanism supports incremental updating of individual objects in cases where the relationships between the objects are not altered and will assist in troubleshooting down to the object- or group level.

PublicationDelivery allows for any number of frames, and the same frame type can be reused multiple times. It is good practice to use as few frames as possible so that the grouping within the same PublicationDelivery is appropriate (avoid "wrapping" objects into their own frames). Objects that naturally belong together, i.e. have the same version and validity, must be collected in the same frame.

In [Gudies](/04-Guides/Guides.md) you will find many examples of how to publish data

## Data submission in CompositeFrame
When grouping Frames into a CompositeFrame, ValidityCondition must be the same for all its frames. That is, ValidityCondition is not set per frame, but is implicitly controlled from the CompositeFrame.

![PublicationDelivery in CompositFrame](/01-Frames/images/CompositFrame.png)
--
## Data submission as single frames

When frames are not grouped in a CompositeFrame, all relevant frames must have explicitly defined ValidityConditions.

![PublicationDelivery as singe frames](/01-Frames/images/SingleFrame.png)
--
