#!/bin/bash
DATE=`date +%Y-%m-%d`
MONTH=`date +%Y-%m`
tar cvfj /tmp/backup-${DATE}.tar.bz2 /backup
aws cp /tmp/backup-${DATE}.tar.bz2 s3://${BUCKET}/${MONTH}/backup-${DATE}.tar.bz2
