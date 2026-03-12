#!/bin/bash
df -h | awk 'NR>1 {
    print $1, $5
    if ($5 > 90) print "WARNING: Partition", $1, "is filled at", $5
}'
