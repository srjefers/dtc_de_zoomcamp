# Week 01 - Homework

## Question 1. Google Cloud SDK
Install Google Cloud SDK. What's the version you have?
To get the version, run `gcloud --version`
> Google Cloud SDK 394.0.0<br>alpha 2022.07.19<br>beta 2022.07.19<br>bq 2.0.75<br>bundled-python3-unix 3.9.12<br>core 2022.07.19<br>gsutil 5.11

## Question 2. Terraform
Now install terraform and go to the terraform directory (week_1_basics_n_setup/1_terraform_gcp/terraform)

After that, run
* terraform init
* terraform plan
* terraform apply

Apply the plan and copy the output (after running apply) to the form.

It should be the entire output - from the moment you typed terraform init to the very end.
## Question 3. Count records
How many taxi trips were there on January 15?
Consider only trips that started on January 15.
``` sql
SELECT COUNT(1) 
FROM yellow_taxi_trips 
WHERE DATE_TRUNC('day',tpep_pickup_datetime) = TO_DATE('20220115','YYYYMMDD');
```
> **53024**
## Question 4. Largest tip for each day
Find the largest tip for each day. On which day it was the largest tip in January?
Use the pick up time for your calculations.
(note: it's not a typo, it's "tip", not "trip")
```sql
SELECT t.day_v, t.tip_amount 
FROM (
	SELECT 
		DATE_TRUNC('day',tpep_pickup_datetime) day_v, tip_amount, 
		RANK() OVER (PARTITION BY DATE_TRUNC('day',tpep_pickup_datetime) ORDER BY tip_amount DESC) rank_v 
	FROM yellow_taxi_trips
	WHERE EXTRACT(MONTH FROM tpep_pickup_datetime) = 1 AND tip_amount > 0
) t WHERE t.rank_v = 1
ORDER BY t.tip_amount DESC;
```
> **Date: 2021-01-20, Tip = 1140.44**

## Question 5. Most popular destination
What was the most popular destination for passengers picked up in central park on January 14?
Use the pick up time for your calculations.
Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown"
``` sql
SELECT 
	destinationid, dim_tz."Zone" 
FROM (
	SELECT 
		"DOLocationID" destinationid, 
		COUNT(1) cant, 
		RANK() OVER (ORDER BY count(1) desc) rank_v
	FROM yellow_taxi_trips 
	WHERE "PULocationID" = 43 
		AND DATE_TRUNC('day',tpep_pickup_datetime) = TO_DATE('20210114','YYYYMMDD')
	GROUP BY "DOLocationID"
) tmp
INNER JOIN dim_taxi_zone dim_tz ON dim_tz."LocationID" = tmp.destinationid
WHERE rank_v = 1;
```
> **Zone: _Upper East Side South_**

## Question 6. Most expensive locations
What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)?
Enter two zone names separated by a slash
For example:
"Jamaica Bay / Clinton East"
If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".

``` sql
SELECT 
	CONCAT(
		COALESCE(dim_tz_p."Zone", 'Unknown'),' / ',COALESCE(dim_tz_d."Zone", 'Unknown')
	)
FROM (
	SELECT 
		"PULocationID" pickup, "DOLocationID" dropoff, AVG(total_amount), RANK() OVER (ORDER BY AVG(total_amount) DESC) rank_v
	FROM yellow_taxi_trips 
	GROUP BY "PULocationID", "DOLocationID"
) tmp 
INNER JOIN dim_taxi_zone dim_tz_p ON dim_tz_p."LocationID" = tmp.pickup
INNER JOIN dim_taxi_zone dim_tz_d ON dim_tz_d."LocationID" = tmp.dropoff
WHERE tmp.rank_v = 1;
```
> **Alphabet City / Unknown**