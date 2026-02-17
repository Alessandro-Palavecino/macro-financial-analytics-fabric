# Bronze Layer Design

## Purpose

The Bronze layer stores raw data retrieved directly from external APIs without business transformations.

## Data Characteristics

- Raw JSON from FRED API
- Full historical data load (initial ingestion)
- Stored with ingestion timestamp
- Partitioned by year and month (based on observation date)

## Table Structure (Conceptual)

bronze_us_cpi

Columns:

- date (DATE)
- value (FLOAT)
- ingestion_timestamp (TIMESTAMP)
- source (STRING)
- load_type (STRING)  # FULL or INCREMENTAL

## Storage Format

Delta Lake format

## Data Governance

- No transformations applied
- Only schema validation
- API response logged
- Ingestion errors recorded

## Future Improvements

- Implement incremental load by checking max(date)
- Add retry mechanism
- Add API call logging table
