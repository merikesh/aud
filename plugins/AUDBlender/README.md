# AUD for Blender

AUD is an exporter for Blender to write out files compatible with Pixar's USD standard.

It currently can only export static meshes, and has no import capability. 

Over time it will gain more export options.

It only support **Blender 2.8 and above**.

## Installation

To install,

1. Download the zip file from the [releases page](https://github.com/merikesh/aud/releases)

2. In the zip you'll find a folder named **AUDBlender**. 
   
   Extract this to the addons locations (see below for common addons locations)

3. Open Blender and go to **Edit > Preferences > Add-Ons**

4. Locate **Export: AUD Exporter** in the add-ons list and enable it.


### Add-On Location

You can read more about [where to export the plugin](https://docs.blender.org/manual/en/dev/getting_started/installing/configuration/directories.html)
but I've listed some common locations below

#### Windows

`%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\2.80\`

#### macOS

`/Users/$USER/Library/Application Support/Blender/2.80/`

#### Linux

`$HOME/.config/blender/2.80/`


## Use

You can export `.usda` files using **Files > Export > AUD (.usda)**

## Contributions

I welcome any contributions on this [on the GitHub repository](https://github.com/merikesh/aud)

