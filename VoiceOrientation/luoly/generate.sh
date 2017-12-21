#!/bin/sh

# Current directory is luoly

cd sound 
rm -rf log
mkdir log
python kws_cch.py
cd ..
python generatePar.py sound/log/test
python generateResult.py sound/log/test


