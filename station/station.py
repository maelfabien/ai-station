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
        help='Generate a template for an AI project'
    )
    init_parser.set_defaults(func=init)
    init_parser.add_argument(
        '--name',
        dest='name',
        type=str,
        nargs=1,
        help='name of package',
        required=True)
    init_parser.add_argument(
        '--author',
        dest='author',
        type=str,
        nargs=1,
        help='name of author',
        required=True)

    # install
    install_parser = commands.add_parser(
        'install',
        help='Install os and python dependencies for your project'
    )
    install_parser.set_defaults(func=install)

    # pipeline
    pipeline_parser = commands.add_parser(
        'pipeline',
        help='Execute your project steps under /project/pipeline'
    )
    pipeline_parser.set_defaults(func=pipeline)
    pipeline_parser.add_argument(
        '--download',
        action='store_const',
        const='True',
        help='downloading data',
        required=False)
    pipeline_parser.add_argument(
        '--processing',
        action='store_const',
        const='True',
        help='processing data',
        required=False)
    pipeline_parser.add_argument(
        '--train',
        action='store_const',
        const='True',
        help='training model',
        required=False)
    pipeline_parser.add_argument(
        '--predict',
        dest='input',
        type=str,
        nargs=1,
        help='input path',
        required=False)

    # tests
    tests_parser = commands.add_parser(
        'tests',
        help='Manage your tests under /tests'
    )
    tests_parser.set_defaults(func=tests)

    # jupyterlab
    lab_parser = commands.add_parser(
        'lab',
        help='Start jupyter lab'
    )
    lab_parser.set_defaults(func=lab)

    # flask
    flask_parser = commands.add_parser(
        'flask',
        help='Start a flask server to serve your AI web app'
    )
    flask_parser.set_defaults(func=flask)

    # tensorboard
    tensorboard_parser = commands.add_parser(
        'tb',
        help='Start a tensorboard server with your project under in /logs'
    )
    tensorboard_parser.set_defaults(func=tb)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        pass


def init(args):
    """Generate a template for an AI project
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
    """Install os and python dependencies for your project
    """

    subprocess.call('sh requirements/requirements-os.sh', shell=True)
    subprocess.call('pip3 install -e .', shell=True)


def pipeline(args):
    """Execute your project steps under /project/pipeline
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
    """Manage your tests under /tests
    """

    subprocess.call('pytest', shell=True)
    subprocess.call('pytest --flake8', shell=True)
    subprocess.call('pytest --cov={} tests/'.format(os.getcwd().rsplit('/', 1)[-1]), shell=True)
    print('all tests passed ✅')


def lab(args):
    """Start jupyter lab
    """

    subprocess.call('jupyter lab --ip=0.0.0.0 --allow-root &', shell=True)


def flask(args):
    """Start a flask server to serve your AI web app
    """

    project_app = os.path.join(os.getcwd(), os.getcwd().rsplit('/', 1)[-1], 'app.py')
    subprocess.call('FLASK_APP={} flask run -h 0.0.0.0 --without-threads'.format(project_app), shell=True)


def tb(args):
    """Start a tensorboard server with your project under in /logs
    """

    if 'tensorboard' not in sys.modules:
        subprocess.call('pip3 install tensorflow tensorboard', shell=True)
    subprocess.call('tensorboard --host 0.0.0.0 --logdir=logs', shell=True)


if __name__ == '__main__':
    main()
