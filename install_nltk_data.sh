# will install nltk data
# requires nltk installed either in virtualenv or global

# get python possibly from virtualenv
PYTHON=`which python`
sudo $PYTHON -m nltk.downloader -d /usr/share/nltk_data brown wordnet
