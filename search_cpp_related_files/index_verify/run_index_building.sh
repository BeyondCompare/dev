#!/bin/sh

cd $(dirname $0)

set -e

mkdir -p log

rm -rf t_app_info t_app_download t_app_quality_score t_app_coreword t_app_cluster t_qanchor_info t_aso_app_message t_appointment_game



# 由陈兵提供
java -jar comsearch-hive-read-1.0-SNAPSHOT-jar-with-dependencies.jar

python main.py > log/main.out 2>log/main.err