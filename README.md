# AUD

**AUD** ( /ɑd/ ), short for the Alternate USD Driver, is an "odd" library
for creating files that are compatible with 
[Pixar's USD](https://graphics.pixar.com/usd/docs/index.html).

It lets you write out **usda** files using USD's ascii format, without
requiring the USD libraries to be present on your system.

This can be extremely useful if you need to create usda files but where building the USD 
libraries is either difficult or impossible.

## Current Status

This repository is currently under development.
It currently is non functional and is currently capable of extracting the schemas from USD's source code
into a skeleton in Python.

The next step is writing out USD files succesfully and making a plugin for Blender.

## Caveat

This library is not officially related to Pixar in anyway, and comes with no semblence of support.

This library is partly automatically generated from Pixar's USD source code, as well as manually
written. As such it should be easy to keep it up to date with the latest versions of USD as they
release, however, by using this library you must understand that the output from it may not be
correct and there is no obligation for either myself or Pixar to support any errors from its output.

## Building

To build this library, run the `build.py` script found in the root of this repository.

This will automatically download the latest version of the USD source code if it cannot find it,
and will generate new versions of the library from that.

It does not compile USD, instead, it will extract the necessary schema data from the source.

## Dependencies

It is important that this library have no external dependencies, other than the one time 
download of the USD source code when building.

As such, the only requirement is that there is either Python 3 or Python 2 present, and the 
library promises to be compatible with both, at least until the Python 2 EOL.

## Repository Structure

### Main Source

The main source code is stored under the `aud` directory. 
Under here, `base.py` provides the base classes needed for this library.

In the `generated` directory we'll find the extracted schemas. 
We may also place files with the same name as the schemas under the main source root,
when we decide to provide extra functionality that the generated classes don't support
e.g. convenience methods

This structure allows users to write `from aud import audGeom` and get our convenience class if
it exists, otherwise it will fall back to the generated class.


### Build Scripts

All code required to build this library will be stored under the `build` directory.

None of this code should be distributed with the library.

### Plugins

Plugins for various applications should be stored under the `plugins` directory with a name
`AUD<ApplicationName>`. For example, the Blender plugin should be `AUDBlender`.

## License

This library is licensed under the MIT license.
