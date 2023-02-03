# climate-hazards-coexistence-medicare-nc


## Data sources

1. ESRI

Space resolution: zip code

```
temperature 
humidity 
smoke
pm2.5
```

Time: 2006 - 2021

2. NSAPH Exposure

```
o3
no2
```

Time: 2006 - 2016

## New metrics

1. polluted day P

- P(pm2.5)
- P(no2)
- P(o3)
- AQI(pm2.5, no2, o3)

A day is polluted if the concentration is higher than the US EPA standard.

2. heatwave day

A heatwave day is a day when average daily temperature is higher than 95 percentile for that place all-time.

It can be 1 or 0 for each day and place.

3. hotspot 

**Induvidual:**

```
Hotspot_i = # of events when WF happened 
```

event = one wild fire than can last for multiple days

**Joint:**

```
Hotspot = HW & P & WF
```

We want to find:
- # hotspot days per location

Example:

```
Hotspot = 1 & 1 & 1
Hotspot = 1
```

4. time lag between climate hazards t

- t(first_hazard, second_hazard)
- t(wf, heatday)
- t(wf, polluted_day)
- t(heatday, polluted_day)

