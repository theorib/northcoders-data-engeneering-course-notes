# 2025-05-22 - Day 46 | Architecture

## Architecture
### LTP 
transctions is what our business cares about, adding an item to the stock, a chat message, 


A **pipeline**, is an automated process that has multiple steps

### 1. ingestion
- leave data where it is, or
- batch process, or
- realtime streaming of data or,

### ETL - Extract Transform Load
    once transformed you can't untransform?
- lots of data cleansing required
- Warehouse storage is limited

ELT - Extract Load Transform
- raw data is useful
- many different future transformations are possible
- very parallelisable

### Datamart
- Data warehouse split up in many different ones

### Data Lake (fancy file storage)
- when data is fundamentally best stored as files
- data lake tools exist to sit between our file storage and give us query abilities

### Data Lakehouse
- a Lake attached to a warehouse via a pipeline

### Compliance/Governance Layer
- basically a transformation step concerned with privacy and or legal issues such as personal data obfuscation, etc.
- can be placed in different positions in the pipeline and the position is critical
- it's all about keeping the data we must keep, and getting rid of data we must not keep
- Normally defined by legal departments
- access to data
- gdpr

### Top-down vs Bottom-up
- wether you start from big centralised databases and split it up
- start as many small sources and consolidate in to one or less

## Final Project
- Give yourself One Goal
- Consider any gaps in your knowledge at this point.
- Give yourself a development goal.
- Acknowledge the aim of the next phase of the bootcamp is consolidation of learning, not product production.
- Understand that progress together as a team is more valuable than a subset of the team delivering a polished outcome.
- Understand that staying in your comfort zone will only make it harder after graduation.


