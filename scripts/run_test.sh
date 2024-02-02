SH=$(cd `dirname ${BASH_SOURCE:-$0}` && pwd)
AH=`cd $SH/.. && pwd`

cd $AH

PYTHONPATH=$AH       \
python -m pipenv run \
   python -m pytest
