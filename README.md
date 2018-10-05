Please install miniconda from https://conda.io/miniconda.html

Or alternatively (if you have brew) run:

`>> brew cask install miniconda`

And run: (add to your ~/.bash_profile for pemanent effect)
`>> . /usr/local/miniconda3/etc/profile.d/conda.sh`

Then to setup the necessary environment run:

`>> conda env create -f py3.yml`

You can then do:

`>> conda activate py3`

`>> python data_grabber.py`

The list of accounts and vendors will be written to json files in the working directory.
