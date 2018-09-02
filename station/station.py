#!/usr/bin/env python3

"""
ai-station

a swiss knife for building your next machine learning project.

More info: https://github.com/fmikaelian/ai-station
"""

import os
import sys
import argparse
from jinja2 import Environment, FileSystemLoader
from shutil import copytree, ignore_patterns
import glob
import station
import textwrap
import subprocess


def main():
    """Contains information about the parsers and their arguments.
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
            Welcome to

                   _       __       __  _
             ___ _(_) ___ / /____ _/ /_(_)__  ___
            / _ `/ / (_-</ __/ _ `/ __/ / _ \/ _ \.
            \_,_/_/ /___/\__/\_,_/\__/_/\___/_//_/
                                           v0.0.1

            A swiss knife for building your next machine learning project.
            '''))

    commands = parser.add_subparsers(help='common commands')

    parser.add_argument(
        '--version',
        action='version',
        version='station %s' % station.__version__
    )

    # init
    init_parser = commands.add_parser(
        'init',
        help='Generate a base template for your machine project.'
    )
    init_parser.set_defaults(func=init)
    init_parser.add_argument(
        '--name',
        dest='name',
        type=str,
        nargs=1,
        help='Name of package',
        required=True)
    init_parser.add_argument(
        '--author',
        dest='author',
        type=str,
        nargs=1,
        help='Name of author',
        required=True)

    # install
    install_parser = commands.add_parser(
        'install',
        help='Install OS dependencies + your project as a python package.'
    )
    install_parser.set_defaults(func=install)

    # pipeline
    pipeline_parser = commands.add_parser(
        'pipeline',
        help='Execute one of your machine learning steps located in /project/pipeline.'
    )
    pipeline_parser.set_defaults(func=pipeline)
    pipeline_parser.add_argument(
        '--download',
        action='store_const',
        const='True',
        help='Downloading data',
        required=False)
    pipeline_parser.add_argument(
        '--processing',
        action='store_const',
        const='True',
        help='Processing data',
        required=False)
    pipeline_parser.add_argument(
        '--train',
        action='store_const',
        const='True',
        help='Training model',
        required=False)
    pipeline_parser.add_argument(
        '--predict',
        dest='input',
        type=str,
        nargs=1,
        help='Input path',
        required=False)

    # tests
    tests_parser = commands.add_parser(
        'tests',
        help='Performs unit-tests, pep8 checks and coverage reports for your tests located in /tests.'
    )
    tests_parser.set_defaults(func=tests)

    # flask
    flask_parser = commands.add_parser(
        'flask',
        help='Start a flask server to serve your demo web app with defined server config.'
    )
    flask_parser.set_defaults(func=flask)
    flask_parser.add_argument(
        '--dev',
        action='store_const',
        const='True',
        help='Serve app with flask development server',
        required=False)
    flask_parser.add_argument(
        '--prod',
        action='store_const',
        const='True',
        help='Serve app with gunicorn production server',
        required=False)

    # jupyterlab
    lab_parser = commands.add_parser(
        'lab',
        help='Start jupyter lab.'
    )
    lab_parser.set_defaults(func=lab)

    # tensorboard
    tensorboard_parser = commands.add_parser(
        'tb',
        help='Start a tensorboard server to display your logs located in /logs.'
    )
    tensorboard_parser.set_defaults(func=tb)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        pass


def init(args):
    """Generate a base template for your machine project.
    """

    cwd = os.getcwd()
    project_name = args.name[0]
    project_author = args.author[0]
    path_project = os.path.join(cwd, project_name)
    path_template = os.path.dirname(os.path.abspath(station.__file__)) + '/template'
    copytree(src=path_template, dst=path_project, ignore=ignore_patterns('__pycache__', '*.pyc'))
    FNULL = open(os.devnull, 'w')
    subprocess.call('sphinx-quickstart -q -p={} -a={} --ext-autodoc {}/docs/sphinx &>/dev/null'.format(project_name, project_author, path_project), stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
    path_template_files = [path for path in glob.iglob(path_project + '/**/*.*', recursive=True)]
    template_files = [path.replace(path_project + '/', '') for path in path_template_files]
    template_files.append('LICENSE')
    env = Environment(loader=FileSystemLoader(path_project))
    for template_file in template_files:
        try:
            template_file_env = env.get_template(template_file)
        except Exception as e:
            # print('Warning on file {}: {}'.format(template_file, e))
            pass
        output = template_file_env.render(project_name=project_name, project_author=project_author)
        with open(os.path.join(path_project, template_file), 'w') as f:
            f.write(output)
            f.close()
    os.rename(path_project + '/project_name', os.path.join(path_project, project_name))

    try:
        print('{} project created 👏'.format(project_name))
    except UnicodeEncodeError:
        print('{} project created'.format(project_name))


def install(args):
    """Install OS dependencies + your project as a python package.
    """

    subprocess.call('sh requirements/requirements-os.sh', shell=True)
    subprocess.call('pip3 install -e .', shell=True)


def pipeline(args):
    """Execute one of your machine learning steps located in /project/pipeline (eg. --train or --predict).
    """

    project_name_pipeline = os.path.join(os.getcwd(), 'sasekoi', 'pipeline')

    if args.download:
        print('downloading data')
        subprocess.call('time python3 {}/download.py'.format(project_name_pipeline), shell=True)
    if args.processing:
        print('processing data')
        subprocess.call('time python3 {}/processing.py'.format(project_name_pipeline), shell=True)
    if args.train:
        print('training model')
        subprocess.call('time python3 {}/train.py'.format(project_name_pipeline), shell=True)
    if args.input:
        print('running inference')
        subprocess.call('time python3 {}/predict.py --input {}'.format(project_name_pipeline, args.input[0]), shell=True)


def tests(args):
    """Performs unit-tests, pep8 checks and coverage reports for your tests located in /tests.
    """

    subprocess.check_call('pytest --flake8 --cov={}'.format(os.getcwd().rsplit('/', 1)[-1]), shell=True)
    subprocess.call('codecov -t {}'.format(os.environ['CODECOV_TOKEN']), shell=True)


def lab(args):
    """Start jupyter lab
    """

    subprocess.call('jupyter lab --ip=0.0.0.0 --allow-root &', shell=True)


def flask(args):
    """Start a flask server to serve your demo web app with defined server config (eg. --dev or --prod).
    """

    if args.dev:
        subprocess.call('FLASK_APP=app.py flask run -h 0.0.0.0 --without-threads', shell=True)
    if args.prod:
        subprocess.call('gunicorn --bind 0.0.0.0:80 --daemon --workers 1 --timeout 60 --access-logfile logs/access.txt --error-logfile logs/error.txt app:app', shell=True)


def tb(args):
    """Start a tensorboard server to display your logs located in /logs.
    """

    if 'tensorboard' not in sys.modules:
        subprocess.call('pip3 install tensorflow tensorboard', shell=True)
    subprocess.call('tensorboard --host 0.0.0.0 --logdir=logs', shell=True)


if __name__ == '__main__':
    main()
