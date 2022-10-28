""" Setup script for tudsv """

from setuptools import setup

setup(name='tudsv',
      version='0.3',
      description='Supplemental material for the lecture Signalverarbeitung '
                  'at TU Dresden',
      url='https://github.com/TUD-STKS/tud-sv',
      author='Bernhard Schrank',
      author_email='bernhard.schrank@tu-dresden.de',
      license='MIT',
      packages=['tudsv'],
      include_package_data=True,
      install_requires=[
          'jupyterlab',
          'pandas',
          'scikit-learn',
          'tudthemes'
      ],
      entry_points={
          'console_scripts': [
              'tud-sv-start = tudsv.__main__:start_jupyter_server',
              'tud-sv-prepare-submission = tudsv.__main__:prepare_submission'
          ]
      }
      )
