# Description runs tests and pycodestyle
# Usage: bash run.sh

# run your unit tests
python test_hw7.py
# run your functional tests
bash test_hw7.sh
#t est your python scripts with pycodestyle
pycodestyle $(git ls-files "*.py")
cd ../
pycodestyle $(git ls-files "*.py")
