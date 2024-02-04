PYTHON_VERSION ?= "3.11"


all: install migrate lint server

server:
	 . env/bin/activate && python$(PYTHON_VERSION) manage.py runserver 8080

debug:
	 . env/bin/activate && python$(PYTHON_VERSION) -m debugpy --listen 0.0.0.0:6969 --wait-for-client  manage.py runserver 8080

clean:
	rm -rf env/

install:
	python$(PYTHON_VERSION) -m venv env
	. env/bin/activate && pip$(PYTHON_VERSION) --version
	. env/bin/activate && python$(PYTHON_VERSION)  -m pip install --upgrade pip
	. env/bin/activate && pip$(PYTHON_VERSION) --version
	. env/bin/activate && pip$(PYTHON_VERSION) install -r requirements.txt --use-pep517

migrate:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py migrate

revert_migrate:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py migrate ${app} ${migration}

migrations:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py makemigrations

empty-migrations:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py makemigrations --empty ${app}

superuser:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py createsuperuser

startapp:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py startapp ${app_name}

format:
	. env/bin/activate && black .

lint:
	. env/bin/activate && pylint --fail-under 9.0 --load-plugins pylint_django --disable=duplicate-code app/*.py common/*.py common/**/*.py api/*.py api/**/*.py tasks/*.py user/*.py user/templatetags/*.py survey/*.py survey/models/*.py survey/tests/*.py survey/view_models/*.py khadamati/*.py khadamati/management/commands/*.py cms/*.py cms/**/*.py cms/views/*.py cms/views/dashboard/*.py configuration/*.py

test:
	TESTS_DB="True"  . env/bin/activate && python$(PYTHON_VERSION) manage.py test --pattern="test_*.py"

test_app:
	TESTS_DB="True"  . env/bin/activate && python$(PYTHON_VERSION) manage.py test ${app} --pattern="test_*.py"

shell:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py shell

makemessages:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py makemessages -l en --ignore env*
	. env/bin/activate && python$(PYTHON_VERSION) manage.py makemessages -l ar --ignore env*

compilemessages:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py compilemessages

collect_static:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py collectstatic --noinput


greenkeeping:
	. env/bin/activate && pur -r requirements.txt

runcommand:
	. env/bin/activate && python$(PYTHON_VERSION) manage.py $(command) $(extra_arg)

