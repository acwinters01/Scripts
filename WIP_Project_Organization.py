import unreal
import os

# assigning Libraries to variables
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
assets_cleaned = 0

# specific path
path_dir = "\\BasePath"

if num_assets > 0:
    # this gives full path for the provided asset
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
    # move file to the folder name matching asset name.
    path_dir = os.path.dirname(asset_path)

for asset in selected_assets:
    # get the class instance and the string name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    # Creating a new path and moving assets
    try:
        new_path = os.path.join(path_dir, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset_name, new_path)
        assets_cleaned += 1
        unreal.log("Cleaned {} and sent to {}".format(asset, new_path))
        # got an error when using asset_name needs an object not a string

    except Exception as err:
        unreal.log("{} couldn't be moved to new location {}".format(asset_name, new_path))

unreal.log("Cleaned {} out of {}".format(assets_cleaned, num_assets))
