from invoke import task


@task(help={
    'ip': 'IP to listen on, defaults to *',
    'extra': 'Port to listen on, defaults to 8888',
})
def lab(ctx, ip='*', port=8888):
    """
    Launch Jupyter lab
    """
    cmd = ['jupyter lab', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))


@task(help={
    'ip': 'IP to listen on, defaults to *',
    'extra': 'Port to listen on, defaults to 8888',
})
def notebook(ctx, ip='*', port=8888):
    """
    Launch Jupyter notebook
    """
    cmd = ['jupyter notebook', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))


{%- if cookiecutter.for_kaggle == true -%}
@task(help={
    'search': 'search term'
})
def competition_list(ctx, search=None):
    """
    List Kaggle competitions
    """
    cmd = ['kaggle competitions list']
    if search:
        cmd = cmd + ['-s {}'.format(search)]
    ctx.run(' '.join(cmd))


@task(help={
    'competition': 'competition url prefix'
})
def competition_download_files(ctx, competition):
    """
    Download Kaggle competition files to ./data/raw folder
    """
    cmd = 'kaggle competitions download -c {} -p ./data/raw/'.format(competition)
    ctx.run(cmd)


@task(help={
    'path': 'path to file to submit',
    'message': 'message describing the submission',
    'competition': 'competition url prefix'
})
def competition_submit_files(ctx, path, message, competition):
    """
    Submit Kaggle competition files
    """
    cmd = 'kaggle competitions submit', '-c {} -f {} -m {}'.format(competition, path, message)
    ctx.run(cmd)
{% endif %}


@task()
def tests(ctx):
    """
    Run Unit Tests and Coverage
    """
    unit_tests(ctx)
    coverage(ctx)


@task()
def unit_tests(ctx):
    """
    Run Unit Tests
    """
    cmd = ["coverage", "run", "-m", "pytest", "tests/"]
    ctx.run(' '.join(cmd))


@task()
def coverage(ctx):
    """
    Run Unit Tests
    """
    commands = [
        "coverage report -m",
        "coverage html -d htmlcov",
        "coverage-badge -f -o ./docs/assets/unit-test-badge.svg",
    ]
    for command in commands:
        ctx.run(command)
