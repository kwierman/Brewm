from invoke import ctask as task
from django.contrib import sites
from django.db.models import signals

@task
def clean(ctx):
    ctx.run('find . -name "*.pyc" -exec rm -rf {} \;')

@task
def syncdb(ctx):
    """Run a syncdb."""
    local('%(run)s syncdb --noinput' % env)


@task
def migrate(ctx,app=None):
    """Apply one (or more) migrations. If no app is specified, fabric will
    attempt to run a site-wide migration.

    :param str app: Django app name to migrate.
    """
    if app:
        ctx.run('%s migrate %s --noinput' % (env.run, app))
    else:
        ctx.run('%(run)s migrate --noinput' % env)

@task(aliases=['m'])
def manage(ctx,command='help'):
    man = 'python {path}/manage.py {command}'.format(path = '.', command = command )
    run(man)


@task
def shell(ctx):
    manage('shell_plus')

@task(aliases=['cc'])
def collectstatic(ctx):
    # brunchbuild()
    manage(ctx,'collectstatic --noinput')

@task
def defaultsettings(ctx):
    ctx.run('cp Brewm/settings/default.py Brewm/settings/local.py')

@task
def ready(ctx):
    ctx.run('. ./brewnode/bin/activate')

@task
def setupnode(ctx):
    ctx.run('rm -rf brewnode')
    ctx.run('nodeenv brewnode')
    ctx.run('. ./brewnode/bin/activate')
    ctx.run('npm install')
    #run('npm init')  # taking all defaults
    #run('npm install bootstrap font-awesome jquery --save')  # the core libraries we need
    #run('npm install webpack  --save') # the builder
    #run('npm install extract-text-webpack-plugin --save')  # plugin to break apart files
    #run('npm install css-loader style-loader file-loader less-loader babel-loader --save')

@task
def initdb(ctx):
    ctx.run('python manage.py loaddata Brewm/fixtures/initial_data.json')
