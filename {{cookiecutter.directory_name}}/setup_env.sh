source env/scripts/activate
python -m ipykernel install --user --name {{cookiecutter.directory_name}}
pip install -r requirements.txt
