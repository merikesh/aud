> **DEPRECATED**: Due to Blender adding native support for USD, the usefulness of this repository is approaching zero.
> So I will leave this up as a reference but will no longer maintain this. It was relatively unmaintained anyway due to work time conflicts.

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

Below are a list of requested and suggested features.

Note that not all features are planned to be implemented.


- [x] Extract USD schemas from USD Source code
- [x] Write out `.usda` files with support for
    * Stage properties
    * Hierarchies with support for classes, defs, and overs
    * Properties and Attributes for prims
    * References and inheritance
    * VariantSets and Variants
    * Time Samples
- [ ] Blender export plugin ( **WIP** )
- [ ] Validation of data against the schema
- [ ] Maya export plugin ( Maybe to check for parity with official plugin)
- [ ] Read support ( No plans )
- [ ] Support for reading/writing binary `.usd` files ( No plans )
- [ ] Support for reading/writing `.usdz` files ( No plans )

## Caveat

This library is not officially related to Pixar in anyway, and comes with no semblence of support.

This library is partly automatically generated from Pixar's USD source code, as well as manually
written. As such it should be easy to keep it up to date with the latest versions of USD as they
release, however, by using this library you must understand that the output from it may not be
correct and there is no obligation for either myself or Pixar to support any errors from its output.

## Building

To build this library, run the `aud/__build__/__init__.py` script found in the root of this repository.

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

All code required to build this library will be stored under the `__build__` directory.

This is distributed with the library but is not to be used by a third party.

### Plugins

Plugins for various applications should be stored under the `plugins` directory with a name
`AUD<ApplicationName>`. For example, the Blender plugin should be `AUDBlender`.

## License

This library is licensed under the MIT license.

## Contributions

Contributions are gladly accepted.

Please open an issue before starting work so we don't double up efforts accidentally.

Perform your work in a branch and make a pull request when you're ready or need to discuss anything.

