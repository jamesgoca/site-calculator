# Site Calculator

This script calculates the size of files recursively in a folder. I am using it to calculate the sizes of my website.

See a sample report in the [sample_report.txt](https://github.com/jamesgoca/site-calculator/blob/master/sample_report.txt) file.

## Installation

To get started, clone this repository:

```git clone https://github.com/jamesgoca/site-calculator```

Once you have cloned the repository, set up a virtual environment and install the required dependencies:

```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Next, set the path of the file that you want to access. This path is relative to your home directory (i.e. /Users/James). Open up the .env file and replace the calculate_folder variable:

```calculate_folder=/file/path```

Finally, run the app.py file:

```python3 app.py```

This project uses Python 3 so you will need to run it in a Python 3 shell.

## Screenshot

![Screenshot of the site calculator](https://github.com/jamesgoca/site-calculator/blob/master/screenshot.png?raw=true)

## License

This project is licensed using an MIT license. See more information in [LICENSE.md](https://github.com/jamesgoca/site-calculator/blob/master/LICENSE.md).

## Authors

- James Gallagher

## Checklist

- [ ] Finish README.md
- [ ] Upload project screenshot
