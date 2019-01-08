import os
import shutil
import json
import sys
import logging
import pprint
import zipfile
import aud_usd_parser

logging.basicConfig()
logger = logging.getLogger('aud-builder')
logger.setLevel(logging.DEBUG)

PY2 = sys.version_info.major == 2
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOWNLOAD = os.path.join(ROOT, "download")

if PY2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


def copy_schemas(download_root, clean=False):
    download_root = os.path.expanduser(download_root)
    target_dir = os.path.join(ROOT, 'schemas')
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # Clean out the schema directory before copying stuff in there
    if clean:
        logger.debug('Cleaning out schemas')
        for schema in os.listdir(target_dir):
            full_path = os.path.join(target_dir, schema)
            if not os.path.isfile(full_path):
                continue
            os.remove(full_path)

    logger.debug('Copying schemas')
    for root, dirs, files in os.walk(download_root):
        for schema in files:
            if schema != "generatedSchema.usda": continue
            full_path = os.path.join(root, schema)
            if 'example' in full_path.lower() or 'test' in full_path.lower(): continue
            target = os.path.join(target_dir, '{}.usda'.format(os.path.basename(root)))

            shutil.copy2(full_path, target)

    logger.debug('Finished copying schemas')
    return target_dir

def download_usd(version=None, force=False, version_root=None, version_zip=None):
    """
    Download the USD file if it can be found
    Args:
        version (str): The version number to use. Defaults to using highest version.
        force (bool): Force redownload of the file and skip checks
        version_root (str): The optional location to check for the source root
        version_zip (str): The optional location to check for the source zip file

    Returns:
        str: The path to the version source

    """
    if not os.path.exists(DOWNLOAD):
        logger.debug("Creating download directory")
        os.mkdir(DOWNLOAD)

    version_root = version_root or os.path.join(DOWNLOAD, version.replace('.', '_'))
    if os.path.exists(version_root) and not force:
        logger.debug('Found existing download: %s', version_root)
        return version_root

    version_zip = version_zip or os.path.join(DOWNLOAD, '{}.zip'.format(version.replace('.', '_')))
    if not os.path.exists(version_zip) and not force:
        logger.debug('Could not find existing zip file (%s). Trying to find download file', version_zip)
        with urlopen("https://api.github.com/repos/PixarAnimationStudios/USD/tags") as tags:
            versions = response = json.loads(tags.read())

        if version:
            versions = [v for v in versions if v['name'][1:] == version]  # tag names are in format vXX.xx
            if not versions:
                raise RuntimeError(
                    "Could not find a USD version matching: {}. \n{}".format(version, pprint.pformat(response)))

        version_url = versions[0]['zipball_url']
        version_zip = os.path.join(DOWNLOAD, '{}.zip'.format(versions[0]['name'][1:].replace('.', '_')))
        version_root = version_zip.replace('.zip', '')

        if os.path.exists(version_zip):
            logger.info('Found existing zip file: %s', version_zip)
        else:
            logger.info('Downloading %s to %s', version_url, version_zip)
            with urlopen(version_url) as u:
                with open(version_zip, 'wb') as f:
                    f.write(u.read())

            logger.info('Finished downloading USD file')

    logger.debug('Extracting zip file (%s) to (%s)', version_zip, version_root)
    with zipfile.ZipFile(version_zip) as f:
        f.extractall(version_root)

    return version_root

def generate_python(version, schema_root):
    source_root = os.path.join(ROOT, 'aud')
    generated_root = os.path.join(source_root, 'generated')
    if not os.path.exists(generated_root):
        os.mkdir(generated_root)

    logger.debug('Cleaning out generated directory')
    for generated in os.listdir(generated_root):
        full_path = os.path.join(generated_root, generated)
        if os.path.isfile(full_path):
            os.remove(full_path)

    aud_usd_parser.generate_python(version, schema_root, generated_root)


def main(version="19.01"):
    print("Running aud-builder using version {} of USD and Python {}.{}.{}".format(
        version, sys.version_info.major, sys.version_info.minor, sys.version_info.micro
    ))
    version_root = download_usd(version)
    schema_root = copy_schemas(version_root)
    generate_python(version, schema_root)


if __name__ == '__main__':
    main()
